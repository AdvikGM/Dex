# 🤖 Project Dex: Advanced AI Command Matrix

Welcome to **Project Dex**, a premium, full-stack AI personal assistant web application featuring a sleek, tech-dashboard interface, automated local routing modules, and a cloud-integrated neural network brain.

Designed and engineered by **Advik** (Lead Developer).

---

## 🚀 Key Architectural Features

* **🧠 Gemini 2.5 Flash Brain:** Natively integrated via the official Google GenAI SDK to handle conversational context, complex queries, and intelligent fallbacks.
* **⏱️ Precision Time Sync:** Uses specialized python `zoneinfo` databases (`tzdata`) to enforce accurate India Standard Time (IST) sync across all visual components.
* **📋 Volatile Memory Todo Matrix:** An active, array-backed task engine allowing real-time appending, retrieval, and status tracking via command inputs.
* **🧮 Built-in Expression Compiler:** Uses math standard libraries to securely compute algebraic algorithms and trigonometric expressions right from the input dock.
* **🗄️ SQLite3 Data Logging:** Asynchronously saves every interaction packet to a secure local structured database engine (`site.db`).
* **🚨 Resilient Link Handlers:** Features isolated error view mapping controllers (`templates/errors/404.html`) to cleanly intercept invalid system paths without server failure.

---

## 🎨 Tech Stack & Framework Infrastructure

* **Backend Core:** Python 3 + Flask Web Framework
* **AI Integration:** Google GenAI Library Client
* **Database Engine:** SQLite3 Relational Storage
* **Frontend UI Layout:** Premium Responsive Dark-Mode Glassmorphism Dashboard (HTML5 / Modern Vanilla CSS3 / JavaScript)

---

## 🛠️ Local Installation & Launch Sequence

To clone and run this application cluster locally on your machine, follow these operational commands:

### 1. Initialize Your Environment Keys
Create a `.env` file in the main folder root directory and map your secure access token credentials:
```text
GEMINI_API_KEY=your_actual_private_google_api_key_here
