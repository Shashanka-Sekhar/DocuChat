from utils.rag_chain import ask_question

print("=" * 60)
print("DocuChat AI")
print("=" * 60)

while True:
    question = input("\nAsk a question (type 'exit' to quit): ")
    if question.lower() == "exit":
        break
    answer, docs = ask_question(question)
    print("\nAnswer\n")
    print(answer)
    