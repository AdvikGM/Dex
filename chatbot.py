import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

class DebuggerBrain:
    def __init__(self):
        self.groq_key = os.getenv("GROQ_API_KEY", "").strip().strip("'\"")
        self.openrouter_key = os.getenv("OPENROUTER_API_KEY", "").strip().strip("'\"")
        
        self.system_prompt = (
            "You are an elite multi-language compiler, static analyzer, and code mentor.\n"
            "Analyze the submitted code (supporting Python, JavaScript, TypeScript, C++, Java, C, Go, Rust, HTML/CSS, SQL).\n"
            "Identify syntax errors, logical bugs, edge-case failures, unhandled exceptions, and performance flaws.\n"
            "Respond STRICTLY in valid raw JSON with this exact structure:\n"
            "{\n"
            '  "language": "Detected language (e.g. python, javascript, cpp, java)",\n'
            '  "errors": [\n'
            '    {"line": 12, "issue": "Brief, precise description of the issue"}\n'
            "  ],\n"
            '  "review": "Concise technical diagnosis explaining root cause, logic flow errors, and best practices.",\n'
            '  "fixed_code": "Full corrected, production-ready code with clean syntax"\n'
            "}\n"
            "Do NOT wrap in markdown fences like ```json. Return pure JSON only."
        )

    def analyze_code(self, code_text: str, filename: str = "main.py") -> dict:
        prompt = f"Filename: {filename}\n\nCode to debug:\n{code_text}"
        
        # 1. Groq Engine (Ultra Fast)
        if self.groq_key:
            for model_id in ["llama-3.1-8b-instant", "llama-3.1-70b-versatile", "mixtral-8x7b-32768"]:
                try:
                    res = requests.post(
                        "[https://api.groq.com/openai/v1/chat/completions](https://api.groq.com/openai/v1/chat/completions)",
                        headers={"Authorization": f"Bearer {self.groq_key}", "Content-Type": "application/json"},
                        json={
                            "model": model_id,
                            "messages": [
                                {"role": "system", "content": self.system_prompt},
                                {"role": "user", "content": prompt}
                            ],
                            "temperature": 0.1
                        },
                        timeout=10
                    )
                    if res.status_code == 200:
                        return self._parse_json(res.json()["choices"][0]["message"]["content"], filename)
                except Exception:
                    continue

        # 2. OpenRouter Free Engine
        if self.openrouter_key:
            for model_id in ["meta-llama/llama-3.1-8b-instruct:free", "mistralai/mistral-7b-instruct:free"]:
                try:
                    res = requests.post(
                        "[https://openrouter.ai/api/v1/chat/completions](https://openrouter.ai/api/v1/chat/completions)",
                        headers={"Authorization": f"Bearer {self.openrouter_key}", "Content-Type": "application/json"},
                        json={
                            "model": model_id,
                            "messages": [
                                {"role": "system", "content": self.system_prompt},
                                {"role": "user", "content": prompt}
                            ],
                            "temperature": 0.1
                        },
                        timeout=10
                    )
                    if res.status_code == 200:
                        return self._parse_json(res.json()["choices"][0]["message"]["content"], filename)
                except Exception:
                    continue

        # 3. Emergency Backup Failover
        return {
            "language": "plaintext",
            "errors": [{"line": 1, "issue": "Engine unreachable. Check network connection or API keys."}],
            "review": "Unable to connect to AI debugger endpoint. Ensure valid keys are supplied.",
            "fixed_code": code_text
        }

    def _parse_json(self, raw: str, filename: str) -> dict:
        clean = raw.strip()
        if clean.startswith("```json"): clean = clean[7:]
        if clean.startswith("```"): clean = clean[3:]
        if clean.endswith("```"): clean = clean[:-3]
        try:
            return json.loads(clean.strip())
        except Exception:
            ext = filename.split(".")[-1].lower() if "." in filename else "plaintext"
            return {
                "language": ext,
                "errors": [{"line": 1, "issue": "Code parsed with generic diagnostics."}],
                "review": clean[:400] if clean else "Code reviewed.",
                "fixed_code": clean
            }

brain = DebuggerBrain()