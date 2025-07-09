from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import os

# Azure OpenAI configuration
AZURE_OPENAI_ENDPOINT = "https://rag-ai-sweden.openai.azure.com/"
AZURE_OPENAI_API_KEY = "qL8wZ40p6FM9oPjJWXNPhUmOY2VsaKaentxqD6yCgMjzc9hWvAYuJQQJ99BGACfhMk5XJ3w3AAABACOGUhWp"  # Paste Key from llm-model
AZURE_DEPLOYMENT_NAME = "llm-model"

# Azure Cognitive Search configuration
COGNITIVE_SEARCH_NAME = "rag-searchsweden"
COGNITIVE_SEARCH_KEY = "dlZCTx1vaUtG7MNaIMhCnhCh9oB7qZAFJLh1AI4M6sAzSeBQINzJ"  # Paste Admin Key from Cognitive Search Keys tab
COGNITIVE_SEARCH_ENDPOINT = "https://rag-searchsweden.search.windows.net"
INDEX_NAME = "azure-rag-demo-index"

# Load PDF and split
loader = PyPDFLoader("demo_paper.pdf")
pages = loader.load_and_split()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(pages)

# Initialize Cognitive Search client
credential = AzureKeyCredential(COGNITIVE_SEARCH_KEY)
client = SearchClient(endpoint=COGNITIVE_SEARCH_ENDPOINT, index_name=INDEX_NAME, credential=credential)

# Upload PDF chunks
for i, chunk in enumerate(chunks):
    document = {"id": str(i), "data": chunk.page_content}
    result = client.upload_documents(documents=[document])
    print(f"Uploaded chunk {i + 1}: {result}")

# Initialize LLm
AZURE_OPENAI_DEPLOYMENT = "llm-model"
llm = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version="2023-03-15-preview",
    deployment_name=AZURE_OPENAI_DEPLOYMENT,
    api_key=AZURE_OPENAI_API_KEY,
    temperature=0
)

def generate_response(question):
    # Limit search results to top 3 documents
    search_results = client.search(question, top=3)

    # Combine only top N documents and truncate
    context = "\n".join([doc["data"][:1500] for doc in search_results])

    # Build prompt with reduced context size
    prompt = f"Answer the question based on the context below.\n\nContext:\n{context}\n\nQuestion:\n{question}"

    # Set max_tokens to a safe value
    response = llm.invoke(prompt, max_tokens=512)

    return response

# Example user query
user_question = "How does domain adaptation work in deep learning?"
answer = generate_response(user_question)
print("💡 Answer:", answer)
