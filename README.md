faqs = {
    "Why shoud I use this?": "If you use this you will get all the blooks in the game ",
    "How do I use it?": "go to the site and make the options a bookmark and go to blooks in your dashboard and run, You should get all the  blooks.",
}

for i, question in enumerate(faqs, start=1):
    print(f"{i}. {question}")

choice = int(input("\nEnter the number of the question you want to view: "))
question = list(faqs.keys())[choice - 1]
print(f"\n💡 {faqs[question]}")
