# 🎯 Job Matching System

An intelligent AI-powered web application that analyzes your resume and matches you with the most suitable job positions based on your skills and experience.

## ✨ Features

- **Smart Resume Analysis** - Extracts text and analyzes your PDF resume
- **AI-Powered Job Matching** - Uses TF-IDF and cosine similarity for accurate matching
- **Match Scoring** - Get percentage scores showing how well you match each job
- **Skill Gap Analysis** - See which skills you need to learn for each position
- **Beautiful UI** - Modern, responsive design with smooth animations
- **Top 3 Recommendations** - Get your best matching job opportunities

## 🚀 How to Use

### 1. **Start the Application**
```powershell
cd c:\Users\bhavan\Desktop\job-matching-system
.\venv\Scripts\python app.py
```

### 2. **Open in Browser**
- Navigate to: `http://127.0.0.1:5000`
- You should see the home page with a "Start Now" button

### 3. **Upload Your Resume**
- Click "Start Now" or "Upload Resume"
- Upload your PDF resume (must be PDF format)
- Wait for analysis to complete

### 4. **View Your Results**
- See top 3 job matches with:
  - **Match Score**: Percentage of how well you match (0-100%)
  - **Required Skills**: Core competencies needed for the job
  - **Skills to Learn**: Skills you don't have that you should develop
- Click to upload another resume or return to home

## 📊 Available Jobs

The system currently matches against 10 job positions:

1. **Data Scientist** - Python, Machine Learning, Data Analysis, Statistics
2. **Web Developer** - HTML, CSS, JavaScript, React, Node, TypeScript
3. **Backend Developer** - Java, Spring, SQL, PostgreSQL, REST API
4. **AI Engineer** - Python, Deep Learning, NLP, TensorFlow, PyTorch
5. **Full Stack Developer** - JavaScript, React, Node, MongoDB, SQL
6. **DevOps Engineer** - Docker, Kubernetes, Linux, AWS, CI/CD
7. **Mobile Developer** - Swift, Kotlin, React Native, Flutter, Android
8. **Database Administrator** - SQL, PostgreSQL, MySQL, Oracle, Performance Tuning
9. **Cloud Architect** - AWS, Azure, GCP, Kubernetes, Infrastructure
10. **Software Engineer** - Java, Python, C++, Design Patterns, OOP

## 🔧 Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python Flask
- **ML/AI**: Scikit-learn (TF-IDF, Cosine Similarity)
- **Data**: Pandas, NumPy
- **PDF Processing**: pdfminer.six
- **Server**: Flask Development Server

## 📁 Project Structure

```
job-matching-system/
├── app.py                    # Flask application
├── model.py                  # ML model for job matching
├── resume_parser.py          # PDF text extraction
├── dataset.csv              # Job database
├── templates/
│   ├── index.html           # Home page
│   ├── upload.html          # Resume upload page
│   └── result.html          # Results display page
├── uploads/                 # Uploaded resumes storage
└── venv/                    # Python virtual environment
```

## 🎨 How It Works

1. **Resume Upload** → PDF file is saved to `uploads/` folder
2. **Text Extraction** → `resume_parser.py` extracts text from PDF
3. **Analysis** → `model.py` vectorizes resume and job descriptions
4. **Matching** → Uses TF-IDF and cosine similarity to calculate match scores
5. **Results** → Top 3 matches displayed with score and skill gaps
6. **Display** → Beautiful card-based UI shows results

## 💡 Sample Resume Keywords

To get better matching results, include relevant skills in your resume:

**For Data Scientist:**
- Python, Machine Learning, Data Analysis, Statistics, SciPy, Pandas, NumPy

**For Web Developer:**
- HTML, CSS, JavaScript, React, Node, TypeScript, Angular, Vue

**For Backend Developer:**
- Java, Spring, SQL, PostgreSQL, REST API, Microservices

**For AI Engineer:**
- Python, Deep Learning, NLP, TensorFlow, PyTorch, Computer Vision

## 🐛 Troubleshooting

### Port Already in Use
If port 5000 is in use, modify `app.py`:
```python
app.run(debug=True, port=5001)  # Use different port
```

### PDF Upload Fails
- Make sure the file is a valid PDF
- Check `uploads/` folder permissions
- File should be readable and not corrupted

### No Job Matches Found
- Ensure your resume contains relevant skill keywords
- Add technical skills and job titles
- Resume should have enough text content

## 🚀 Future Enhancements

- [ ] More job positions in database
- [ ] Skill level assessment (beginner, intermediate, advanced)
- [ ] Salary range suggestions
- [ ] Learning path recommendations
- [ ] LinkedIn profile integration
- [ ] Real-time job marketplace API
- [ ] User accounts and history
- [ ] PDF resume generation

## 📝 License

Free to use for personal and commercial purposes.

## 👨‍💻 Author

AI Job Matching System - Built with Flask & Machine Learning

---

**Happy Job Hunting! 🎉**
