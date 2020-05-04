from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tooltips import ToolTips, ToolTipsImage

from PIL import Image, ImageTk

import approximation_functions as af
import functions as f

select_dict = {
    'Exponential Decline': af.exponential_decline,
    'Harmonic Decline': af.harmonic_decline,
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

        width = 580
        height = 450

        w = self.winfo_screenwidth() // 2 - width // 2
        h = self.winfo_screenheight() // 2 - height // 2

        self.geometry('{}x{}+{}+{}'.format(width, height, w, h))
        self.resizable(False, False)

        self.title("Approximation")

        self.iconbitmap('img/icon.ico')

        self.frame2 = Frame()
        self.frame2.pack(side=LEFT, padx=5)

        self.lbox = Listbox(self.frame2, selectmode=SINGLE, width=24, height=24)
        self.lbox.pack(side=TOP)

        for i in select_dict.keys():
            self.lbox.insert(END, i)

        # self.scroll = Scrollbar(command=self.lbox.yview)
        # self.scroll.pack(side=LEFT, fill=Y)
        # self.lbox.config(yscrollcommand=self.scroll.set)
        self.lbox['state'] = 'disabled'

        self.frame1 = Frame()
        self.frame1.pack(side=LEFT, padx=10)

        self.tree = ttk.Treeview(show="headings", selectmode='none', height=400)
        self.tree["columns"] = ("x", "y")
        self.tree.column("x", width=80, minwidth=60, stretch=NO)
        self.tree.column("y", width=80, minwidth=60, stretch=NO)
        self.tree.heading("x", text="x")
        self.tree.heading("y", text="y")
        self.tree.pack(side=LEFT)

        self.name = Label(self.frame1, text='')
        self.name.pack(side=TOP, pady=5)

        self.tree2 = ttk.Treeview(self.frame1, show="headings", selectmode='none', height=9)
        self.tree2["columns"] = ("x", "y")
        self.tree2.column("x", width=60, minwidth=10, stretch=NO)
        self.tree2.column("y", width=160, minwidth=10, stretch=NO)
        self.tree2.pack(side=BOTTOM, pady=10)

        img = Image.open("img/functions/empty.jpg")
        render = ImageTk.PhotoImage(img)
        self.function = Label(self.frame1, image=render, borderwidth=1, relief='solid')
        self.function.image = render
        self.function.pack(side=TOP, pady=5)

        self.b1 = Button(self.frame1, text="Open file", command=self.openFile, width=20)
        self.b1.pack(fill=X)

        self.b2 = Button(self.frame1, text="Run", command=self.run)
        self.b2.pack(fill=X)
        self.b2['state'] = 'disabled'

        self.b3 = Button(self.frame2, text="Search for the best (run all)", command=self.run_all)
        self.b3.pack(side=BOTTOM, fill=X, pady=5)
        self.b3['state'] = 'disabled'

        self.b3tt = ToolTips(self.b3, "It may be a long time")

    def openFile(self):
        file_name = fd.askopenfilename()
        file = open(file_name, 'r')
        data = file.read()

        if data[-1] == '\n':
            data = data[:-1]

        for _ in range(10):
            data = data.replace('  ', ' ')

        data = data.split('\n')

        for k in range(len(data) - 1):
            if data[k][0] == ' ':
                data[k] = data[k][1:]

        try:
            self.mas_x = [float(i.split()[0]) for i in data]
            self.mas_y = [float(i.split()[1]) for i in data]

            if len(self.mas_x) != len(self.mas_y):
                mb.showerror('Error!', 'Data Incorrect!')

            self.lbox['state'] = 'normal'
            self.b2['state'] = 'normal'
            self.b3['state'] = 'normal'

            for i in self.tree.get_children():
                self.tree.delete(i)
            for x, y in zip(self.mas_x, self.mas_y):
                self.tree.insert('', 'end', values=(int(x), y))

        except:
            self.lbox['state'] = 'disabled'
            self.b2['state'] = 'disabled'
            self.b3['state'] = 'normal'

            for i in self.tree.get_children():
                self.tree.delete(i)

            mb.showerror('Error!', 'Data Incorrect!')

        self.lboxtt = ToolTipsImage(self.lbox, select_dict)

    def run(self):
        option = self.lbox.curselection()
        res = select_dict[self.lbox.get(option)](self.mas_x, self.mas_y)

        img = Image.open("img/functions/" + select_dict[self.lbox.get(option)].__name__ + ".jpg")
        render = ImageTk.PhotoImage(img)
        self.function.configure(image=render)
        self.function.image = render

        name = self.lbox.get(option)
        self.name['text'] = name

        mas_z = res.pop('mas_z')

        for i in self.tree2.get_children():
            self.tree2.delete(i)
        for x, y in res.items():
            self.tree2.insert('', 'end', values=(x, y))

        f.draw_chart(self.mas_x, self.mas_y, mas_z, name.lower() + ' approximation')

    def run_all(self):
        res = {}
        for name, func in select_dict.items():
            try:
                res[name] = func(self.mas_x, self.mas_y)
            except:
                pass

        search_name, search_value = '', {'R^2': 0}
        for name, value in res.items():
            try:
                if value['R^2'] > search_value['R^2']:
                    search_name, search_value = name, value
            except:
                pass

        mas_z = search_value.pop('mas_z')

        img = Image.open("img/functions/" + select_dict[search_name].__name__ + ".jpg")
        render = ImageTk.PhotoImage(img)
        self.function.configure(image=render)
        self.function.image = render

        for i in self.tree2.get_children():
            self.tree2.delete(i)
        for x, y in search_value.items():
            self.tree2.insert('', 'end', values=(x, y))

        self.name['text'] = search_name
        f.draw_chart(self.mas_x, self.mas_y, mas_z, search_name.lower() + ' approximation')


def main():
    window = Window()
    window.mainloop()


if __name__ == '__main__':
    main()
