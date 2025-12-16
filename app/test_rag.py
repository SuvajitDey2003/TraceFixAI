from app.rag import retrieve_similar_errors


query = "IndexError when accessing list"
results = retrieve_similar_errors(query)

print(results)
