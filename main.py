import cohere
from qdrant_client import QdrantClient

# Initialize Cohere client
cohere_client = cohere.Client(api_key='9HgYT8dxqVVBTC4iNp9OS8shPD5cbKWgWTZNaTOp')

# Initialize Qdrant client
qdrant_client = QdrantClient(api_key="nNWdYRTYLSdw2PMChu2dlRYC67Ja-77_DGh-kyb8aa5BxuwFVXFP9Q", api_url="44e6fb22-9094-444a-9a69-4feaf6eb5b94.us-east-1-0.aws.cloud.qdrant.io")

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

# Create index
qdrant_client.create_index(index_name=index_name, index_config=index_config)

# Embed the document using Cohere
document = "This is a sample document"
embedding = cohere_client.embed(texts=[document])[0]  # Cohere returns a list of embeddings

# Convert the Cohere embedding to the format expected by Qdrant
embedding_dict = {"id": 1, "vector": embedding}

# Add the embedding to the index
qdrant_client.add_documents(index_name=index_name, documents=[embedding_dict])

query_embedding = [0.1, 0.2, ..., 0.5]
search_result = client.search(
    index_name=index_name,
    query={
        "vector": query_embedding,
        "top": 10
    }
)

