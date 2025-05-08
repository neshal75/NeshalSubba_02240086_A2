class Pokemon_card_binder_manager:
    MAX_POKEDEX = 1025
    CARDS_PER_PAGE = 64
    GRID_ROWS = 8
    GRID_COLUMNS = 8
    """creating the class called pokemon card binder manager and listing the
    class level constants like maximum pokedex equal to 1025 like all  """
    def __init__(self):
        self.binder = {}
    def know_position_cards(self, Number_of_pokedex):
        """defining the function called know the position of the card which have list of pokedex number """
        index = Number_of_pokedex - 1
        Number_of_pages = index // self.CARDS_PER_PAGE + 1
        index_of_pages = index % self.CARDS_PER_PAGE
        row = index_of_pages // self.GRID_COLUMNS + 1
        column = index_of_pages % self.GRID_COLUMNS + 1
        return Number_of_pages, row, column
    """the code help you to calcukate the position of the card"""



    def add_card(self):
        """defining the function and adding the pokemon card to the binder"""
        try:
            Number_of_pokedex = int(input("Please enter your pokedex number: "))
            if not (1 <= Number_of_pokedex <= self.MAX_POKEDEX):
                print(" Your pokedex number is wrong, please enter the number between 1 to 1025.")
                return
            """convert the pokemin number to the integer and the number is not in the required range then come back to main"""

            if Number_of_pokedex in self.binder:
                page, row, column = self.binder[Number_of_pokedex]
                print(f"The number of page is: {page}")
                print(f"location : for row {row}, for column {column}")
                print(f" The status: Pokedex is {Number_of_pokedex} is present in the binder.")
                """if the card is already in the binder then find the location of it """
            else:
                page, row, column = self.know_position_cards(Number_of_pokedex)
                self.binder[Number_of_pokedex] = (page, row, column)
                print(f"The number of page is: {page}")
                print(f"location: for Row {row},for Column {column}")
                print(f"the status: The pokedex is added in {Number_of_pokedex} to the binder")
                """and if it is not their and it a new card then claculate it and find the position of card"""
        except ValueError:
            print("You have inserted wrong input, please put the valid integer to get the result.")
            """if the input is invalid then return saying it a invalid input"""



    def Binder_reset(self):
        print("ALART! All the pokemon cards that you have will be deleted if you reset it.")
        print("Once you reset, you cannot reverse it.")
        """This function will reset all the card in the binder where to do that a certain warning is given as mention above."""
        select_option = input("THINK AGAIN! YOU CAN TYPE 'confirm' TO RESET EVERYTHING OR TYPE 'exit' TO GO BACK TO THE MAIN MENU: ").lower()
        if select_option == "confirm":
            self.binder.clear()  # everything will be cleared in the dictionary
            print(" Whatever the cards you have been, everything is delected, and your binder is reset is confirmed.")
        elif select_option == "exit":
            print("Going back to the main menu.")
        else:
            print("the input you enter is wrong, RETURN TO MAIN MENU.")
            """Using the if else statement we can reset the binder """



    def see_your_binder(self):
        print("Your current binder contents:")
        print("(^_^)===================(^_^)")
        """the above line help you to find the content of the binder """
        if not self.binder:
            print("IT'S EMPTY!, your binder is empty.")
        else:
            for Number_of_pokedex in sorted(self.binder):
                page, row, column = self.binder[Number_of_pokedex]
                print(f"Your pokedex is:{Number_of_pokedex}:")
                print(f"The page: {page}")
                print(f" Location: for row {row}, for Column {column}")
        """The if else statement tell you if the binder is empty and create a loop that show all the location of the save cards"""
        print("<(^-^)>===================<(^-^)>")
        total_cards = len(self.binder)
        Your_percentage = (total_cards / self.MAX_POKEDEX) * 100
        print(f"Total cards present in the binder: {total_cards}")
        print(f"% completion: {Your_percentage:.1f}%")
        if total_cards == self.MAX_POKEDEX:
            print("you got all this only!")




    def exit_program(self):
        print(" THANK YOU! ")
        print(f"TYou have added {len(self.binder)} cards.")
        print("BYE, BYE....!")
        exit()
        """This function help to exit the program """



    def main_menu(self):
        print("\n THIS IS POKEMON CARDS BINDER MANAGER")
        while True:
            print("\n Menu:")
            print("1. If you want to add Pokemon card enter 1")
            print("2. If you want to reset binder enter 2")
            print("3. if you want to view the current placements enter 3")
            print("4. enter 4 to exit the program")
            option = input("Please select the option from the above lists: ").strip()
            if option == "1":
                self.add_card()
            elif option == "2":
                self.Binder_reset()
            elif option == "3":
                self.see_your_binder()
            elif option == "4":
                self.exit_program()
            else:
                print("Please select the option from 1 to 4, you have enter invalid input.")
            """the function display the main menu to the user and user are supposed to select the option given above"""

if __name__ == "__main__":
    manager = Pokemon_card_binder_manager()
    manager.main_menu()
    """This run the program if the file is run directly and imported from other and 
    the other line creates the the object of the class whereby all the function define 
     can be used. The last line call the main menu where manager as object. """