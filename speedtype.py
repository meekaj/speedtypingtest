import time
import random

# Predefined list of sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "All good things come to those who wait.",
    "To be or not to be, that is the question.",
    "A journey of a thousand miles begins with a single step.",
    "You only live once, but if you do it right, once is enough."
    "Please take your dog, Cali, out for a walk - he really needs some exercise!"
    "What a beautiful day it is on the beach, here in beautiful and sunny Hawaii."
    "Rex Quinfrey, a renowned scientist, created plans for an invisibility machine."
    "All the grandfather clocks in that store were set at exactly 3 o'clock."
    "There are so many places to go in Europe for a vacation--Paris, Rome, Prague, etc."
    ""
]

def generate_sentence():
    return random.choice(sentences)

def calculate_typing_metrics(user_input, reference):
    words_input = user_input.split()
    words_reference = reference.split()
    accuracy_count = sum(1 for word in words_input if word in words_reference)
    accuracy = (accuracy_count / len(words_reference)) * 100
    return accuracy

def typing_test():
    sentence = generate_sentence()
    print(sentence)
    print("----------------------------------------")
    print("Press Enter when you are ready to start typing...")
    input()

    start_time = time.time()
    user_input = input("Type the sentence: ")
    end_time = time.time()

    accuracy = calculate_typing_metrics(user_input, sentence)
    time_taken = round(end_time - start_time, 2)
    wpm = round((len(sentence.split()) / time_taken) * 60)

    print("----------------------------------------")
    print("Your accuracy is: {:.2f}%".format(accuracy))
    print("Time taken: {} seconds".format(time_taken))
    print("Your typing speed is: {} words per minute".format(wpm))

    if accuracy < 50 or wpm < 30:
        print("You need to practice typing more!")
    elif accuracy < 80 or wpm < 60:
        print("You are doing great!")
    elif accuracy <= 100 or wpm <= 100:
        print("You are a pro in typing!")
    else:
        print("You are a typing machine!")

def main():
    print("Let's Start")
    while True:
        typing_test()
        if input("Do you want to try again? (y/n): ") != "y":
            break
        print("\n")

if __name__ == "__main__":
    main()