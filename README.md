
# 🚀 Smart Prompt Engineering Playground

A simple interactive app to compare and rate different prompt engineering strategies using LLMs.

---

## ✨ Features
- Run multiple prompt strategies on the same input  
- View outputs side-by-side  
- Rate each response (1–5)  
- Instantly update results table  
- Save results for later analysis  

---

## 📸 Screenshots
<img width="1862" height="897" alt="Screenshot from 2026-04-30 14-12-05" src="https://github.com/user-attachments/assets/f52d6199-e8c6-4a45-b743-566733d14ea3" />

<img width="1862" height="897" alt="Screenshot from 2026-04-30 14-12-20" src="https://github.com/user-attachments/assets/e35d18ef-6946-43dc-a848-db8c56bcba74" />




---

## 🧠 Why this project?

Same input → Different prompts → Compare outputs → Rate → Improve

---

## 🛠️ Tech Stack
- Streamlit  
- OpenAI API  
- YAML  
- Pandas  
- python-dotenv  

---

## 📁 Project Structure

smart-prompt-playground/
├── app.py
├── llm.py
├── prompts.yaml
├── requirements.txt
├── .env
├── logs/
└── screenshots/

---

## ⚙️ Setup

```bash
git clone https://github.com/KarunaChandrakapure/Smart-Prompt-Engineering-Playground.git
cd smart-prompt-playground
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:

```
OPENAI_API_KEY=your_api_key_here
```

Run:

```bash
streamlit run app.py
```

---

## 🧪 How it works
1. Enter a message  
2. Run strategies  
3. Compare outputs  
4. Rate them  
5. Save results  

---

## 💾 Storage
Results saved in:

logs/results.csv

---

## 💡 Learnings
- Prompt engineering is iterative  
- Structure improves output quality  
- Evaluation matters  

---

⭐ Star the repo if you found this useful!
