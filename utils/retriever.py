from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

def load_vector_store():
    vector_db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    return vector_db

def search_documents(query, k=3):
    vector_db = load_vector_store()
    retriever = vector_db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10
        }
    )
    results = retriever.invoke(query)
    
    return results