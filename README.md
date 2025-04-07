# Resume Analyzer – Python Project

A beginner-friendly Python script that analyzes your resume PDF and checks how well it matches a set of job-ready skills. Great for freshers and job seekers aiming to improve their resumes!

---

## Features

- Extracts text from PDF resumes
- Scans for relevant tech + soft skills
- Calculates a match score
- Shows matched & missing skills for self-review

---

## Tech Stack

- Python 3
- PyPDF2 (PDF parsing)
- Regular Expressions (`re` module)

---

## Folder Structure

```
Resumeanalyzer/
│
├── resume_analyzer.py       # Main script
├── Shaivisinghresume.pdf    # Your resume file
└── README.md                # This file
```

---

##  How to Use

1. **Install the required package**

```bash
pip install PyPDF2
```

2. **Run the script**

```bash
python resume_analyzer.py
```

3. **When prompted, enter your PDF file name**

```
Enter path to your resume PDF:
Shaivisinghresume.pdf
```

That's it!

---

## Sample Output

```
Resume Analysis Result
Matched Keywords: python, mysql, communication, teamwork
Skill Match Score: 53.33%
Missing Skills: power bi, excel, leadership, data visualization, ...
```

---

## Customization

You can edit the `KEYWORDS` list in the script to match job descriptions or roles you're targeting.

---

## Author

**Shaivi Singh**  
Python Enthusiast | B.Tech in Big Data Analytics  
[LinkedIn](https://www.linkedin.com/in/shaivi-singh)

---

## Support

If you liked this project, feel free to give it a ⭐ on GitHub or share it with someone who's preparing for placements!
