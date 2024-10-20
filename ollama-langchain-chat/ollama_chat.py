# importing the required libraries
from langchain_ollama import OllamaLLM
import os
from langchain_community.llms import LlamaCpp, Ollama
from dotenv import load_dotenv


load_dotenv()
# defining the chat app class
class ChatApp:
    def __init__(self, model):
        # Initialize the LLM with the specific model
        self.llm = model
        self.conversation_history = []

    def add_message(self, role, content):
        # Add each message to the conversation history
        self.conversation_history.append((role, content))

    def stream_response(self):
        # Send the current messages with context to the model
        messages = self.conversation_history
        stream = self.llm.stream(messages)  # Stream from the LLM
        
        full_response = ""
        try:
            # Print chunks as they are streamed
            for chunk in stream:
                full_response += chunk
                print(chunk, end="", flush=True)  # Show the chunk in real-time
        except StopIteration:
            # In case the stream ends unexpectedly
            pass
        
        print()  # Newline after full response
        return full_response

    def chat(self):
        print("Chat App Initialized. Type 'exit' to stop.\n")
        while True:
            # Get user input
            user_input = input("You: ")
            
            if user_input.lower() == "exit":
                print("Exiting chat...")
                break
            
            # Add the user's message to the history
            self.add_message("human", user_input)
            
            # Get and print the AI's response
            print("AI: ", end="", flush=True)  # Print "AI: " without newline
            ai_response = self.stream_response()
            
            # Add the AI's response to the history
            self.add_message("ai", ai_response)
# defining the ollama chat function
def Ollama_chat(model:str = "llama3.1"):
    ollama_url=os.getenv('OLLAMA_URL', 'http://localhost:11434')
    llm = OllamaLLM(model=model, base_url=ollama_url)
    chat_app = ChatApp(model=llm)
    chat_app.chat()

# defining ollama chat using gguf models
def Ollama_chat_gguf(model_path:str):
    llm = LlamaCpp(model_path=model_path,
                   n_gpu_layers=1,
                   )
    chat_app = ChatApp(model=llm)
    chat_app.chat()

# Example of how to use the ChatApp class
if __name__ == "__main__":

    # condition to choose between ollama, huggingface and gguf models or exit to stop the program
    choice = input("Do you want to use ollama, huggingface or gguf models? (ollama/huggingface/gguf): ")
    if choice == "ollama":
        model = input("Enter the model name: ")
        Ollama_chat(model)
    elif choice == "gguf":
        model_path = input("Enter the model path: ")
        Ollama_chat_gguf(model_path)
    else:
        print("Invalid choice")
