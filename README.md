# Magic_8_Ball
Creating a magic 8 ball on python

With the help of this code, a Magic 8 Ball program, the user can ask a question and get a random response. Three categories—positive, neutral, and negative, are used to categorize the responses. Additional capabilities of the code include seeing, deleting, counting, and searching the archive of earlier questions and responses. The code uses the random and os libraries to handle file operations and choose replies at random. Based on the input from the user, the main loop calls the appropriate functions. A history.txt file keeps track of all the queries and responses.

LINK TO VIDEO:
https://www.youtube.com/watch?v=V38aKqDW3qc&ab_channel=KhaledAbdelhamid


My big breakthrough moment was when I was trying to figure out what library to use and how to use it to be able to store the history and access it with the most integrable techniques. I then discovered it was the history.txt file. 


Lines 14-52 are all examples of data abstraction, used to get different outcomes, such as viewing, searching, and clearing history. It helps to define what those things mean, all while telling the system what to do when those options are picked. 


CODE SEGMENT:
def magic_8_ball():
    question = input("What is your question? ")
    # randomizes choices
    answer_type = random.choice(list(responses.keys()))
    answer = random.choice(responses[answer_type])
    with open("history.txt", "a") as f:
        f.write(f"Question: {question}\nAnswer Type: {answer_type}\nAnswer: {answer}\n")
    print(answer)

This code takes the input from the user and then outputs a random answer from the list of answers given previously. 


 