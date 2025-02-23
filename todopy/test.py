import tkinter as tk
from tkinter import ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.frame = ttk.Frame(canvas)
        self.frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        window = canvas.create_window((0, 0), window=self.frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

root = tk.Tk()
frame = ScrollableFrame(root)
frame.pack(fill="both", expand=False)
#frame.place(width= 300,height=300)
for i in range(10):
    box = ttk.Frame(frame.frame, relief="ridge", borderwidth=2 , width=300 , height= 50)
    box.pack(fill="x", padx=5, pady=2)
    ttk.Label(box, text=f"Option {i+1}").pack(side="left", padx=5)
    ttk.Checkbutton(box).pack(side="right", padx=5)

root.mainloop()

