from App.app import App
import os


my_app = None

def clear_ui():
    try:
        os.system('clear')
    except:
        pass
    else:
        os.system('cls')

def query_gram():
    clear_ui()
    gram = input("\n")
    pass

def init():
    log_import()
    my_app.run()

def log_import():
    global my_app

    clear_ui()
    file_name = input("Log File:\n")
    max_grams = input("Maximum Gram Size:\n")
    my_app = App(file_name, max_grams)

    print("Log import with success.\nPress any button to return")
    if input():
        menu()

def calc_score():
    clear_ui()
    test_file = input("Enter the test file name:\n")
    pass

def save_data(gram_size):
    



def menu():
    global my_app

    clear_ui()

    print(
    """
    | ** Syscall Analyser ** |

    -> Select an Option:
        1. Import Syscall Log
        2. Consult DataBase
        3. Output n-gram Data
        4. Calculate N-Gram Score
        5. Clear Data
        6. Exit

    """
    )

    opt = input()

    if opt == '1':
        init()
    elif opt == '2':
        query_gram()
    elif opt == '3':
        pass
    elif opt == '4':
        pass
    elif opt == '5':
        pass
    elif opt == '6':
        return
    else:
        menu()
