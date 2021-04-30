import tkinter as tk
from PIL import Image, ImageTk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

    def create_hello_frame(self):
        self.pack()
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self,
                              text="QUIT",
                              fg="red",
                              bg="black",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def create_sample_frame(self):
        self.grid()

        self.button = tk.Button(self)
        self.button["text"] = "demo"
        self.button.grid(row=0,
                         column=0,
                         sticky=tk.N + tk.W,
                         padx=5)

        self.check_value = tk.BooleanVar()
        self.check_value.set(False)
        self.check_button = tk.Checkbutton(self, var=self.check_value)
        self.check_button["text"] = "demo"
        self.check_button["command"] = self.say_hi
        self.check_button.grid(row=1,
                               column=0,
                               sticky=tk.N + tk.W,
                               padx=5)

        self.entry = tk.Entry(self)
        self.entry.grid(row=2,
                        column=0,
                        sticky=tk.N + tk.W,
                        padx=5)

        self.label = tk.Label(self)
        self.label["text"] = "demo"
        self.label.grid(row=3,
                        column=0,
                        sticky=tk.N + tk.W,
                        padx=5)

        self.languages = tk.Listbox(self)
        languages = ('Python', 'Java', 'C', 'JavaScript', 'Golang', 'Scala')
        self.languages["height"] = len(languages)
        [self.languages.insert(i+1, x) for i, x in enumerate(languages)]
        self.languages.grid(row=4,
                            column=0,
                            sticky=tk.N + tk.W,
                            padx=5)

        self.options = ("Python", "Java", "Swift")
        self.choice = tk.StringVar()
        self.choice.set("Python")
        self.option_menu = tk.OptionMenu(self, self.choice, *self.options)
        self.option_menu.grid(row=5,
                              column=0,
                              sticky=tk.N + tk.W,
                              padx=5)

        self.radio_button = tk.Radiobutton(self)
        self.radio_button["text"] = "demo"
        self.radio_button.grid(row=6,
                               column=0,
                               sticky=tk.N + tk.W,
                               padx=5)

        self.scale = tk.Scale(self)
        self.scale.grid(row=7,
                        column=0,
                        sticky=tk.N + tk.W,
                        padx=5)

        self.spin_box = tk.Spinbox(self,
                                   from_=0,
                                   to=10)
        self.spin_box.grid(row=8,
                           column=0,
                           sticky=tk.N + tk.W,
                           padx=5)

        self.text = tk.Text(self,
                            height=10,
                            width=50)
        self.text.grid(row=9,
                       column=0,
                       sticky=tk.N + tk.W,
                       padx=5)

        self.quit = tk.Button(self,
                              text="QUIT",
                              fg="red",
                              bg="black",
                              command=self.master.destroy)
        self.quit.grid(row=10,
                       column=0,
                       sticky=tk.N + tk.W,
                       padx=5)

    def say_hi(self):
        print("hi there, everyone!")
        print(self.check_value.get())


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.create_sample_frame()
    app.mainloop()

