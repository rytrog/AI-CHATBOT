from chat import ask

print("AI is running (type 'exit' to quit) \n")

while True:
    question = input("You: ")

    if question.lower() in ["exit", "quit"]:
        print("👋 Bye bro")
        break

    answer = ask(question)
    print("AI:", answer)
    print()
