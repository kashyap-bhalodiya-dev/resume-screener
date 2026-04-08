# Resume Screener

## Initial Commit

# 🚀 AI Resume Screening System

An intelligent resume screening system that ranks resumes based on their relevance to a given job description using NLP, embeddings, and vector search.

---

## 📌 Overview

This project simulates a real-world Applicant Tracking System (ATS) by:

- Extracting text from PDF resumes
- Cleaning and preprocessing text data
- Converting text into numerical representations
- Performing similarity matching
- Ranking candidates based on relevance

---

## 🧠 Key Features

- 📄 Upload multiple PDF resumes
- 🔍 Extract and process resume content
- 🧹 Text preprocessing (cleaning + stopword removal)
- 📊 TF-IDF based similarity (baseline model)
- 🤖 Semantic matching using embeddings
- 📈 Ranked output with match percentage

---

## 🏗️ Tech Stack

- **Backend:** FastAPI  
- **NLP:** NLTK, Scikit-learn  
- **Embeddings:** Sentence Transformers  
- **Vector Search:** FAISS  
- **PDF Parsing:** PyPDF2  

---

## ⚙️ How It Works

### Step 1: Resume Input
- Users upload resumes (PDF format)
- Provide job description

---

### Step 2: Text Extraction
- Extract raw text from PDFs using PyPDF2

---

### Step 3: Preprocessing
- Convert to lowercase
- Remove special characters
- Remove stopwords

---

### Step 4: Feature Engineering

#### 🔹 Phase 1: TF-IDF
- Converts text into numerical vectors
- Performs keyword-based matching

#### 🔹 Phase 2: Embeddings
- Uses Sentence Transformers
- Captures semantic meaning of text

---

### Step 6: Ranking

- Retrieve top matching resumes
- Convert distance → similarity score
- Return ranked results

---

## 📊 Example Output

```json
{
  "ranking": [
    {
      "file_name": "resume.pdf",
      "match_percentage": 87.45
    },
    {
      "file_name": "resume_backend.pdf",
      "match_percentage": 62.13
    }
  ]
}