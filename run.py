from pprint import pprint

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
   
""")
    
    print("Welcome to the strategic game of Battleship!\n")
    print("Have you got what it takes to take down your enemy's warships?\n")
    
    print("1. Start Game\n")
    print("2. Rules\n")
    print("3. Exit Game\n")
    
    menu_choice = input("Please choose one of the above, using the numbers 1, 2 or 3\n")
    
    if menu_choice == '1':
        display_game_board()
    else:
        print("Please choose something else")
    
def display_game_board():
    """
    Generates a game board for the user
    and will then prompt the user to make their first choice
    """
    game_board = [
        ['', '', '', '', '',],
        ['', '', '', '', '',],
        ['', '', '', '', '',],
        ['', '', '', '', '',],
        ['', '', '', '', '',]
    ]
    
    pprint(game_board)
        
    
def main():
    """
    Run all of the games functions
    """
    start_screen()
    
main()