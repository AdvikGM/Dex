# 🤖 Dex Web Assistant

Dex is a responsive, full-stack personal assistant bot built using Python, Flask, and an interactive frontend interface inspired by Google Gemini. The application features a modular architecture, a programmatic conversational API routing engine, and automated SQLite3 conversation logging.

---

## 🏗️ Project Architecture

The project has been refactored into a modular **Model-View-Controller (MVC)** inspired layout to separate the interface view layer from the backend operational logic layers:

* **View Layer (`templates/index.html`):** Responsive centered UI web interface with dynamic asynchronous data transaction hooks.
* **Sandbox Engine (`dex.py`):** Standalone console bot environment used for rapid script execution and localized testing.
* **Controller Layer (`dex_api.py`):** Holds core configuration maps, intent dictionaries, and conversational data routing logic rules.
* **Application Entrypoint (`run.py`):** Single-point operational trigger used to boot and monitor the local Flask server framework.
* **Model Layer (`site.db`):** Relational database storage engine running background queries to cleanly capture transaction histories.

---

## 🛠️ Features & Command Routing

Dex processes user statements dynamically through an optimized class string matcher. You can interact with the bot using the following standard structural hooks via the central web screen input bar:

* **`Time`** - Returns the localized date and a live, formatted clock time string.
* **`System`** - Displays the engine specifications, current version, and database connection confirmation statuses.
* **`Flip`** - Flips a virtual coin and returns randomized `HEADS!` or `TAILS!` outcomes.
* **`Roll`** - Generates a secure, randomized simulated 6-sided die roll outcome.
* **Greetings (`Hello`, `Hi`, etc.)** - Triggers contextually appropriate answers pulled from a built-in intent data dictionary map.

---

## 🚀 Installation & Local Execution

### 1. Project Directory Access
Open your Windows Command Prompt terminal and migrate straight down into your local programming working workspace path:
```cmd
cd C:\Users\mahesh\Documents\Programming\Dex
