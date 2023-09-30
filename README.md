# Chatbot Streamlit App

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/balnarendrasapa/chatbot)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/balnarendrasapa/chatbot)
![GitHub](https://img.shields.io/github/license/balnarendrasapa/chatbot)

This streamlit is just an example of how a Large Language Model works. This streamlit is built upon FALCON-4B llm. This llm is light weight and does not require a GPU. 
This example are taken from langchain library. The link to the original [repo](https://github.com/langchain-ai/streamlit-agent/tree/main). But that chatbot requires you to have OPEN_AI API Key. You don't need that here. This is hosted on Huggingface Spaces. Link to the chatbot [site](https://huggingface.co/spaces/bnsapa/chat_lang)

## Development setup ⚙️

This repository contains a devcontainer.json file. You can either choose to open this in codespace or build a development environment locally. If you choose to develop locally, make sure to install the `Remote Development` extension in VSCode.

- If you want to open in codespaces, click on the above badge `Open in GitHub Codespaces` 🛠️
- If you want to open in VSCode locally, click on the above badge `Open in Dev Containers` 🛠️

## Running server 🏃‍♂️
### In Dev Environment 🛠️
- To run the server, run the command `make run`. This starts up the streamlit app. You can access the stremalit app through `localhost:8501` 🚀
- To stop the server, run `make stopserver` ⛔

### Using docker-compose in root 🐳

- To run using docker-compose, cd into the root directory and run `docker-compose up`. This may not be useful for development.
- There is an image available in this repository. If you just want to check this project out, download `other/docker-compose.yml` file and run `docker-compose up` 🐳
