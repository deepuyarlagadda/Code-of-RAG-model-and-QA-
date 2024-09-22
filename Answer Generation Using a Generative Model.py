Answer Generation Using a Generative Model
 import cohere

co = cohere.Client('YOUR_API_KEY')

response = co.generate(
    model='large',
    prompt=f"Context: {result['matches'][0]['text']} \n Question: {query}\n Answer:",
    max_tokens=100
)

print(response.generations[0].text)
