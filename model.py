from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import re

def predict_jobs(resume_text):
    """
    Analyze resume and find matching job positions
    Returns top 3 job matches with scores and missing skills
    """
    data = pd.read_csv("dataset.csv")
    
    # Convert to lowercase and clean text
    resume_clean = re.sub(r'[^a-z\s]', '', resume_text.lower())
    
    job_roles = data["Job Role"].tolist()
    job_skills = data["Skills"].tolist()
    
    # Improved TF-IDF Vectorization
    vectorizer = TfidfVectorizer(
        analyzer='word',
        ngram_range=(1, 2),
        stop_words='english',
        max_features=100
    )
    
    # Fit and transform job skills + resume
    all_texts = [skill.lower() for skill in job_skills] + [resume_clean]
    vectors = vectorizer.fit_transform(all_texts)
    
    # Calculate similarity scores
    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    scores = similarity[0]
    
    # Create results with job info
    results = list(zip(job_roles, scores, job_skills))
    results.sort(key=lambda x: x[1], reverse=True)
    
    # Process top 3 jobs
    top_jobs = []
    
    for job, score, skills in results[:3]:
        # Extract skills from both resume and job requirements
        required_skills = set(skill.strip().lower() for skill in skills.split() if len(skill.strip()) > 2)
        resume_skills = set(word.lower() for word in resume_clean.split() if len(word) > 2)
        
        # Find missing skills
        missing = list(required_skills - resume_skills)
        
        # Calculate match percentage (normalized 0-100)
        match_percentage = min(round(score * 100, 1), 100)
        
        top_jobs.append({
            "job": job,
            "score": match_percentage,
            "missing": missing[:5],  # Show top 5 missing skills
            "required_skills": list(required_skills)[:8]  # Show required skills
        })
    
    return top_jobs