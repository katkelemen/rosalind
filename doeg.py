# -*- coding: utf-8 -*-
from Tkinter import Tk, Frame, BOTH


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="pink")   
         
        self.parent = parent
        
        self.initUI()
    
    def initUI(self):
      
        self.parent.title("Rosebud")
        self.pack(fill=BOTH, expand=1)
        

def main():
  
    root = Tk()
    root.geometry("500x400+300+100")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  