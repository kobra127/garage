import csv
from itertools import filterfalse
from tkinter import *
from tkinter import ttk
from xmlrpc.client import FastParser
vybrano=0
t=0
car=[]
window = Tk()
window.title('Гараж с машинами')
window.geometry('1920x650+0+0')
label = ttk.Label()
label.pack(anchor=N, fill=X)
def vydelenie(vybrano):
    vybrano = ""
    for selected_item in tree.selection():
        t = tree.item(selected_item)
        znachenye = t["values"]
        vybrano = f"{vybrano}{znachenye}\n"
    label["text"]=vybrano
def delete():
    b=[]
    h=str(tree.selection())
    symbols = []
    for symbol in h:
        symbols += symbol
    i=0
    for i in symbols:
        if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            b.append(i)
    while b[0]=='0':
        if b[0]=='0':
            b.remove('0')
        elif b[0] == '1' or b[0] == '2' or b[0] == '3' or b[0] == '4' or b[0] == '5' or b[0] == '6' or b[0] == '7' or b[0] == '8' or b[0] == '9':
            break
    j= ' '.join(b)
    j=int(j)
    j=j-1
    car.pop(j)
    with open('cars.txt', 'w', encoding='utf-8') as f:
        pass
    i = len(car)
    with open('kolcars.txt', 'w', encoding='utf-8') as f:
        f.write(str(i))
    for a in range(i):
        b = car.pop(0)
        with open('cars.txt', 'a', encoding='utf-8') as f:
            f.write(str(b))
    for person in car:
        tree.insert("", END, values=person)
print('для удаления, выделите строку. выберите delete и перезапустите программу')
print('для добавления, нажмите add')
print('для сохранения - нажмите save')
with open('cars.txt', 'r', encoding='utf-8') as f:
    with open('kolcars.txt', 'r', encoding='utf-8') as kolcars:
        m = kolcars.read()
    for i in range(0,int(m)):
       s=f.readline()
       car.append(s)
columns=("название","компания","пробег",'фары','коробка передач','цвет')
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
def save():
    with open('cars.txt', 'w', encoding='utf-8') as f:
        pass
    i=len(car)
    with open('kolcars.txt', 'w', encoding='utf-8') as f:
        f.write(str(i))
    for a in range(i):
        b=car.pop(0)
        with open('cars.txt','a',encoding='utf-8') as f:
            f.write(str(b))
def add():
    new_car=[]
    print('название машины')
    g0=str(input())
    print('компания')
    g1=str(input())
    print('пробег в километрах')
    g2=str(input())
    print('Фары:')
    g3=str(input())
    print('коробка передач:')
    g4=str(input())
    print('цвет машины:')
    g5=str(input())
    h=g0+' '+g1+' '+g2+' '+g3+' '+g4+' '+ g5 +'\n'
    new_car.append(h)
    car.append(h)
    for person in new_car:
        tree.insert("", END, values=person)
    return car
main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label="New",command=add)
file_menu.add_command(label="delete",command=delete)
file_menu.add_command(label="save", command=save)
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu)
window.config(menu=main_menu)



def selected(event):
    # получаем выделенный элемент
    selection = combobox.get()
    label["text"] = f"вы выбрали: {selection}"

def sort(col, reverse):
    # получаем все значения столбцов в виде отдельного списка
    l = [(tree.set(k, col), k) for k in tree.get_children("")]
    # сортируем список
    l.sort(reverse=reverse)
    # переупорядочиваем значения в отсортированном порядке
    for index,  (_, k) in enumerate(l):
        tree.move(k, "", index)
    # в следующий раз выполняем сортировку в обратном порядке
    tree.heading(col, command=lambda: sort(col, not reverse))

tree.heading("название", text="название", command=lambda:sort(0,False) )
tree.heading("компания", text="компания", command=lambda:sort(1,False) )
tree.heading("пробег", text="пробег", command=lambda:sort(2,False) )
tree.heading("фары", text='фары', command=lambda:sort(3,False) )
tree.heading('коробка передач', text='коробка передач', command=lambda:sort(4,False) )
tree.heading('цвет',text='цвет', command=lambda:sort(5,False) )

tree.column("#1", stretch=NO, width=320)
tree.column("#2", stretch=NO, width=320)
tree.column("#3", stretch=NO, width=320)
tree.column("#4", stretch=NO, width=320)
tree.column("#5", stretch=NO, width=320)
tree.column("#6", stretch=NO, width=320)

label = ttk.Label()
label.pack(anchor=NW, fill=X, padx=5, pady=5)
for person in car:
    tree.insert("", END, values=person)



tree.bind("<<TreeviewSelect>>", vydelenie)

window.mainloop()