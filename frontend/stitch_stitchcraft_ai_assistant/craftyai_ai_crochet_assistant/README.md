# 🧶 CraftyAI — Multimodal Crochet Assistant

CraftyAI is a multimodal AI-powered crochet assistant that generates personalized crochet patterns from both text prompts and image inputs. The project uses **Gemma 4 E4B** running locally through **LM Studio**, combined with a **FastAPI backend** and a modern interactive frontend UI.

---

# ✨ Features

* 🖼️ Image-based crochet inspiration analysis
* 💬 Text prompt understanding
* 🧠 AI-powered crochet pattern generation
* 🧵 Structured crochet instructions
* 🎨 Yarn color recommendations
* 🪡 Hook size suggestions
* 📋 Difficulty estimation
* 💡 Finishing tips
* ⚡ Fully local inference using LM Studio
* 🔒 No external AI APIs required

---

# 🛠️ Tech Stack

## Frontend

* HTML
* TailwindCSS
* JavaScript

## Backend

* FastAPI
* Python
* Uvicorn

## AI / Inference

* Gemma 4 E4B
* LM Studio
* OpenAI-compatible local API

---

# 📂 Project Structure

```bash
project/
│
├── backend/
│   ├── services/
│   ├── venv/
│   ├── config.py
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   └── code.html
│
└── README.md
```

---

# ⚙️ Setup Instructions

## 1️⃣ Install Python

Download Python:

https://www.python.org/downloads/

Make sure to enable:

```bash
Add Python to PATH
```

during installation.

---

# 2️⃣ Install LM Studio

Download LM Studio:

https://lmstudio.ai/

---

# 3️⃣ Load Gemma 4 E4B Model

Inside LM Studio:

* Search for:

  ```bash
  google/gemma-4-e4b
  ```

* Download the model

* Load the model

---

# 4️⃣ Start LM Studio Local Server

Go to:

```bash
Developer → Local Server
```

Turn server ON.

Expected endpoint:

```bash
http://127.0.0.1:1234/v1
```

---

# 5️⃣ Install Backend Dependencies

Open terminal inside `backend/`

Run:

```bash
pip install -r requirements.txt
```

If requirements file is unavailable:

```bash
pip install fastapi uvicorn python-multipart openai
```

---

# 6️⃣ Run Backend

Inside `backend/`:

```bash
py -m uvicorn main:app --reload
```

Backend will run at:

```bash
http://127.0.0.1:8000
```

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# 7️⃣ Run Frontend

Open:

```bash
frontend/code.html
```

Recommended:

* Use VS Code Live Server extension

---

# 🔄 System Workflow

```text
Frontend UI
    ↓
FastAPI Backend
    ↓
LM Studio Local API
    ↓
Gemma 4 E4B
    ↓
Generated Crochet Pattern
```

---

# 📸 Inputs Supported

* Crochet inspiration images
* Yarn stash photos
* Plushie references
* Text-based project ideas

---

# 📦 Example Output

```json
{
  "project_title": "Beginner Crochet Turtle",
  "materials": [
    "Worsted yarn",
    "5mm hook"
  ],
  "difficulty": "Beginner",
  "crochet_instructions": [
    "Start with a magic ring...",
    "Increase stitches evenly..."
  ]
}
```

---

# 🚀 Future Improvements

* PDF pattern export
* Voice-based crochet assistant
* Pattern saving system
* User accounts
* Crochet diagram generation
* AI stitch visualizer
* Mobile responsiveness improvements

---

# 🧠 AI Model

This project uses:

```bash
google/gemma-4-e4b:2
```

through LM Studio's OpenAI-compatible API.

---

# 👩‍💻 Authors

Built as a multimodal AI crochet assistant project using local inference and modern AI tooling.

---

# 📜 License

This project is for educational and demonstration purposes.
