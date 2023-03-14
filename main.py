import cohere
from qdrant_client import QdrantClient
from preprocessor import preprocess_documents, get_document_embeddings, nlp


# Initialize Cohere client
cohere_client = cohere.Client(api_key='9HgYT8dxqVVBTC4iNp9OS8shPD5cbKWgWTZNaTOp')

# Initialize Qdrant client
qdrant_client = QdrantClient(api_key="nNWdYRTYLSdw2PMChu2dlRYC67Ja-77_DGh-kyb8aa5BxuwFVXFP9Q")

# Define index configuration
index_config = {
    "distance": "euclidean",
    "vector_size": 512,
    "index": {
        "type": "hnsw",
        "params": {
            "ef_search": 128
        }
    }
}
index_name = "my_index"

# Preprocess documents
docs = preprocess_documents(directory="samples")

# Get document embeddings
embeddings = get_document_embeddings(docs, cohere_client)

# Create index and add documents
for i, embedding in enumerate(embeddings):
    document_id = docs[i]["id"]
    embedding_dict = {"id": document_id, "vector": embedding}
    qdrant_client.add_documents(index_name=index_name, documents=[embedding_dict])

# Define query
query_text = "This is a sample query"
query_doc = nlp(query_text)
query_tokens = [token.text.lower() for token in query_doc if not token.is_stop and not token.is_punct and not token.like_num]
query_embedding = cohere_client.embed(texts=[" ".join(query_tokens)]).embeddings[0]

# Search for similar documents

# Search for similar documents
search_result = qdrant_client.search(
    collection_name=collection_name,
    search_request={
        "vector": query_embedding,
        "top": 10
    }
)



print(search_result)
