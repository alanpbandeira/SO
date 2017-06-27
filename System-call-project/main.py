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
    file_name = "data/" + file_name
    max_grams = int(input("Maximum Gram Size: "))
    my_app = App(file_name, max_grams)

    print("Log imported with success")


def calc_score():
    clear_ui()
    test_file = "data/" + input("Enter the test file name:\n")
    my_app.gram_similarity(test_file)
    print(my_app.scores)
    # print("Similarity Score: ", fo.ngram_score(base_file, test_file))

    print("\nPress any button to return")
    while input() is not "":
        continue
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

    print("Data save with success.\nPress enter to continue.")
    while input() is not "":
        continue
    menu()


def local_ddisplacement():
    """docstring"""
    clear_ui()
    window_size = int(input("Enter window size: "))
    data_file = input("Enter test file name: ")

    data = my_app.score_data_plot(window_size, data_file)

    # TODO
    # Call pyplot and soutput the results.


def menu():
    global my_app

    clear_ui()

    print(
        """| ** Syscall Analyser ** |

        -> Select an Option:
            1. Import Syscall Log
            2. Inport ".strace" File
            3. Consult DataBase
            4. Output N-Gram Data
            5. Calculate N-Gram Score
            6. Clear Data
            7. Exit"""
    )

    opt = input()

    if opt == '1':
        init()
    elif opt == '2':
        reformat()
    elif opt == '3':
        query_gram()
    elif opt == '4':
        save_data()
    elif opt == '5':
        calc_score()
    elif opt == '6':
        my_app = None
        while input() is not "":
            continue
        menu()
    elif opt == '7':
        clear_ui()
        return
    else:
        menu()

menu()
