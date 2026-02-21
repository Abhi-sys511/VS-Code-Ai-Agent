from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
import os

PERSIST_DIR = "./knowledge_db"

embeddings = OllamaEmbeddings(model="llama3")

def load_vectorstore():
    return Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embeddings
    )

def ingest_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = text_splitter.split_documents(documents)

    vectorstore = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=PERSIST_DIR
    )

    vectorstore.persist()

    return f"Indexed {len(docs)} document chunks."

def retrieve_context(query, k=4):
    vectorstore = load_vectorstore()
    results = vectorstore.similarity_search(query, k=k)

    context = "\n\n".join(
        [f"(Source Page {doc.metadata.get('page', 'N/A')})\n{doc.page_content}"
         for doc in results]
    )

    return context, results