from App.app import App


my_app = None

def query_gram():
    gram = input("\n")
    pass

def log_import():
    global my_app

    file_name = input("Log File:\n")
    print("\n")
    max_grams = input("Maximum Gram Size:\n")
    my_app = App(file_name, max_grams)

def init():
    log_import()
    my_app.run()

def run_ui():
    print("| ** Syscall Analyser ** |\n")
    print("Select ")    
