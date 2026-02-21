📘 AI Research Assistant
Complete Technical Roadmap & Documentation


1️⃣ Project Objective

Build a modular AI Research Assistant in Python that:

Accepts user input

Uses Large Language Models (LLMs)

Generates research-style responses

Saves results automatically to a file

Runs locally without cloud dependency

2️⃣ Development Journey Overview

The project evolved through multiple implementation phases:

Phase	Model Used	Type	Result
Phase 1	OpenAI	Cloud	Required billing
Phase 2	Anthropic	Cloud	Credit limitation
Phase 3	Gemini	Cloud	API configuration issues
Phase 4	Ollama (Llama3)	Local	Fully working

Final Decision:
✔ Use Ollama (Local Llama3) for stability, cost-free usage, and offline capability.

3️⃣ Environment Setup
Python Version

Python 3.10

Virtual Environment Creation
python -m venv venv

Activate:

venv\Scripts\activate
Why Virtual Environment?

Isolates dependencies

Prevents global package conflicts

Makes project reproducible

Clean separation per project

4️⃣ Project Structure
AI Agent Tutorial/
│
├── venv/                    → Virtual environment
├── requirements.txt         → Dependency list
├── main.py                  → Core assistant logic
├── tools.py                 → Tool definitions (earlier phase)
├── research_output.txt      → Auto-generated research log
├── .env                     → API keys (cloud phase)


5️⃣ Dependency Overview

Installed via:

pip install -r requirements.txt

Key packages used during development:

Package	Purpose
langchain	AI orchestration
langchain-openai	OpenAI integration
langchain-anthropic	Claude integration
langchain-community	Search & Wikipedia tools
langchain-ollama	Local Ollama wrapper
python-dotenv	Load environment variables
pydantic	Structured output validation
duckduckgo-search	Web search tool
wikipedia	Wikipedia API
6️⃣ Architecture Evolution
Initial Agent Architecture (Cloud Based)
User Input
   ↓
LangChain Agent
   ↓
Tool Selection
   ↓
External Tool (Search/Wiki)
   ↓
LLM Response

Issues:

Billing requirements

Tool binding compatibility

Version mismatches

Model API limitations

Final Architecture (Local Ollama)
User Input
   ↓
main.py
   ↓
LangChain Ollama Wrapper
   ↓
Ollama Service (Background)
   ↓
Llama3 Model (Local)
   ↓
Response Printed + Saved to File

This architecture removed:

API keys

Billing dependency

Internet requirement

Tool binding issues

7️⃣ Final Working System (Local Version)
main.py Responsibilities

The final main.py:

Initializes local LLM

Accepts user queries

Generates response

Prints result

Saves query + response with timestamp

Handles errors gracefully

8️⃣ Automatic File Saving Feature

This feature replicates what was shown in the YouTube tutorial.

Behavior:

Every query is saved automatically into:

research_output.txt
Saved Format:
==============================
Timestamp: YYYY-MM-DD HH:MM:SS
Query: <User Query>

Response:
<Model Response>
==============================
Purpose:

Maintains research log

Creates persistent history

Enables future data review

Simulates agent save tool behavior

9️⃣ Final Working Code (Core Logic)
from langchain_ollama import ChatOllama
from datetime import datetime

llm = ChatOllama(model="llama3")

def save_to_file(query, response_text, filename="research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_output = (
        f"==============================\n"
        f"Timestamp: {timestamp}\n"
        f"Query: {query}\n\n"
        f"Response:\n{response_text}\n"
        f"==============================\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_output)

def main():
    print("\n🔎 Research Assistant (Local Llama3)\n")

    while True:
        query = input("What can I help you research? (type 'exit' to quit): ")

        if query.lower() == "exit":
            print("Goodbye 👋")
            break

        try:
            response = llm.invoke(query)

            print("\n📄 Result:\n")
            print(response.content)
            print("\n" + "-" * 60 + "\n")

            save_to_file(query, response.content)

        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    main()
🔟 Execution Flow

When running:

python main.py

Process:

Program starts

Waits for user input

User types query

Query sent to Llama3

Response returned

Printed to terminal

Logged into research_output.txt

Loop continues

1️⃣1️⃣ Error Learning Summary

Major error categories encountered:

Dependency Errors

Missing modules

Incorrect versions

API Errors

Authentication failure

Billing not configured

Credit insufficient

Model Errors

Incorrect model name

API version mismatch

Framework Errors

Deprecated functions

Tool binding unsupported

Agent architecture mismatch

Each error strengthened:

Debugging ability

Stack trace reading skill

Version compatibility understanding

LLM provider differences knowledge

1️⃣2️⃣ Key Concepts Learned

This project covered:

Virtual environments

Dependency management

Cloud vs Local LLMs

API key handling

LangChain architecture

Agent-based systems

Tool abstraction

File handling in Python

Error handling with try-except

Timestamp formatting

System architecture design

1️⃣3️⃣ Final System Characteristics

✔ Fully local
✔ No API keys required
✔ No billing required
✔ Offline capability
✔ Auto research logging
✔ Modular architecture
✔ Clean execution loop
✔ Expandable structure

1️⃣4️⃣ Future Improvements (Optional)

Add conversation memory

Save results as JSON

Add search tools again

Convert to web interface

Add GUI using Streamlit

Convert into REST API

Implement structured output validation again

1️⃣5️⃣ Final Summary

This project demonstrates:

End-to-end LLM integration experience

Real-world debugging exposure

Migration from cloud APIs to local models

Architecture refinement process

Tool experimentation and fallback strategy

Implementation of automated logging system

It represents a complete AI system development lifecycle from experimentation to stable production-like setup.
