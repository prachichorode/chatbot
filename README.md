# chatbot
# 🤖 Rule-Based Chatbot

A simple **Rule-Based Chatbot built using Python**. This chatbot interacts with users through the command line and responds to predefined questions and keywords.

This project is suitable for beginners who are learning **Python, conditional statements, loops, functions, and user input handling**.

## 📌 Features

* 👋 Responds to greetings such as `hello`, `hi`, and `hey`
* 😊 Responds to **"How are you?"**
* 🤖 Tells the user its name
* 🆘 Provides help information
* 🙏 Responds to "thank you"
* 👋 Exits when the user types `bye`, `exit`, or `quit`
* ❓ Provides a default response for unknown inputs
* 💻 Runs directly in the terminal/command prompt

## 🛠️ Technologies Used

* **Python 3**
* `input()`
* `print()`
* `if-elif-else`
* `while` loop
* Functions
* String methods: `.lower()` and `.strip()`

## 📂 Project Structure

```text
rule-based-chatbot/
│
├── chatbot.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rule-based-chatbot.git
```

### 2. Open the Project Folder

```bash
cd rule-based-chatbot
```

### 3. Run the Python Program

```bash
python chatbot.py
```

## 💬 Example

```text
===== RULE-BASED CHATBOT =====

ChatBot: Hello! I am your AI chatbot.
ChatBot: Type 'bye' to exit.

You: hello
ChatBot: Hello! How can I help you?

You: how are you
ChatBot: I am fine. Thanks for asking!

You: what is your name
ChatBot: My name is CODSOFT ChatBot.

You: help
ChatBot: I can answer simple questions about myself.

You: thank you
ChatBot: You're welcome!

You: bye
ChatBot: Goodbye! Have a nice day.
```

## 🧠 How It Works

The chatbot takes input from the user and converts it to lowercase using:

```python
user_input = input("You: ").lower().strip()
```

It then checks the input against predefined conditions.

For example:

```python
if user_input in ["hello", "hi", "hey"]:
    print("ChatBot: Hello! How can I help you?")
```

If the input matches a condition, the chatbot provides the corresponding response.

If no condition matches, it displays:

```text
ChatBot: Sorry, I don't understand that.
```

## 🎯 Learning Objectives

Through this project, you can learn:

* Python functions
* Loops
* Conditional statements
* String handling
* User input
* Basic chatbot logic
* Command-line application development

## 🔮 Future Improvements

The chatbot can be enhanced by adding:

* More questions and responses
* Weather information
* Time and date responses
* Calculator functionality
* Natural Language Processing (NLP)
* Voice input and output
* GUI using Tkinter
* AI-based responses

## 👩‍💻 Author

**Prachi**

## 📄 License

This project is created for **educational and learning purposes**.
