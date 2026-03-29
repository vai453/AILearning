import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')
API_KEY = os.getenv("API_KEY_GEMINI") or os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("Set API_KEY_GEMINI or OPENAI_API_KEY in your environment or .env file")

# OpenAI client
client = OpenAI(api_key=API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

# Load FAISS index


# Load chunks



class QueryRAG:
    # Retrieve relevant chunks
    def retrieve(self ,query, k=3):
        index = faiss.read_index("index.faiss")
        with open("chunks.pkl", "rb") as f:
            chunks = pickle.load(f)
        query_embedding = model.encode([query])
        distances, indices = index.search(np.array(query_embedding), k)

        return [chunks[i] for i in indices[0]]

    # Generate answer
    def generate_answer(self,query):
        retrieved_chunks = self.retrieve(query)
        context = "\n\n".join(retrieved_chunks)

        prompt = f"""
        Answer based only on the context below.

        Context:
        {context}

        Question:
        {query}
        """

        response = client.chat.completions.create(
            model="gemini-3-flash-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers based only on the provided context."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content