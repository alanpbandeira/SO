import os
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import os

from threading import Thread
from decimal import *
from App.app import App
from App import file_operations as fo


my_app = None
num_plots = 0
getcontext().prec = 2


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


def log_import(file_name=None):
    global my_app

    clear_ui()

    if file_name is None:
        file_name = input("Log File: ")
        file_name = "data/" + file_name
    else:
        file_name = "online_base/" + file_name

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


def local_displacement():
    """docstring"""
    global num_plots

    clear_ui()
    window_size = int(input("Enter window size: "))
    data_file = "data/" + input("Enter test file name: ")
    plot_name = input("Enter plot name: ")
    out_put = "plots/" + plot_name + ".png"

    data = my_app.score_data_plot(window_size, data_file)

    # print(max(list(data.values()))+10)
    with open(out_put, 'w') as fhand:
    # Call pyplot and output the results.
        num_plots += 1
        plt.figure(num_plots)
        plt.plot(list(data.keys()), list(data.values()))
        # plt.ylim(0.0, float(max(list(data.values())))+10)
        # plt.xlim(0.0, max(list(data.keys())))
        # plt.yticks(np.arange(0.0, 101.0, 5))
        plt.xlabel("Window position")
        plt.ylabel("Score (%)")
        plt.title(plot_name)
        plt.savefig(out_put)

    print("Plot save successfully.\nPress enter to continue.")
    while input() is not "":
        continue
    menu()


def app_monitor(pid):
    out_dest = os.getcwd() + "/online_base/output.log"

    try:
        subprocess.run(["strace", "-o", out_dest, "-p", pid])
    except:
        print ("strace not found")



def online_monitoring():
    clear_ui()

    app_name = input("Enter applicaiton name: ")

    try:
        app_pid = str(int(subprocess.check_output(["pidof", app_name])))
    except:
        print("""Invalid applicaiton name.
                Press enter to return to the main menu.""")
        while input() is not "":
            continue
        menu()

    # TODO init monitoring thread
    Thread(target=app_monitor, args=(app_pid))

    while input("Enter 'quit' to exit monitoring mode") != 'quit':
        continue

    # TODO kill monitoring thread
    menu()


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
            6. Plot gram displacement
            7. Online Monitoring
            8. Clear Data
            9. Exit"""
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
        local_displacement()
    elif opt == '7':
        online_monitoring()
    elif opt == '8':
        my_app = None
        while input() is not "":
            continue
        menu()
    elif opt == '9':
        clear_ui()
        return
    else:
        menu()

menu()
