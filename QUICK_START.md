# Quick Start Guide - Job Matching System

## 🎯 What Does This App Do?

This system analyzes your resume and matches you with the best job positions. It uses AI Machine Learning to:
1. Read your PDF resume
2. Extract skills and experience
3. Compare with 10 different job positions
4. Show you the top 3 best matches
5. Tell you which skills you need to learn

---

## ⚡ Quick Steps

### Step 1: Start the Server
Run in PowerShell:
```
cd "c:\Users\bhavan\Desktop\job-matching-system"
.\venv\Scripts\python app.py
```

You should see:
```
Running on http://127.0.0.1:5000
```

### Step 2: Open Your Browser
Go to: **http://127.0.0.1:5000**

### Step 3: Upload a Resume
1. Click the **"Start Now →"** button
2. Click **"Choose PDF File"** or drag and drop a PDF
3. Select your resume (must be PDF format)
4. Click **"🚀 Analyze My Resume"**

### Step 4: View Results
See your job matches with:
- **🏆 Ranking** (1st, 2nd, 3rd best match)
- **📊 Match Score** (0-100% how well you fit)
- **💡 Required Skills** (what the job needs)
- **📚 Skills to Learn** (what you're missing)

---

## 📄 How to Convert Resume to PDF

### From Word/Google Docs:
1. Open your resume
2. Click **File → Download As → PDF**
3. Save the file

### From Text:
1. Open Notepad or Word
2. Paste your resume content here: `SAMPLE_RESUME.txt`
3. Format it nicely
4. Save as **PDF** (File → Export as PDF)

---

## 🧪 Test with Sample Resume

1. Create a PDF from `SAMPLE_RESUME.txt` in this folder
2. Upload it and watch the magic happen!
3. The sample has many skills that match our jobs

---

## 💼 What Jobs Are Available?

1. Data Scientist
2. Web Developer
3. Backend Developer
4. AI Engineer
5. Full Stack Developer
6. DevOps Engineer
7. Mobile Developer
8. Database Administrator
9. Cloud Architect
10. Software Engineer

---

## 🎨 Features

✅ Beautiful modern interface
✅ Automatic PDF text extraction
✅ AI-powered matching algorithm
✅ Shows skills you need to learn
✅ Mobile-friendly design
✅ Smooth animations
✅ Fast processing

---

## ⚙️ Troubleshooting

**Port 5000 already in use?**
```python
# Change port in app.py last line:
app.run(debug=True, port=5001)  # Use 5001 instead
```

**PDF won't upload?**
- Make sure it's a real PDF file
- Check file isn't corrupted
- File size should be reasonable

**No job matches found?**
- Add more keywords to your resume
- Include skill names like: Python, Java, JavaScript, React, etc.
- Be specific about your experience

---

## 📚 Tips for Best Results

Include these in your resume:
- Programming languages (Python, Java, JavaScript, etc.)
- Frameworks (React, Angular, Spring, etc.)
- Tools (Docker, Kubernetes, Git, etc.)
- Databases (PostgreSQL, MongoDB, MySQL, etc.)
- Cloud platforms (AWS, Azure, GCP)
- Soft skills (Leadership, Communication, etc.)

Write naturally - don't just list keywords!

---

## 🚀 Next Steps

1. **Run the app** with the command above
2. **Create a PDF resume** from the sample
3. **Upload and get results!**
4. **Share your matches** with friends

---

**Questions?** Open the README.md file for detailed documentation.

Happy Job Hunting! 🎉
