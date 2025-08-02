# app.py
import streamlit as st
from codescan.load_index import main as load_index
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import tempfile


st.set_page_config(
    page_title="CodeScan - Source Code Chat",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 CodeScan - Chat with Your Code")
st.markdown("Upload a GitHub repo URL and start asking questions about the source code.")

# --- Sidebar for repo input ---
st.sidebar.header("🔗 Repository Setup")
repo_url = st.sidebar.text_input("Enter GitHub repo URL", placeholder="https://github.com/your/repo")
clone_button = st.sidebar.button("📥 Clone and Analyze")

# --- Display area ---
if clone_button:
    with st.spinner("Cloning and processing the repository..."):
        try:
            # Clone to temp directory
            temp_dir = tempfile.mkdtemp()
            # Load vector store from code
            vectordb = load_index(repo_url,temp_dir)

            # Load OpenAI LLM (Chat)
            llm = ChatOpenAI(temperature=0)
            qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                retriever=vectordb.as_retriever(),
                return_source_documents=True
            )

            st.success("Repository loaded and indexed successfully! You can now ask questions.")
            st.session_state.qa_chain = qa_chain  # Store for chat use

        except Exception as e:
            st.error(f"❌ Failed: {e}")

# --- Chat interface ---
if "qa_chain" in st.session_state:
    st.subheader("💬 Ask Questions About the Codebase")

    query = st.text_input("Type your question...", placeholder="What does the main function do?")
    if query:
        with st.spinner("Thinking..."):
            result = st.session_state.qa_chain(query)
            st.markdown("**🧠 Answer:**")
            st.write(result["result"])

            with st.expander("📄 Source Documents"):
                for doc in result["source_documents"]:
                    st.markdown(f"**File:** `{doc.metadata.get('source', 'unknown')}`")
                    st.code(doc.page_content, language="python")

