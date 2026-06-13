# Dex Core Neural Network 🧠🚀

Dex is an energetic, high-speed personal assistant bot built on top of a professional Python Flask backend and a highly responsive, feature-rich web dashboard view. It features a self-healing dual-engine image pipeline, real-time user trait extraction, session thread management, and a global circuit breaker fail detector.

---

## 🛠️ New Features (Since Last Release)

### 1. Multi-Threaded Saved Sessions
The interface now supports dynamic contextual threads. Users can instantiate fresh session logs (`+ New Chat`) or jump back into historical interaction contexts directly from the sidebar without polluting current chat memories.

### 2. Live Cognitive Fact Vault
Dex features a dynamic trait extractor. The backend analyzes incoming user statements in real-time, pulling out permanent personal facts (hobbies, equipment models, or family connections) and saving them securely to an adaptive fact panel.

### 3. Native Multi-Modal Attachments
Equipped with a secure media attachment portal (`📎`). Users can feed real physical images straight into Dex's cognitive layer via local base64 encoding strings for high-fidelity scene analysis and detailed visual descriptions.

### 4. Integrated Voice Grid Matrix
Features a dual-channel speech engine:
* **Input Layer (`🎙️`):** Built-in web speech recognition translates live voice commands into text fields automatically.
* **Output Layer (`🔊`):** Optional speech synthesis text stripping vocalizes Dex's message replies aloud.

### 5. Self-Healing Dual AI Image Engine
The image generation framework (`draw [prompt]`) is completely detached from rigid SDK layers to prevent downtime bottlenecks. 
* **Primary Route:** Connects to an unmetered, high-speed real-time generation array.
* **Secondary Route:** If the primary engine returns a rate-limit block (`402 Payment Required`), the script instantly intercepts the response and re-maps the prompt parameters onto a completely independent backup cloud generation node.

### 6. Global Circuit Breaker Pop-Up Detector
A comprehensive safety net wraps the workspace core. If *any* background system fails—whether it is an image timeout, an internet disconnection, or a severe text model endpoint failure—the system completely suppresses broken chat bubbles from appearing on screen and instantly surfaces a clean browser modal:
`Something Went Wrong (404)`

---

## 🏗️ Project Architecture Layout

```text
Dex/
├── app/
│   ├── __init__.py       # App initializations
│   ├── routes.py         # Flask routing layers
│   └── chatbot.py        # Core Engine (Interceptors, Skills, Memory)
├── templates/
│   └── index.html        # Frontend Neural Network Dashboard View
├── run.py                # App main entry execution point
└── README.md             # Project documentation
