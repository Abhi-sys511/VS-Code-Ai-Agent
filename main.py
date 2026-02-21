from langchain_ollama import ChatOllama
from datetime import datetime
import json
import time
import sys
from rag_engine import ingest_pdf, retrieve_context

llm = ChatOllama(model="llama3", temperature=0.5)

def save_to_json(data, filename="research_output.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(data)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, indent=4)

def stream_response(prompt):
    full_response = ""
    for chunk in llm.stream(prompt):
        token = chunk.content
        full_response += token
        sys.stdout.write(token)
        sys.stdout.flush()
    return full_response

def main():
    print("\n🚀 Research Assistant FINAL VERSION")
    print("Features: Multi-PDF RAG + Streaming + Source Citation\n")
    print("Commands:")
    print("  /loadpdf path_to_pdf")
    print("  exit\n")

    while True:
        query = input("Ask something: ")

        if query.lower() == "exit":
            print("Goodbye 👋")
            break

        if query.startswith("/loadpdf "):
            path = query.replace("/loadpdf ", "").strip()
            try:
                result = ingest_pdf(path)
                print(f"\n📚 {result}\n")
            except Exception as e:
                print("❌ Error loading PDF:", e)
            continue

        try:
            print("\n🔎 Retrieving relevant documents...\n")

            context, docs = retrieve_context(query)

            augmented_prompt = f"""
You are an intelligent research assistant.

Use ONLY the provided context to answer.
If answer is not in context, say you don't know.

Context:
{context}

Question:
{query}

Provide a clear answer and mention source page numbers.
"""

            start_time = time.time()

            print("\n📄 Answer:\n")

            answer = stream_response(augmented_prompt)

            end_time = time.time()
            response_time = round(end_time - start_time, 2)

            print(f"\n\n⏱ Response Time: {response_time} seconds")
            print("\n" + "-" * 60 + "\n")

            log_data = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "query": query,
                "response": answer,
                "response_time_seconds": response_time
            }

            save_to_json(log_data)

        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    main()