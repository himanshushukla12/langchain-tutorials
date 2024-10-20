# README

## LangChain-Based Chat Application with Ollama and GGUF Models

This repository contains a beginner-friendly Python-based chat application that leverages **LangChain** to enable context-based chatting with AI models. The app is designed to work seamlessly with **Ollama** models and **GGUF** models, making it easy for users to switch between different types of AI models for their chatbot needs.

### Repository Link

[https://github.com/himanshushukla12/langchain-tutorials](https://github.com/himanshushukla12/langchain-tutorials)

---

## Overview

This project demonstrates how to build a context-aware chat application using LangChain and models like **Ollama** and **GGUF**. The chat application stores the entire conversation history in a variable, which allows the AI to maintain context throughout the interaction. This approach ensures that the chatbot can understand and respond based on previous messages, leading to more coherent and relevant conversations.

### Key Features

- **Context-Aware Chatting**: The chat application maintains a history of user and AI messages, allowing the AI to reference earlier parts of the conversation for a more natural and engaging experience.
- **Support for Multiple Model Types**:
  - **Ollama Models**: Easily integrate with models from Ollama using the `OllamaLLM` wrapper.
  - **GGUF Models**: Support for running GGUF models using `LlamaCpp`, making it versatile for various local AI models.
- **Beginner-Friendly Code**: The code is structured to help newcomers understand the basics of working with **LangChain** and how to implement a simple chat interface.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/himanshushukla12/langchain-tutorials.git
   cd langchain-tutorials
   ```

2. **Create a Virtual Environment** (Optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root of your project and add the following:
     ```
     OLLAMA_URL=http://localhost:11434  # Replace with your Ollama server URL if different
     ```

---

## Usage

The script allows you to choose between using **Ollama** models or **GGUF** models for chatting. Follow the instructions below to start a chat session:

1. **Run the Script**:
   ```bash
   python ollama_chat.py
   ```

2. **Choose a Model**:
   - When prompted, select the type of model you want to use:
     ```
     Do you want to use ollama, huggingface or gguf models? (ollama/huggingface/gguf):
     ```

3. **For Ollama Models**:
   - Enter the name of the model:
     ```
     Enter the model name: llama3.1
     ```

4. **For GGUF Models**:
   - Enter the path to the GGUF model:
     ```
     Enter the model path: /path/to/your/gguf-model
     ```

5. **Start Chatting**:
   - The chat application will initialize, and you can begin typing your messages:
     ```
     Chat App Initialized. Type 'exit' to stop.

     You: Hello!
     AI: Hi there! How can I assist you today?
     ```

6. **Type 'exit' to End the Chat**:
   - To terminate the chat session, type:
     ```
     You: exit
     Exiting chat...
     ```

---

## How It Works

### ChatApp Class

The `ChatApp` class is designed to manage the conversation flow:

- **Initialization**: Takes an LLM instance (Ollama or GGUF) and initializes the conversation history.
- **Message Handling**: The `add_message` method allows adding user and AI messages to the conversation history.
- **Streaming Responses**: Uses the `stream_response` method to stream AI responses in real-time, providing a dynamic chat experience.
- **Context Management**: Keeps track of all user and AI messages, enabling context-aware conversations.

### Ollama Chat

The `Ollama_chat` function initializes an Ollama LLM and starts a chat session. This function makes it easy to integrate with Ollama models and manage conversations.

### GGUF Chat

The `Ollama_chat_gguf` function allows users to chat with GGUF models. By specifying the model path, users can load local GGUF models and start chatting without complex setup.

---

## Why Use This Project?

- **Learn LangChain**: This project is an excellent starting point for understanding how to integrate AI models with LangChain and build chat applications.
- **Easy Model Integration**: Whether you want to work with Ollama models or local GGUF models, this project provides a simple interface for both.
- **Context Management**: The app maintains conversation history, enabling more coherent and context-aware responses from the AI model.

---

## Contributions

Feel free to open issues or submit pull requests to improve the project. Contributions are always welcome!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Happy chatting! 😊