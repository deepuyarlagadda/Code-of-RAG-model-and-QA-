Storing Embeddings in Pinecone:
    import pinecone

pinecone.init(api_key='YOUR_API_KEY', environment='us-west1-gcp')
index = pinecone.Index("document-qa-bot")

# Store the document embeddings in the index
for idx, embed in enumerate(embeddings):
    index.upsert([(f"id_{idx}", embed)])
