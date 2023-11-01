from random import randint

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
        display_game_board()
    elif menu_choice == '2':
        display_rules()
    else:
        print("Please choose something else")
    
def display_game_board():
    """
    Generates a game board for the user
    and will then prompt the user to make their first choice
    """
    # Creates five instances of game_board and populates the list with 'O' five times to represent spaces for ships.
    for x in range(8):
        game_board.append(['O'] * 8)
    
    # Creates a grid for the game_board using join to print row headers and the zip function to pair letters with each row.
    #https://stackoverflow.com/questions/53446425/creating-a-row-of-numbers-letters-in-my-python-battleship-game
    print(" ", " ".join("12345678"))
    for letter, row in zip("ABCDEFGH", game_board):
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
    
    
    
def main():
    """
    Run all of the games functions
    """
    start_screen()
    
main()