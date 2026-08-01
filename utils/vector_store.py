import os
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

def load_vector_store():
    return Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

def create_vector_store(chunks):
    if os.path.exists("db") and os.listdir("db"):
        print("Loading existing vector database...")
        return load_vector_store()
    
    print("Creating vector database...")
    vector_db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    batch_size = 25
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i+batch_size]
        vector_db.add_documents(batch)
        print(f"Indexed {min(i+batch_size,len(chunks))}/{len(chunks)}")

    return vector_db