from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(vectors):
    job_vector = vectors[-1] # only last vector because JD was at the last 
    resume_vectors = vectors[:-1] # all elements except last becuase others are resumes

    scores = cosine_similarity(resume_vectors, job_vector)

    return scores