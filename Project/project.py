import random
import os


# Dictionary containing different tones of reply
responses = {
    # different tones have set answers stored in array
    "positive": ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes."],
    "neutral": ["Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again."],
    "negative": ["Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
}


# Function to get a random answer and write the question, answer type and answer to the history.txt file
def magic_8_ball():
    question = input("What is your question? ")
    # randomizes choices
    answer_type = random.choice(list(responses.keys()))
    answer = random.choice(responses[answer_type])
    with open("history.txt", "a") as f:
        f.write(f"Question: {question}\nAnswer Type: {answer_type}\nAnswer: {answer}\n")
    print(answer)


# Function to view the entire history.txt file
def view_history():
    with open("history.txt", "r") as f:
        print(f.read())


# Function to clear the history.txt file by writing an empty string to it
def clear_history():
    with open("history.txt", "w") as f:
        f.write("")
    print("History cleared.")


# Counts the number of lines to figure out how many questions asked
def count_history():
    with open("history.txt", "r") as f:
        lines = f.readlines()
        print(f"Number of questions asked: {len(lines)}")


# Fuction that searches for a specefic input in history
def search_history():
    search_term = input("Enter a search term: ")
    with open("history.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if search_term in line:
                print(line)


# Main loop to handle user input and call the corresponding functions
while True:
    user_input = input("\n Welcome to the Magic 8 Ball App!\nEnter 'ask' to ask a question, 'view' to view the history, 'clear' to clear the history, 'count' to count the number of questions asked, 'search' to search history, or 'exit' to exit the app.\n")
    # if statements setting different modes to the functions
    if user_input.lower() == "ask":
        magic_8_ball()
    elif user_input.lower() == "view":
        if os.path.exists("history.txt") and os.path.getsize("history.txt") > 0:
            view_history()
        else:
            print("No history found.")
    elif user_input.lower() == "clear":
        clear_history()
    # uses functions from os library to help with operations
    elif user_input.lower() == "count":
        if os.path.exists("history.txt") and os.path.getsize("history.txt") > 0:
            count_history()
        else:
            print("No history found.")
    elif user_input.lower() == "search":
        if os.path.exists("history.txt") and os.path.getsize("history.txt") > 0:
            search_history()
        else:
            print("No history found.")
    elif user_input.lower() == "exit":
        break
    else:
        print("Invalid input. Please enter a valid command.")
