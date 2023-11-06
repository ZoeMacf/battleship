from random import randint
from pprint import pprint

#create a dictionary to convert letters to numbers, allowing user to use Int values to guess ship location
letter_to_number = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

#Uses list comprehension to create a blank list eight times, this can then be populated by the user's guesses and compared to the ship locations
USER_GUESS = [['O'] * 5 for x in range(5)]

#Uses list comprehension to create a blank list eight times, this can then be populated by the ships locations
SHIP_LOCATION = [[''] * 5 for x in range(5)]

user_turn = 0
user_score = 0

def start_screen():
    """Prints welcome screen with ASCII art and menu page"""
    
    print("""
    
                                                                                       
 _|_|_|                _|      _|      _|              _|_|_|  _|        _|            
 _|    _|    _|_|_|  _|_|_|_|_|_|_|_|  _|    _|_|    _|        _|_|_|        _|_|_|    
 _|_|_|    _|    _|    _|      _|      _|  _|_|_|_|    _|_|    _|    _|  _|  _|    _|  
 _|    _|  _|    _|    _|      _|      _|  _|              _|  _|    _|  _|  _|    _|  
 _|_|_|      _|_|_|      _|_|    _|_|  _|    _|_|_|  _|_|_|    _|    _|  _|  _|_|_|    
                                                                             _|        
                                                                             _| 
                                                                             
                                  )___(
                           _______/__/_
                  ___     /===========|   ___
 ____       __   [\\\]___/____________|__[///]   __
 \   \_____[\\]__/___________________________\__[//]___
  \40A                                                 |
   \                                                  /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      
   
""")
    
    print("Welcome to the strategic game of Battleship!\n")
    print("Have you got what it takes to take down your enemy's warships?\n")
    
    print("1. Start Game\n")
    print("2. Rules\n")
    print("3. Exit Game\n")
    
    menu_choice = input("Please choose one of the above, using the numbers 1, 2 or 3\n")
    
    if menu_choice == '1':
        display_game_board(USER_GUESS)
    elif menu_choice == '2':
        display_rules()
    elif menu_choice == '3':
        print('So long captain!..')
        print('Closing game...')
    else:
        print("Please choose something else")

def display_game_board(game_board):
    """
    Generates a game board for the user
    and will then prompt the user to make their first choice
    """
    # Creates a grid for the game_board using join to print row headers and the zip function to pair letters with each row.
    #https://stackoverflow.com/questions/53446425/creating-a-row-of-numbers-letters-in-my-python-battleship-game
    print(" ", " ".join("ABCDE"))
    for letter, row in zip("12345", game_board):
        print(letter, " ".join(row))
        

def display_rules():
    """
    Displays the game rules to user.
    """       
    
    print("Your goal is to try and sink all of your opponents ships before they sink yours\n")
    print("The ships are all different sizes and will be placed around the grid\n")
    print("You must use column and row numbers only to make your guess\n")
    print("If your guess is correct 'HIT' will be displayed to the screen\n")
    print("if not then 'MISS' will be displayed\n")
    
    print("Can you sink all the ships before your opponent?\n")
    
    main_menu = input("Type 'return' to go back to the main menu\n")
    
    if main_menu == 'return':
        start_screen()
    else:
        print("Error: Please type 'return' to go back to the main menu")

def create_battleships(game_board):
    """
    Will create five ships for the game
    """
    # For each of the 5 ships assign a random integer between 1 and 7 to
    # the grid row and column.
    # Add this value to the game_board and assign it 'S'
    for x in range(5):
        battleship_row = randint(0,4)
        battleship_col = randint(0,4)
        game_board[battleship_row][battleship_col] = "S"

def guess_ship_location():
    """
    Allows the user to guess the location of the ships and returns the guess.
    """ 
    global user_turn
    global user_score
    while user_turn < 5:
        row = int(input("Please enter a row number from 1-5\n"))
        col = letter_to_number[input("Please enter a column letter from A-E\n").upper()]
        if SHIP_LOCATION[row][col] == 'S':
            print("HIT")
            SHIP_LOCATION[row][col] = "X"
            user_turn += 1
            user_score += 1
        elif SHIP_LOCATION[row][col] == "X":
            print("Captain, we've already fired there!")
            user_turn += 1
        else: 
            print("Miss!")
            user_turn += 1
            
        

def hit_count():
    """
    Get a count of the ships that have been correctly guessed by the user
    """
    #bypass function for now, placeholder for future function
    pass   
    
    
    
    
def main():
    """
    Run all of the games functions
    """
    start_screen()
        
    create_battleships(SHIP_LOCATION)
    guess_ship_location()
    print(user_score)
    
    
    
main()