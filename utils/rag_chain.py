from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from utils.retriever import search_documents

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["context", "question"],

    template="""
You are an AI assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
say:

"I couldn't find this information in the document."

Keep the answer concise.

Context:
{context}

Question:
{question}

Answer:"""
)

def ask_question(question):
    docs = search_documents(question)
    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    response = llm.invoke(final_prompt)
    return response.content, docs