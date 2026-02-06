# this is mainly setup for openai


from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

load_dotenv()


pdf_path = Path(__file__).parent/"nodejs.pdf"

#Load this file in python program

loader = PyPDFLoader(file_path = pdf_path)
docs = loader.load()

print(docs[12])


# split the docs into smaller chunks


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 400 
)

chunks = text_splitter.split_documents(documents = docs)

# create vector embedding 

embedding_model = OpenAIEmbeddings(
    model = "text-embedding-3-large"
)

vector_store = QdrantVectorStore.from_documents(
    documents = chunks,
    embedding = embedding_model,
    url = "http://localhost:6333/",
    collection_name = "learning_rag"
)

print("Indexing of documents done...") 








# this is mainly setup for using hugging face api 

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

pdf_path = Path(__file__).parent / "nodejs.pdf"

# Load PDF
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()
print(docs[12])

# Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)
chunks = text_splitter.split_documents(docs)

# ⭐ FREE HuggingFace Embeddings (NO API KEY NEEDED)
embedding_model = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"  # FREE embedding model
)

# Store in Qdrant
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333/",
    collection_name="learning_rag"
)

print("Indexing completed using FREE HuggingFace Embeddings...")

