from langchain_ollama import ChatOllama
from datetime import datetime

# Initialize Local LLM
llm = ChatOllama(model="llama3")

# Function to save results
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

            # Save to file
            save_to_file(query, response.content)

        except Exception as e:
            print("❌ Error:", e)


if __name__ == "__main__":
    main()