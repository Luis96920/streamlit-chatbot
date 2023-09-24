.PHONY: run
run:
	streamlit run streamlit_apps/chat.py --server.port 8501 &

# stop server
.PHONY: stopserver
stopserver:
	fuser -k 8501/tcp
