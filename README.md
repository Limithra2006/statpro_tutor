# 📊 StatProTutor

**StatProTutor** is a smart and student-friendly web app that helps you learn Statistics and Probability with step-by-step solving, visualizations, quizzes, and even an AI tutor! Whether you're a beginner or looking to revise your concepts, StatProTutor is built for you.

---

## 🚀 Features

- 🧮 **Stat Solver**: Solve Mean, Variance, Std Dev, Binomial, Z-Score, T-Test, Chi-Square
- 📊 **Visualizations**: Histogram and Boxplot for data interpretation
- 🧠 **Quiz Mode**: 20+ questions to test your statistics knowledge
- 🤖 **AI Tutor Chatbot**: Ask doubts and get instant answers using OpenAI API
- 🔢 **Live Probability Calculator**
- 🤖 **Mini Machine Learning Playground** – Learn basics of ML
- 📁 **CSV Input Support** and **Download Results**

---

## 🛠️ Built With

- **Python**
- **Streamlit**
- **NumPy**, **Pandas**
- **Matplotlib**, **Seaborn**
- **OpenAI API**
- **ReportLab** (for PDF export)
- **dotenv** (for API key security)

---


## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Limithra2006/statpro_tutor.git
cd statpro_tutor
python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate           # On Windows
pip install -r requirements.txt
streamlit run main.py
statpro_tutor/
├── main.py                        # Main Streamlit app
├── solver.py                      # Core statistical logic
├── explain.py                     # Explanations for results
├── ai_chatbot.py                  # OpenAI chatbot integration
├── stat_solver.py                 # Page logic for Stat Solver
├── ml_playground.py               # Mini ML experiments
├── probability_calculator.py      # Probability computation page
├── requirements.txt               # Python dependencies
├── .env                           # API keys (not pushed)
├── .gitignore                     # Ignore env and cache
└── assets/                        # Optional: banner images, etc.

---

✅ After this:

1. **Paste this into your `README.md` file** inside the repo folder.
2. Commit and push:

```bash
git add README.md
git commit -m "Added professional README"
git push origin main

