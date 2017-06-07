import os
import tkinter as tk
from tkinter import ttk, scrolledtext, Frame, Text, Scrollbar


class App(Frame):
    """docstring for App."""
    def __init__(self, master=None):
        super(App, self).__init__(master)
        self.master = master
        self.s_string = tk.StringVar()

        self.master.title('File Search')
        # self.pack(fill='both', expand='yes')
        self.master.resizable(0, 0)

        # Adding the label
        string_label = ttk.Label(self.master, text='Search String: ')
        string_label.grid(column=0, row=0)
        # string_label.pack(side="top")

        # Adding a textbox
        self.input_data = ttk.Entry(self.master, width=20, textvariable=self.s_string)
        self.input_data.focus()
        self.input_data.grid(column=1, row=0)
        # self.input_data.pack(side="top")

        # Adding a Button
        self.action = ttk.Button(self.master, text="Search", command=self.string_search)
        self.action.grid(column=2, row=0)
        # self.action.pack(side="top")

        # Adding scrolled textbox
        scroll_w = 100
        scroll_h = 15
        self.scr_textbox = scrolledtext.ScrolledText(
            self.master, width=scroll_w, height=scroll_h, wrap=tk.WORD)
        self.scr_textbox.grid(column=0, columnspan=10)

        self.run()

    def run(self):
        self.master.mainloop()

    def string_search(self):
        stg = self.s_string.get().lower()
        results = []

        if stg == '':
            print(stg)
            return

        print('search start')

        for dirname, dirnames, filenames in os.walk('/'):
            for subdirname in dirnames:
                # print(os.path.join(dirname, subdirname))
                path = os.path.join(dirname, subdirname)
                if stg in path.lower():
                    results.append(path)

            for filename in filenames:
                # print(os.path.join(dirname, filename))
                path = os.path.join(dirname, filename)
                if stg in path.lower():
                    results.append(path)

        print('finished searching')
        paths = "\n".join(results) + "\n"

        self.scr_textbox.insert('end', paths)
