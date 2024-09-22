Query Processing
query = "What is the return policy?"
query_embedding = model.encode([query])
result = index.query(queries=query_embedding, top_k=5)  # Retrieve the top 5 most relevant chunks
