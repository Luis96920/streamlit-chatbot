from langchain.agents import ConversationalChatAgent, AgentExecutor
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain import HuggingFaceHub
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.chains import LLMChain, RetrievalQA
from langchain import PromptTemplate
import streamlit as st
import os
import dotenv

dotenv.load_dotenv()

HUGGINGFACE_API = os.getenv("HUGGINGFACE_API")

st.set_page_config(page_title="ChatBot", page_icon="😊")
st.title("ChatBot")

msgs = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(
    chat_memory=msgs, return_messages=True, memory_key="chat_history", output_key="output"
)
if len(msgs.messages) == 0:
    msgs.clear()
    msgs.add_ai_message("How can I help you?")
    st.session_state.steps = {}

avatars = {"human": "user", "ai": "assistant"}
for idx, msg in enumerate(msgs.messages):
    with st.chat_message(avatars[msg.type]):
        # Render intermediate steps if any were saved
        for step in st.session_state.steps.get(str(idx), []):
            if step[0].tool == "_Exception":
                continue
            with st.expander(f"✅ **{step[0].tool}**: {step[0].tool_input}"):
                st.write(step[0].log)
                st.write(f"**{step[1]}**")
        st.write(msg.content)

if prompt := st.chat_input(placeholder="Who won the Women's U.S. Open in 2018?"):
    st.chat_message("user").write(prompt)

    msgs.add_user_message(prompt)
    llm = HuggingFaceHub(
            repo_id="tiiuae/falcon-7b-instruct",
            model_kwargs={"temperature": 0.5, "max_new_tokens": 500},
            huggingfacehub_api_token=HUGGINGFACE_API,
        )
    prompt_template = PromptTemplate.from_template(
        "Answer the question: {prompt}"
    )
    qa_chain = LLMChain(llm = llm, prompt = prompt_template)
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = qa_chain({"prompt": prompt})
        msgs.add_ai_message(response["text"])
        st.write(response["text"])
