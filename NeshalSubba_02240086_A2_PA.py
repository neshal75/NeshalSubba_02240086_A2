import random
# Guess the Number Game Class
class Guess_number_game:
    def __init__(self):
        self.score = 0
        """the _init_ help to initializes the score to 0 """
    def play_game(self):
        """defining the function called play game """
        print("\nWELCOME TO GUESS THE NUMBER GAME")
        hidden_num = random.randint(1, 10)
        You_have_tried = 0
        while True:
            try:
                guess = int(input("Enter a number between 1 and 10: "))
                You_have_tried += 1
                if guess == hidden_num:
                    print("WOW, Correct guess!")
                    self.score += max(0, 10 - You_have_tried)
                    break
                else:
                    print("Better luck next time")
            except ValueError:
                print("Please enter a valid number!")

"""i have use the while loop and it will run untill it is true and i have used the try
except to find the hidden number and used except if the user have input a invalid number"""



# Rock Paper Scissors Game Class
class Rock_Paper_Scissors_game:
    def __init__(self):
        self.score = 0
        """first creating the class called rock paper scissors game and define the init to use 
        new function and the score is 0"""
    def play_game(self):
        print("\nWELCOME TO ROCK PAPER SCISSORS GAME")
        items = ["rock", "paper", "scissors"]
        """defining the func called play game and a creating a list called item that have
        rock, paper and scissors """
        while True:
            """the while loop continue to run untill the condition is true"""
            user_select = input("Choose rock, paper, or scissors (or type 'exit' to go back): ").lower()
            if user_select == "exit":
                break
            if user_select not in items:
                print("Wrong input, try again.")
                continue
            cpu_select = random.choice(items)
            print("Computer selected:", cpu_select)

            if user_select == cpu_select:
                print("Draw, play again.")
            elif (user_select == "rock" and cpu_select == "scissors") or \
                 (user_select == "paper" and cpu_select == "rock") or \
                 (user_select == "scissors" and cpu_select == "paper"):
                print("WIN! You beat the computer.")
                self.score += 1
            else:
                print("You lose the game.")
"""using if else statement to find out the result of the game where the user can input the item 
and the computer will select the item randomly. at end they will compare the otem to find the winner"""



# Trivia Pursuit Game Class
class TriviaPursuitGame:
    def __init__(self):
        self.score = 0
        """class is created and _init_ is defined where at first the score is zero"""
        self.questions = {
            "Mathematics": [
                ["Calculate 7 + 6 * 4", "b", {"a": "30", "b": "31", "c": "52"}]
            ],
            "Physics": [
                ["Who discovered the electron?", "a", {
                    "a": "Joseph John Thomson", "b": "Ernest Rutherford", "c": "James Chadwick"}]
            ]
        }
    """a category is created where different question is asked to the user and it will return true if the
    user put the correct answer else return false"""
    def play_game(self):
        print("\nTRIVIA PURSUIT GAME")
        for category in self.questions:
            print("\nCategory:", category)
            for question in self.questions[category]:
                print(question[0])
                for key in question[2]:
                    print(f"{key}. {question[2][key]}")
                answer = input("Your answer: ").lower()
                if answer == question[1]:
                    print(" WOW, your Correct!!!")
                    self.score += 1
                else:
                    print(f"Wrong. Correct answer is: {question[1]}")
    """"firstly the function is defined giving the return if the answer is correct else return false """



# Pokemon Binder Manager Class
class card_Binder_Manager:
    def __init__(self):
        self.binder = []
    """creating a class and defing init and creating a empty list where the new cards are added"""
    def manage(self):
        print("\nPOKEMON CARD BINDER MANAGER")
        while True:
            print("\nMain Menu:")
            print("1. Add a card")
            print("2. Reset binder")
            print("3. View cards")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                if len(self.binder) >= 64:
                    print("Binder is full. Max 64 cards allowed.")
                else:
                    card = input("Enter card name: ")
                    self.binder.append(card)
                    print(f"{card} added to binder.")
            elif choice == "2":
                self.binder = []
                print("Binder reset.")
            elif choice == "3":
                if not self.binder:
                    print("Binder is empty.")
                else:
                    for i, card in enumerate(self.binder, start=1):
                        print(f"{i}. {card}")
            elif choice == "4":
                break
            else:
                print("Invalid choice.")
"""firstly showing the main menu to the user and using the if else statement let the user to select the option as mention above"""



#  Control center of all
class Game:
    def __init__(self):
        self.guess_game = Guess_number_game()
        self.rps_game = Rock_Paper_Scissors_game()
        self.trivia_game = TriviaPursuitGame()
        self.binder_manager = card_Binder_Manager()
        """creating the class called game where all the games are mention together"""
    def show_scores(self):
        print("\nTOTAL SCORES:")
        print("Guess Number Game:", self.guess_game.score)
        print("Rock Paper Scissors:", self.rps_game.score)
        print("Trivia Pursuit:", self.trivia_game.score)
        """here it will help to show the score of each game"""
    def main_menu(self):
        while True:
            print("\n MAIN MENU ")
            print("1. Guess the Number")
            print("2. Rock Paper Scissors")
            print("3. Trivia Pursuit")
            print("4. Pokemon Binder")
            print("5. Show Total Scores")
            print("6. Exit")
            """defining the main menu where all the above option are displayed to the user to select"""
    
            choice = input("Select the option from the list: ")
            if choice == "1":
                self.guess_game.play_game()
            elif choice == "2":
                self.rps_game.play_game()
            elif choice == "3":
                self.trivia_game.play_game()
            elif choice == "4":
                self.binder_manager.manage()
            elif choice == "5":
                self.show_scores()
            elif choice == "6":
                print("You are leaving the Game center. bye bye!")
                break
            else:
                print("You have enter the wrong input, read the instruction carefully")


# Run the Program
if __name__ == "__main__":
    control_center = Game()
    control_center.main_menu()
    """firstly it will check if the file is running directly or not then control center
    acces all in the class called game and at end it call the main menu allowing user to select the option in the main menu"""