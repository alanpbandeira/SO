from App.app import App
from App import file_operations as fo
import os


my_app = None

def clear_ui():
    try:
        os.system('clear')
    except:
        os.system('cls')

def reformat():
    clear_ui()

    f = input("Enter file name: ")
    fo.reformat_input(f)

    print("\nPress any button to return")
    while input() is not "":
        continue
    menu()

def query_gram():
    clear_ui()

    print("Enter gram:")
    gram = input("\n")

    if my_app.data_search(gram):
        print("Gram sequence found in data_base")
    else:
        print("Gram sequence not found in data_base")

    print("\nPress enter to continue.")
    while input() is not "":
        continue
    menu()

def init():
    log_import()
    my_app.run()

    print("\nPress enter to continue")
    while input() is not "":
        continue
    menu()

def log_import():
    global my_app

    clear_ui()
    file_name = input("Log File: ")
    max_grams = int(input("Maximum Gram Size: "))
    my_app = App(file_name, max_grams)

    print("Log imported with success")

def calc_score():
    clear_ui()
    test_file = input("Enter the test file name:\n")
    my_app.gram_similarity(test_file)
    print("Similarity Score: ", fo.ngram_score(base_file, test_file))

    print("\nPress any button to return")
    if input():
        menu()

def save_data():
    clear_ui()
    gram_size = int(input("Enter gram_size: "))
    idx_file = my_app.descriptor.idx_file
    idx_file = idx_file[:idx_file.rfind('.')]

    grams = []
    for tree in my_app.data_base.values():
        grams += tree.traverse(gram_size-1, my_app.max_gram)

    file_name = idx_file + "_logbase_" + str(gram_size) + ".gram"

    fo.output_gram(file_name, grams)
    # with open(file_name, 'w') as fhand:
    #     for item in grams:
    #         fhand.write(item)

    print("Data save with success.\nPress enter to continue.")
    while input() is not "":
        continue
    menu()

def menu():
    global my_app

    clear_ui()

    print(
    """| ** Syscall Analyser ** |

    -> Select an Option:
        1. Import Syscall Log
        2. Consult DataBase
        3. Output n-gram Data
        4. Calculate N-Gram Score
        5. Clear Data
        6. Inport ".strace" File
        7. Exit
    """
    )

    opt = input()

    if opt == '1':
        init()
    elif opt == '2':
        query_gram()
    elif opt == '3':
        save_data()
    elif opt == '4':
        calc_score()
    elif opt == '5':
        my_app = None
    elif opt == '6':
        reformat()
    elif opt == '7':
        clear_ui()
        return
    else:
        menu()

menu()
