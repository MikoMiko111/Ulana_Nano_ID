from tkinter import*
from tkinter import ttk
import base64
root = Tk()
root.title('Ulana Nano ID')
root.geometry('270x150')
root.resizable(False,False)
idn = ttk.Entry(root,width = 30)
idn.place(x = 50,y = 20)
labelid = ttk.Label(root,text = 'ID :')
labelid.place(x = 20,y = 20)
result = Label(root)
result.place(x = 20,y = 100)
def main():
    global b
    a = idn.get()
    b = base64.b64decode(a)
    result['text'] = b
def create():
    root2 = Tk()
    root2.title('Создать ID...')
    root2.geometry('270x150')
    root2.resizable(False,False)
    idn2 = ttk.Entry(root2,width = 30)
    idn2.place(x = 70,y = 20)
    labelid2 = ttk.Label(root2,text = 'Вход :')
    labelid2.place(x = 20,y = 20)
    result2 = Label(root2)
    result2.place(x = 20,y = 100)
    def encode():
        a2 = idn2.get()
        b2 = base64.b64encode(a2.encode("utf-8"))
        b3 = str(b2, "utf-8")
        result2['text'] = b3
    buta2 = ttk.Button(root2,text = 'Создать ID',command = encode)
    buta2.place(x = 20,y = 50)
    root2.mainloop()

buta = ttk.Button(root,text = 'Сканировать ID',command = main)
buta.place(x = 20,y = 50)
butt = ttk.Button(root,text = 'Создать ID...',command = create)
butt.place(x = 130,y = 50)
root.mainloop()
