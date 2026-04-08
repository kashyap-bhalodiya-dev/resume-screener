from sklearn.feature_extraction.text import TfidfVectorizer 


def get_tfidf_vectors(resumes, job_desc):
    documents = resumes + [job_desc] # merging resumes array with job_desc as array so final will be [resume1, resume2, job_desc]

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(documents)

    return vectors