# CodeX AI - Intelligent Coding Assistant Chatbot

A ChatGPT-style chat application built with Streamlit and Python, featuring bilingual support (Arabic/English) and intelligent responses for programming-related queries - **without using any external LLM or API**.

## 🌟 Features

- 💬 **Interactive Chat Interface** - ChatGPT-like conversation experience
- 🌐 **Bilingual Support** - Full support for Arabic and English languages
- 📝 **Multi-Conversation Management** - Create, switch between, and manage multiple chat sessions
- 🎨 **Modern UI Design** - Clean, professional interface inspired by ChatGPT
- 🤖 **Smart Local Responses** - Intelligent pattern-matching responses without external APIs
- 💾 **Session State Management** - Conversations persist during the session
- ⚡ **Fast & Lightweight** - No API calls, instant responses

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YasmineSaad79/codex-ai.git
cd codex-ai
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
streamlit run chat_app.py
```

The application will open in your browser at: `http://localhost:8501`

## 📖 How to Use

1. **Select Language** - Choose between Arabic (العربية) or English from the sidebar
2. **Start Chatting** - Type your message in the input box at the bottom
3. **New Conversation** - Click "✏️ New Chat" to start a fresh conversation
4. **Switch Conversations** - Click on any previous conversation in the sidebar to load it
5. **Delete Conversations** - Click the 🗑️ icon next to any conversation to delete it

## 🛠️ Technical Details

### Built With
- **Python** - Core programming language
- **Streamlit** - Web application framework
- **HTML/CSS** - Custom styling for ChatGPT-like interface

### Key Components

#### 1. Session State Management
```python
st.session_state.messages
st.session_state.conversations
```
Stores conversation history and manages multiple chat sessions.

#### 2. Chat Components
- `st.chat_message` - Displays messages in chat format
- `st.chat_input` - Input field for user messages

#### 3. Local Response Generation
```python
def generate_response(user_input: str, lang: str) -> str:
```
Generates intelligent responses using pattern matching - **no external API required**.

### Project Structure
```
codex-ai/
├── chat_app.py          # Main application file
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── DEMO_SCRIPT.md      # Demo presentation script
```

## 💡 Features Explained

### Bilingual Support
The chatbot understands and responds in both Arabic and English:
- Detects language from user input
- Provides contextually appropriate responses
- Maintains language consistency throughout conversations

### Smart Pattern Matching
The response system uses keyword detection to understand queries about:
- Programming languages (Python, Java, JavaScript)
- Learning to code
- Technical problems and debugging
- Web development
- Artificial Intelligence
- Code examples

### Multi-Conversation System
- Create unlimited chat sessions
- Each conversation has a unique title (auto-generated from first message)
- Switch between conversations seamlessly
- Delete conversations individually

## 🎯 Use Cases

- **Learning Programming** - Get guidance on starting your coding journey
- **Language Information** - Learn about different programming languages
- **Technical Assistance** - Get help with coding concepts
- **Code Examples** - View simple code snippets in Python and JavaScript

## 📝 Requirements

See `requirements.txt` for the complete list of dependencies:
- streamlit

## 🔮 Future Enhancements

- [ ] Database integration for persistent storage
- [ ] Integration with external LLM APIs (OpenAI, Claude)
- [ ] File and image upload support
- [ ] Code syntax highlighting
- [ ] Export conversation history
- [ ] User authentication system
- [ ] Response rating system

---

**Note:** This chatbot uses local pattern matching for responses and does not require any external API keys or LLM services. All responses are generated locally using Python functions.
