import os
import tkinter as tk
from tkinter import ttk, scrolledtext, Frame


class App(Frame):
    """docstring for App."""
    def __init__(self, master=None):
        super(App, self).__init__(master)
        self.master = master
        self.s_string = tk.StringVar()
        self.results = []

        # self.master = tk.Tk()
        self.master.title('File Search')

        # Adding the label
        string_label = ttk.Label(self.master, text='Search String: ')
        string_label.grid(column=0, row=0)

        # Adding a textbox
        self.input_data = ttk.Entry(self.master, width=12, textvariable=self.s_string)
        self.input_data.focus()
        self.input_data.grid(column=1, row=0)

        # Adding a Button
        self.action = ttk.Button(self.master, text="Search", command=self.string_search)
        self.action.grid(column=2, row=0)

        # Adding scrolled textbox
        # scroll_w = 30
        # scroll_h = 3
        # self.scr_textbox = scrolledtext.ScrolledText(
        #     self.master, width=scroll_w, height=scroll_h, wrap=tk.WORD)
        # self.scr_textbox.grid(column=0, columnspan=3)

        self.run()

    def run(self):
        self.master.mainloop()

    def string_search(self):
        stg = self.s_string.get().lower()

        if stg == '':
            print(stg)
            return

        print('search start')

        for dirname, dirnames, filenames in os.walk('/'):
            for subdirname in dirnames:
                # print(os.path.join(dirname, subdirname))
                path = os.path.join(dirname, subdirname)
                if stg in path.lower():
                    self.results.append(path)
                    print(self.results)

            for filename in filenames:
                # print(os.path.join(dirname, filename))
                path = os.path.join(dirname, filename)
                if stg in path.lower():
                    self.results.append(path)

        print('finished searching')
        paths = "\n".join(self.results)

        result_label = ttk.Label(self.master, text=paths)
        result_label.grid(column=0, columnspan=3)
