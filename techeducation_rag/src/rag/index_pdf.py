import os
import PyPDF2
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_FILE = "index.faiss"
CHUNKS_FILE = "chunks.pkl"

model = SentenceTransformer('all-MiniLM-L6-v2')
class IndexPDF:
    def load_pdf(self,file_path):
        text = ""
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text

    def chunk_text(self, text, chunk_size=500, overlap=50):
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start += chunk_size - overlap
        return chunks

    def create_index(self , pdf_path):
        print("🔄 Indexing started...")

        text = self.load_pdf(pdf_path)
        chunks = self.chunk_text(text)

        embeddings = model.encode(chunks)

        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(np.array(embeddings))

        faiss.write_index(index, INDEX_FILE)

        with open(CHUNKS_FILE, "wb") as f:
            pickle.dump(chunks, f)

        print("✅ Index created and saved.")