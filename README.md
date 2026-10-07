# Multi-Session Chatbot

A simple AI chatbot built using **LangChain** and **Ollama (qwen2.5:0.5b)** with support for multiple independent chat sessions.

## Features

- Chat with qwen2.5:0.5b locally using Ollama
- Maintains conversation history
- Create multiple chat sessions
- Switch between sessions
- View all available sessions
- View the current session
- Each session has its own independent memory

## Technologies Used

- Python
- LangChain
- Ollama
- qwen2.5:0.5b

## How It Works

The chatbot uses `RunnableWithMessageHistory` to manage conversation history.

Each session has a unique `session_id`, and the conversation history is stored separately for each session.

```text
User
  ↓
Chatbot
  ↓
Session ID
  ↓
Chat History
  ↓
qwen2.5:0.5b
  ↓
Response
```

## Session Commands

| Command | Description |
|---|---|
| `1` | Create a new session |
| `2` | Show all sessions |
| `3` | Show current session |
| `4` | Switch session |
| `break` | Exit chatbot |

## Example

```text
You: my name is Vignesh
Bot: Nice to meet you, Vignesh!

1
Enter a new session_id: user2

You: my name is Kumar
Bot: Nice to meet you, Kumar!

4
Give the session_id to change: user1

You: what is my name?
Bot: Your name is Vignesh.
```

Each session maintains its own conversation history.

## Installation

Install the required packages:

```bash
pip install langchain langchain-core langchain-ollama
```

Make sure **Ollama** is installed and the Llama 3.1 model is available:

```bash
ollama pull qwen2.5:0.5b
```

Run the Python program:

```bash
python chatbot.py
```

## Project Structure

```text
chatbot/
│
├── chatbot.py
└── README.md
```

## Learning Concepts

This project demonstrates:

- LangChain prompts
- Chat message history
- Session management
- `RunnableWithMessageHistory`
- Local LLM integration
- Ollama
- Conversation memory
