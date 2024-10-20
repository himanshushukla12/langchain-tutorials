# Ollama Chat with Hugging Face Models

This project demonstrates how to create a simple chat application using Ollama to interact with Hugging Face models. It uses the `langchain_ollama` library to facilitate communication with the Ollama server.

## Prerequisites

- Python 3.7+
- Ollama installed and running on your system
- Required Python packages (install via `pip install -r requirements.txt`):
  - langchain_ollama
  - ollama
  - llama-cpp-python[cublas] # GPU enabled
  - gradio
## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ollama-huggingface-chat.git
   cd ollama-huggingface-chat
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Ensure Ollama is installed and running on your system. Follow the [Ollama installation guide](https://github.com/jmorganca/ollama#installation) if needed.

4. Download the desired Hugging Face model using Ollama. For example:
   ```
   ollama pull llama2
   ```

## Usage

1. Open `ollama_chat.py` and modify the model name if needed:
   ```python
   llm = OllamaLLM(model="llama2")
   ```

2. Run the chat application:
   ```
   python ollama_chat.py
   ```

3. Start chatting with the AI model. Type your messages and press Enter. The AI will respond in real-time.

4. To exit the chat, type 'exit' and press Enter.

## Features

- Real-time streaming of AI responses
- Conversation history maintained throughout the chat session
- Easy integration with different Hugging Face models supported by Ollama

## Customization

You can easily customize the chat application by modifying the `ChatApp` class in `ollama_chat.py`. Some possible enhancements include:
- Adding support for system prompts
- Implementing temperature and other generation parameters
- Creating a web-based interface

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.