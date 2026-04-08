from fastapi import FastAPI, UploadFile, File, Form
from typing import List
from utils.preprocess import clean_text
from utils.vectorizer import get_tfidf_vectors
from utils.similarity import compute_similarity
from utils.pdf_parser import extract_text_from_pdf
from utils.embeddings import get_embeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Resume Screening API Running"}

@app.post("/rank")
async def rank_resumes(
    files: List[UploadFile] = File(...),
    job_description: str = Form(...)
):
    resumes = []

    # Step 1: Read PDFs
    for file in files:
        text = extract_text_from_pdf(file.file)
        resumes.append(text)
    
    # Step 2: Clean Text
    resumes_clean = [clean_text(r) for r in resumes]
    job_clean = clean_text(job_description)

    ## Below is the TF-IDF ---- START

    # # Step 3: Vectorize
    # vectors = get_tfidf_vectors(resumes_clean, job_clean)

    # # Step 4: Similarity Check
    # scores = compute_similarity(vectors)

    ## Below is the TF-IDF ---- END

    ## Below is the Embeddings ----- START

    all_texts = resumes_clean + [job_clean]

    embeddings = get_embeddings(all_texts)

    job_vector = embeddings[-1]
    resume_vectors = embeddings[:-1]

    scores = cosine_similarity(resume_vectors, [job_vector])



    ## Below is the Embeddings ----- END


    # Ranking
    ranked = list(enumerate(scores))
    ranked.sort(key=lambda x: x[1], reverse=True)

    result = []
    for i, score in ranked:
        result.append({
            "file_name": files[i].filename,
            "score": round(float(score) * 100, 2)
        })
    
    return {"ranking": result}