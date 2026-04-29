from app.rag.vectordb import get_vectorstore
from app.rag.llm import generate_response

def run_rag(query, filters=None):
    db = get_vectorstore()

    docs = db.similarity_search(query, k=5)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer only using the context below:

    {context}

    Question: {query}
    """

    answer = generate_response(prompt)

    sources = [doc.metadata.get("source", "unknown") for doc in docs]

    return {"answer": answer, "sources": sources}