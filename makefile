.PHONY: run
run:
	streamlit run streamlit_apps/chat.py --server.port 8501 &
	streamlit run streamlit_apps/chat_url.py --server.port 8502