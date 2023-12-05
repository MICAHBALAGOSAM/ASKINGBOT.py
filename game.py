#this is still in progress
import colorama

def initialize_colorama():
    colorama.init()

def play_game():
    score = 0
    items = ["dark", "dark chocolate", "milk", "milk chocolate", "white", "white chocolate"]

    start = input("Would you like to play? ")

    if start.lower() == "yes":
        print("STARTING")

    age = int(input("How old are you? "))
    print(f"Wow, you're older than me, you are {age}.")

    def ask_question(question, answer):
        user_answer = input(question)
        if user_answer.lower() == answer:
            print(colorama.Fore.GREEN + "Correct")
            return 1
        else:
            print(colorama.Fore.RED + "Incorrect")
            return -1

    score += ask_question("What's 40 x 2.5: ", "100")
    score += ask_question("What's 5 x 20: ", "100")
    score += ask_question("What's 8 x 12.5: ", "100")
    score += ask_question("What's 25 x 4: ", "100")
    score += ask_question("What's 10 x 10: ", "100")

    number = int(input("Enter a number: "))
    if number >= 0:
        result = 10 * number
        print(f"Your number became this result: {result}")

    chocolate_type = input("Name a type of chocolate: ")
    if chocolate_type.lower() in items:
        print(f"Yes, {chocolate_type.capitalize()} is a type of chocolate.")
        score += 3
        print(f"Your score is {score}")
    else:
        print(f"No, {chocolate_type.capitalize()} is not a type of chocolate.")
        score -= 5
        print(f"Your score is {score}")

    print("------------------------------")
    if score >= 5:
        print("You got a good score on the test!!!!!", score, "/ 5")
    else:
        print("You got a bad score on the test", score, "/ 5")
    print("------------------------------")

if __name__ == "__main__":
    initialize_colorama()
    play_game()
