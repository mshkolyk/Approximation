from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
from PIL import Image, ImageTk

import approximation_functions as af

select_list = ['Exponential Decline', 'Harmonic Decline', 'Hyperbolic Decline', 'Bleasdale', 'Farazdaghi-Harris',
               'Reciprocal', 'Reciprocal Quadratic', 'Reciprocal-YD', 'Reciprocal Quadratic-YD',
               'Exponential Plus Linear', 'Logistic', 'Weibull Model', 'Ratkowsky Model', 'MMF', 'Exponential',
               'Modified Exponential', 'Vapor Pressure Model', 'Sinusoidal', 'Rational Model',
               'Steinhart Hart Equation', 'Truncated Fourier Series', 'Polinom 4', 'Polinom 5', 'Polinom 6']

select_dict = {
    'Exponential Decline': af.linear,
    'Harmonic Decline': af.exponential_decline,
    'Hyperbolic Decline': af.hyperbolic_decline,
    'Bleasdale': af.bleasdale,
    'Farazdaghi-Harris': af.farazdaghi_harris,
    'Reciprocal': af.reciprocal,
    'Reciprocal Quadratic': af.reciprocal_quadratic,
    'Reciprocal-YD': af.reciprocal_yd,
    'Reciprocal Quadratic-YD': af.reciprocal_quadratic_yd,
    'Exponential Plus Linear': af.exponential_plus_linear,
    'Logistic': af.logistic,
    'Weibull Model': af.weibull_model,

    'Ratkowsky Model': af.ratkowsky_model,
    'MMF': af.mmf,
    'Exponential': af.exponential,
    'Modified Exponential': af.modified_exponential,
    'Vapor Pressure Model': af.vapor_pressure_model,

    'Sinusoidal': af.sinusoidal,
    'Rational Model': af.rational_model,
    'Steinhart Hart Equation': af.steinhart_hart_equation,
    'Truncated Fourier Series': af.truncated_fourier_series,

    'Polinom 4': af.polinom(4),
    'Polinom 5': af.polinom(5),
    'Polinom 6': af.polinom(6)
}


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.mas_x = []
        self.mas_y = []

        width = 520
        height = 400

        w = self.winfo_screenwidth() // 2 - width // 2
        h = self.winfo_screenheight() // 2 - height // 2

        self.geometry('{}x{}+{}+{}'.format(width, height, w, h))
        self.resizable(False, False)

        self.title("Approximation")
        self.iconbitmap("img/icon2.png")

        self.lbox = Listbox(selectmode=EXTENDED, width=24, height=25)
        self.lbox.pack(side=LEFT)
        for i in select_list:
            self.lbox.insert(END, i)

        self.scroll = Scrollbar(command=self.lbox.yview)
        self.scroll.pack(side=LEFT, fill=Y)
        self.lbox.config(yscrollcommand=self.scroll.set)
        self.lbox['state'] = 'disabled'

        self.frame1 = Frame()
        self.frame1.pack(side=LEFT, padx=20)

        # self.frame2 = Frame()
        # self.frame2.pack(side=RIGHT, padx=10)

        self.tree = ttk.Treeview(show="headings", selectmode='none', height=400)
        self.tree["columns"] = ("x", "y")
        self.tree.column("x", width=80, minwidth=60, stretch=NO)
        self.tree.column("y", width=80, minwidth=60, stretch=NO)
        self.tree.heading("x", text="x")
        self.tree.heading("y", text="y")
        self.tree.pack(side=LEFT)

        # self.entry = Entry(self.frame1)
        # self.entry.pack(anchor=N)

        self.b1 = Button(self.frame1, text="Open file", command=self.openFile, width=20)
        self.b1.pack(fill=X)

        self.b2 = Button(self.frame1, text="Run", command=self.run)
        self.b2.pack(fill=X)
        self.b2['state'] = 'disabled'

        # img = Image.open("img/icon.png")
        # render = ImageTk.PhotoImage(img)
        # self.initil = Label(self.frame2, image=render)
        # self.initil.image = render
        # self.initil.pack()

    def openFile(self):
        file_name = fd.askopenfilename()
        file = open(file_name, 'r')
        data = file.read()

        if data[-1] == '\n':
            data = data[:-1]

        for _ in range(10):
            data = data.replace('  ', ' ')

        data = data.split('\n')

        for k in range(len(data)-1):
            print(data[k])
            if data[k][0] == ' ':
                data[k] = data[k][1:]

        try:
            self.mas_x = [float(i.split()[0]) for i in data]
            self.mas_y = [float(i.split()[1]) for i in data]

            if len(self.mas_x) != len(self.mas_y):
                mb.showerror('Error!', 'Data Incorrect!')

            self.lbox['state'] = 'normal'
            self.b2['state'] = 'normal'

            for i in self.tree.get_children():
                self.tree.delete(i)
            for x, y in zip(self.mas_x, self.mas_y):
                self.tree.insert('', 'end', values=(int(x), y))

        except:
            self.lbox['state'] = 'disabled'
            self.b2['state'] = 'disabled'

            for i in self.tree.get_children():
                self.tree.delete(i)

            mb.showerror('Error!', 'Data Incorrect!')

    def run(self):
        option = self.lbox.curselection()
        select_dict[self.lbox.get(option)](self.mas_x, self.mas_y)


def main():
    window = Window()
    window.mainloop()


if __name__ == '__main__':
    main()
