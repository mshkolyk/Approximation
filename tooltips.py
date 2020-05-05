import tkinter as tk
from PIL import Image, ImageTk
from images import images
from io import BytesIO


class ToolTips(object):
    def __init__(self, widget, text=''):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, _):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20

        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                         background='white', relief='solid', borderwidth=1,
                         font=("times", "12", "normal"))
        label.pack(ipadx=1)

    def close(self, _):
        if self.tw:
            self.tw.destroy()


class ToolTipsImage(object):
    def __init__(self, widget, select_dict):
        self.widget = widget
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
        self.widget.bind("<<ListboxSelect>>", self.update)

        self.select_dict = select_dict

    def enter(self, _):
        x, y = 0, 0
        x += self.widget.winfo_rootx() + 170
        y += self.widget.winfo_rooty() + 32
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))

        option = self.widget.curselection()
        try:
            # img = Image.open("img/functions/" + self.select_dict[self.widget.get(option)].__name__ + ".jpg")
            img = Image.open(BytesIO(images[self.select_dict[self.widget.get(option)].__name__]))

        except:
            # img = Image.open("img/functions/empty.jpg")
            img = Image.open(BytesIO(images['empty']))

        render = ImageTk.PhotoImage(img)
        self.label = tk.Label(self.tw, image=render, borderwidth=1, relief='solid')
        self.label.image = render

        self.label.pack(ipadx=1)

    def update(self, _):
        option = self.widget.curselection()
        # img = Image.open("img/functions/" + self.select_dict[self.widget.get(option)].__name__ + ".jpg")
        img = Image.open(BytesIO(images[self.select_dict[self.widget.get(option)].__name__]))
        render = ImageTk.PhotoImage(img)
        self.label.configure(image=render)
        self.label.image = render

        self.label.pack(ipadx=1)

    def close(self, _):
        if self.tw:
            self.tw.destroy()
