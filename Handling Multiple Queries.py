Handling Multiple Queries
@st.cache
def create_embeddings_for_document(document_text):
    chunks = chunk_document(document_text)
    document_embeddings = create_embeddings(chunks)
    return document_embeddings
