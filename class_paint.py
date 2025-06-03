from tkinter import *

class Paint(Frame):
    def __init__(self, parent, x, y):
        Frame.__init__(self, parent)
        self.parent = parent
        self.color = "black"
        self.brush_size = 1
        self.width = 900
        self.height = 600
        self.setUI()
        self.x = x
        self.y = y

    def draw(self, event):
        self.canv.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2,
                              fill=self.color, outline=self.color)

        self.x.append(event.x)
        self.y.append(-event.y)

    def setUI(self):
        self.pack(fill=BOTH, expand=1)
        self.canv = Canvas(self, bg="white", width=self.width, height=self.height)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.canv.grid(padx=1, pady=1, sticky=W+E+N+S)
        self.canv.bind("<B1-Motion>", self.draw)
        
        # Рисуем сетку
        self.draw_grid()

    def draw_grid(self):
        """Рисует координатную сетку на Canvas с разметкой."""
        step = 50  # Шаг сетки
        width = self.width
        height = self.height

        # Вертикальные линии с разметкой
        for i in range(0, width+step, step):
            self.canv.create_line(i, 0, i, height+step, fill="gray", dash=(1, 5))
            if i != width // 2:  # Не рисуем метку для центральной оси Y
                self.canv.create_text(i, height - 10, text=str(i - width // 2), fill="black", font=("Arial", 8))

        # Горизонтальные линии с разметкой
        for i in range(0, height+step, step):
            self.canv.create_line(0, i, width+step, i, fill="gray", dash=(1, 5))
            if i != height - step:  # Не рисуем метку для нижней грани
                self.canv.create_text(10, i, text=str(height // 2 - i), fill="black", font=("Arial", 8), anchor=W)

        # Ось X (горизонтальная линия внизу)
        self.canv.create_line(0, height//2, width+step, height//2, fill="black", width=2)

        # Ось Y (вертикальная линия по центру)
        self.canv.create_line(width // 2, 0, width // 2, height, fill="black", width=2)
