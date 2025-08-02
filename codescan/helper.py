from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import Language


def split_documents(documents, chunk_size=500, chunk_overlap=50     ):
    """
    Split documents into smaller chunks for processing.

    :param documents: List of documents to be split.
    :param chunk_size: Size of each chunk.
    :param chunk_overlap: Overlap between chunks.
    :return: List of text chunks.
    """
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        chunks = text_splitter.split_documents(documents)
        return chunks
    except Exception as e:
        raise RuntimeError(f"Failed to split documents: {e}")

def load_embeddings():
    """
    Load OpenAI embeddings for text processing.

    :return: An instance of OpenAIEmbeddings.
    """
    try:
        embeddings = OpenAIEmbeddings()
        return embeddings
    except Exception as e:
        raise RuntimeError(f"Failed to load embeddings: {e}")