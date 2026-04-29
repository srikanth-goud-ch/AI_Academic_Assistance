from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.vectordb import get_vectorstore

def ingest_pdf(file_path, metadata=None):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    if metadata:
        for chunk in chunks:
            chunk.metadata.update(metadata)

    db = get_vectorstore()
    db.add_documents(chunks)
    db.persist()