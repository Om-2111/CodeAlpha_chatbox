# 🤖 Basic Chatbot with File Logging

## 📌 Overview
This is a **simple rule-based chatbot** created as part of my **CodeAlpha Internship (Task 4)**.  
The chatbot can recognize greetings, farewells, and basic conversations, and it **logs every chat with timestamps** into a file for reference.

---

## 🛠 Features
- Detects greetings (`hi`, `hello`, `hey`, `good morning`, etc.)
- Responds to **"how are you"**
- Recognizes farewells (`bye`, `goodbye`, `see you`)
- Flexible keyword-based detection (no exact match needed)
- **File handling:** Saves all chats with timestamps in `chat_log.txt`
- User-friendly continuous conversation loop

---

## 🧩 Key Concepts Used
- **Dictionary & Keyword Matching**
- **Conditional Statements (`if-elif`)**
- **Loops (`while True`)**
- **Functions**
- **File Handling (optional enhancement)**
- **User Input/Output**

---

## 📂 Files
- `chatbot.py` → The main Python chatbot script
- `chat_log.txt` → Stores all conversation history with timestamps (auto-created when you run the chatbot)

---

## 🚀 How to Run
1. Install **Python 3** on your system.
2. Download the `chatbot.py` file.
3. Open a terminal/command prompt and run:
   ```bash
   python chatbot.py
