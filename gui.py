import tkinter as tk
import random

class App(tk.Tk):
    def __init__(self,columns,rows, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=columns*25, height=rows*25, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = rows
        self.columns = columns
        self.cellwidth = 25
        self.cellheight = 25

        self.rect = {}
        self.oval = {}
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="white", tags="rect")
                # self.oval[row,column] = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill="blue", tags="oval")

        # self.redraw(1000)

    def update(self, row,column,t):
        self.canvas.itemconfig("rect", fill="white")
        x1 = column*self.cellwidth
        y1 = row * self.cellheight
        x2 = x1 + self.cellwidth
        y2 = y1 + self.cellheight
        oval = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill="blue", tags="oval")
        text = self.canvas.create_text(x1/2+x2/2,y1/2+y2/2,text=t)
        self.canvas.itemconfig("oval", fill="blue")
        # for i in range(10):
        #     row = random.randint(0,19)
        #     col = random.randint(0,19)
        #     item_id = self.oval[row,col]
        #     self.canvas.itemconfig(item_id, fill="green")
        # self.after(delay, lambda: self.redraw(delay))

# if __name__ == "__main__":
#     app = App(rows=10,columns=10)
#     app.after(1000,lambda: app.update(1,1))
#     app.mainloop()
