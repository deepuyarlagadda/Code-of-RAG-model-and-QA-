 Embedding Creation:
     from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # This is a lightweight model for creating embeddings
chunks = ["Text chunk 1...", "Text chunk 2...", "Text chunk 3..."]  # Split your document into chunks
embeddings = model.encode(chunks)


     
