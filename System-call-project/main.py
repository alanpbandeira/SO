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

def menu():
    global my_app

    clear_ui()

    print(
    """
    | ** Syscall Analyser ** |

    -> Select an Option:
        1. Import Syscall Log
        2. Consult DataBase
        3. Calculate N-Gram Score
        4. Clear Data
        5. Exit

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
    else:
        menu()
