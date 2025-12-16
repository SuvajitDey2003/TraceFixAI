# 🛠️ TraceFix AI

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-FF4B4B.svg)](https://streamlit.io/)

**TraceFix AI** is an intelligent debugging assistant powered by Generative AI and RAG (Retrieval-Augmented Generation). It analyzes error messages and stack traces, identifies root causes, suggests fixes, and provides prevention strategies using real-world knowledge.

## ✨ Features

- **🔍 Intelligent Error Analysis**: Automatically analyzes error messages and stack traces
- **💡 Context-Aware Solutions**: Uses RAG to retrieve similar past issues for better accuracy
- **🎯 Root Cause Identification**: Pinpoints the exact cause of errors
- **🔧 Actionable Fixes**: Provides clear, step-by-step solutions
- **🛡️ Prevention Strategies**: Suggests best practices to prevent similar issues
- **⚡ Fast & Efficient**: Powered by FAISS for lightning-fast similarity search
- **🌐 REST API**: FastAPI backend for easy integration
- **🖥️ User-Friendly UI**: Clean Streamlit interface for interactive debugging

## 📋 Table of Contents

- [Why TraceFix AI?](#-why-tracefix-ai)
- [How It Works](#-how-it-works)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#-usage)
  - [Running the Application](#running-the-application)
  - [API Usage](#api-usage)
  - [Example](#example)
- [Project Structure](#-project-structure)
- [Technology Stack](#-technology-stack)
- [Contributing](#-contributing)
- [Support](#-support)
- [Maintainers](#-maintainers)

## 🎯 Why TraceFix AI?

Debugging can be time-consuming and frustrating. TraceFix AI helps developers:

- **Save Time**: Get instant analysis instead of searching through documentation
- **Learn Faster**: Understand not just the fix, but why errors occur
- **Prevent Future Issues**: Apply best practices to avoid similar problems
- **Access Knowledge**: Leverage accumulated debugging experience through RAG

## 🔬 How It Works

1. **Error Input**: User submits an error message or stack trace
2. **Embedding**: Error is converted to vector embeddings using Sentence Transformers
3. **Retrieval**: FAISS index finds similar errors from the knowledge base
4. **Context Building**: Retrieved errors provide context with causes, fixes, and prevention
5. **AI Analysis**: Groq LLM analyzes the error with retrieved context
6. **Solution Output**: Returns comprehensive analysis with root cause, fix, and prevention

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Groq API key ([Get one here](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SuvajitDey2003/TraceFixAI.git
   cd TraceFixAI
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv tracefixai-env
   source tracefixai-env/bin/activate  # On Windows: tracefixai-env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Set up your Groq API key**
   
   Create a `.env` file in the project root:
   ```bash
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   ```
   
   Or export it as an environment variable:
   ```bash
   export GROQ_API_KEY=your_groq_api_key_here
   ```

2. **Build the FAISS index** (required on first run)
   ```bash
   python app/embed.py
   ```

## 💻 Usage

### Running the Application

**Option 1: Using the convenience script**
```bash
chmod +x run.sh
./run.sh
```

**Option 2: Manual startup**

Start the FastAPI backend:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

In a new terminal, start the Streamlit UI:
```bash
streamlit run ui/app.py --server.port 7860 --server.address 0.0.0.0
```

Access the application at `http://localhost:7860`

### API Usage

You can also interact with the FastAPI backend directly:

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "error_log": "IndexError: list index out of range"
  }'
```

**Python example:**
```python
import requests

response = requests.post(
    "http://localhost:8000/analyze",
    json={"error_log": "IndexError: list index out of range"}
)

result = response.json()
print(result["analysis"])
```

### Example

**Input:**
```
IndexError: list index out of range
```

**Output:**
The AI will provide:
- **Root Cause**: Explanation of why the error occurred
- **Fix**: Step-by-step solution to resolve the issue
- **Prevention**: Best practices to avoid the error in the future
- **Context**: Similar past issues for reference

## 📁 Project Structure

```
TraceFixAI/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── rag.py           # RAG retrieval logic
│   ├── embed.py         # FAISS index builder
│   ├── prompts.py       # Prompt templates
│   └── test_rag.py      # RAG testing
├── ui/
│   └── app.py           # Streamlit UI
├── data/
│   └── errors/
│       └── errors.json  # Error knowledge base
├── requirements.txt     # Python dependencies
├── run.sh              # Convenience startup script
├── .gitignore
└── README.md
```

## 🛠️ Technology Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
- **Frontend**: [Streamlit](https://streamlit.io/) - Interactive web UI
- **AI Model**: [Groq](https://groq.com/) - Fast LLM inference (llama-3.1-8b-instant)
- **Embeddings**: [Sentence Transformers](https://www.sbert.net/) - all-MiniLM-L6-v2 model
- **Vector Search**: [FAISS](https://github.com/facebookresearch/faiss) - Efficient similarity search
- **HTTP Client**: [Requests](https://requests.readthedocs.io/) - API communication

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**: Implement your feature or bug fix
4. **Test your changes**: Ensure everything works as expected
5. **Commit your changes**: `git commit -m "Add: your feature description"`
6. **Push to your branch**: `git push origin feature/your-feature-name`
7. **Open a Pull Request**: Describe your changes and submit for review

### Ideas for Contributions

- Add more error examples to the knowledge base
- Improve the RAG retrieval algorithm
- Add support for more programming languages
- Enhance the UI with additional features
- Write comprehensive tests
- Improve documentation

## 📚 Support

Need help? Here are your options:

- **Issues**: [GitHub Issues](https://github.com/SuvajitDey2003/TraceFixAI/issues) - Report bugs or request features
- **Discussions**: [GitHub Discussions](https://github.com/SuvajitDey2003/TraceFixAI/discussions) - Ask questions and share ideas
- **Documentation**: Check this README and inline code comments

## 👥 Maintainers

- **Suvajit Dey** - [@SuvajitDey2003](https://github.com/SuvajitDey2003)

---

**Built with ❤️ using FastAPI, FAISS, Groq & Streamlit**

If you find this project helpful, please consider giving it a ⭐!
