import cohere
from qdrant_client import QdrantClient


client = cohere.Client(api_key='9HgYT8dxqVVBTC4iNp9OS8shPD5cbKWgWTZNaTOp')

document = "This is a sample document"

embedding = client.embed(texts=[document])
print(f"Embedding for the document '{document}': {embedding} ")

