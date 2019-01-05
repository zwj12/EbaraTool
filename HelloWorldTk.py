import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # self.grid(sticky=tk.N + tk.S + tk.E + tk.W)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # top = self.winfo_toplevel()
        # top.rowconfigure(0, weight=1)
        # top.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)
        self.button1 = tk.Button(self, text='button1')
        self.button1.grid(row=1, column=1)
        self.button2 = tk.Button(self, text='button2')
        self.button2.grid(row=2, column=2)
        self.quit = tk.Button(self, text='Quit', command=self.quit)
        self.quit.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)


app = Application()
app.master.title('Sample application')
app.mainloop()
