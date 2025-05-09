from bibliotecas import *
from tkinter import Entry


class EntPlaceHold(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color="#ad7628"):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind('<FocusIn>', self.foc_in)
        self.bind('<FocusOut>', self.foc_out)

        self.put_placeholder()


    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    
    def foc_in(self):
        if self['fg'] == self.placeholder_color:
            self.delete(0, 'end')
            self['fg'] = self.default_fg_color
        
    
    def foc_out(self):
        if not self.get():
            self.put_placeholder()