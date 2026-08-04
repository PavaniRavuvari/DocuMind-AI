# 🤖 DocuMind AI – RAG-Based PDF Question Answering System

DocuMind AI is an intelligent **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions in natural language. The system retrieves the most relevant information from the uploaded document using semantic search and generates context-aware answers with Google's Gemini LLM.

---

## 🚀 Features

- 📄 Upload any PDF document
- 💬 Ask questions in natural language
- 🔍 Semantic search using Sentence Transformers
- 📚 FAISS Vector Database for efficient similarity search
- 🤖 Google Gemini for context-aware answer generation
- 📝 Chat history support
- ⚡ Session state management for faster interactions
- 🎨 Interactive Streamlit interface
- 🛡️ User-friendly error handling

---

## 🏗️ Project Architecture

```
                PDF Document
                     │
                     ▼
            Text Extraction (PyPDF2)
                     │
                     ▼
               Text Chunking
                     │
                     ▼
      Sentence Transformer Embeddings
                     │
                     ▼
             FAISS Vector Database
                     │
          User Question (Query)
                     │
                     ▼
        Query Embedding Generation
                     │
                     ▼
      Semantic Similarity Search (Top-K)
                     │
                     ▼
        Retrieved Relevant Chunks
                     │
                     ▼
      Prompt Augmentation (RAG)
                     │
                     ▼
      Google Gemini LLM
                     │
                     ▼
            Context-Aware Answer
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| Sentence Transformers | Text Embeddings |
| FAISS | Vector Database |
| Google Gemini API | Large Language Model |
| PyPDF2 | PDF Text Extraction |
| NumPy | Numerical Computation |
| python-dotenv | Environment Variable Management |

---

## 📂 Project Structure

```
documind-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
└── utils/
    ├── pdf_reader.py
    ├── text_chunker.py
    ├── embeddings.py
    ├── faiss_store.py
    └── gemini_helper.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/documind-ai.git

cd documind-ai
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure API Key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

### Run Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Home Page

*(Add screenshot here)*

---

### Asking Questions

*(Add screenshot here)*

---

### Chat History

*(Add screenshot here)*

---

## 🧠 How It Works

1. User uploads a PDF.
2. Text is extracted from the document.
3. The extracted text is split into smaller chunks.
4. Sentence Transformers convert each chunk into vector embeddings.
5. FAISS stores the embeddings for efficient retrieval.
6. User enters a question.
7. The question is converted into an embedding.
8. FAISS retrieves the Top-K most relevant chunks.
9. Retrieved chunks are combined with the user's question.
10. Gemini generates a context-aware answer.

---

## 📌 Example

**Question**

```
What is Pavani's phone number?
```

**Answer**

```
8978907023
```

---

## 🌟 Future Improvements

- OCR support for scanned PDFs
- Multiple PDF support
- Source citation with page numbers
- Chat memory
- Voice-based interaction
- LangChain integration
- LangGraph agent workflow
- ChromaDB support
- Docker deployment
- Cloud deployment

---

## 🎯 Learning Outcomes

This project demonstrates practical understanding of:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- FAISS Indexing
- Large Language Model Integration
- Prompt Augmentation
- Streamlit Development
- API Integration

---

## 👩‍💻 Author

**Pavani Ravuvari**

GitHub: https://github.com/PavaniRavuvari

LinkedIn: https://linkedin.com/in/pavani-ravuvari/

---

## 📜 License

This project is licensed under the MIT License.
