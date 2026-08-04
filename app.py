import streamlit as st

from utils.pdf_reader import extract_text
from utils.text_chunker import chunk_text
from utils.embeddings import create_embeddings, model
from utils.faiss_store import create_faiss_index, search_faiss
from utils.gemini_helper import generate_answer


st.set_page_config(
    page_title="DocuMind AI",
    page_icon="🤖",
    layout="wide"
)

# Session State
if "faiss_index" not in st.session_state:
    st.session_state.faiss_index = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "messages" not in st.session_state:
    st.session_state.messages = []


# Sidebar
with st.sidebar:

    st.title("📚 About")

    st.write("""
DocuMind AI

Features:
✅ PDF Upload
✅ Semantic Search
✅ FAISS Retrieval
✅ Gemini Answers

Built Using:
- Python
- Streamlit
- FAISS
- Sentence Transformers
- Gemini
""")


# Title
st.title("🤖 DocuMind AI")
st.markdown(
    "Upload a PDF and ask questions about its contents."
)


# Upload PDF
pdf_file = st.file_uploader(
    "📄 Upload Document",
    type=["pdf"]
)


# Process PDF only once
if pdf_file and st.session_state.faiss_index is None:

    text = extract_text(pdf_file)

    chunks = chunk_text(
        text,
        chunk_size=500,
        overlap=100
    )

    embeddings = create_embeddings(chunks)

    faiss_index = create_faiss_index(embeddings)

    st.session_state.faiss_index = faiss_index
    st.session_state.chunks = chunks

    st.success("PDF Processed Successfully!")


# Question Input
question = st.text_input(
    "💬 Ask a Question"
)


# Question Answering
if (
    question
    and st.session_state.faiss_index is not None
):

    query_embedding = model.encode(question)

    indices = search_faiss(
        st.session_state.faiss_index,
        query_embedding,
        top_k=5
    )

    retrieved_chunks = []

    for idx in indices:

        retrieved_chunks.append(
            st.session_state.chunks[idx]
        )

    context = "\n".join(retrieved_chunks)

    with st.spinner(
        "Analyzing document..."
    ):

        answer = generate_answer(
            context,
            question
        )

    st.session_state.messages.append(
        {
            "question": question,
            "answer": answer
        }
    )

    st.subheader("🤖 Answer")
    st.success(answer)

    # Uncomment for debugging
    # st.subheader("Retrieved Chunks")
    # for chunk in retrieved_chunks:
    #     st.write(chunk)


# Chat History
if st.session_state.messages:

    st.subheader("💬 Chat History")

    for chat in reversed(
        st.session_state.messages
    ):

        st.markdown(
            f"**You:** {chat['question']}"
        )

        st.markdown(
            f"**DocuMind AI:** {chat['answer']}"
        )

        st.divider()
if st.sidebar.button("🗑️ Clear Chat"):

    st.session_state.messages = []        
if st.sidebar.button("📄 Upload New PDF"):

    st.session_state.faiss_index = None
    st.session_state.chunks = None    