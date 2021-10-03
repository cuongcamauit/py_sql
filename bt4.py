from sqlite3.dbapi2 import DatabaseError
import tkinter as tk
from tkinter import StringVar, ttk
import sqlite3
def ok(f):
    con = sqlite3.connect('QuanLySinhVien.db')
    cur = con.cursor()
    cur = cur.execute("SELECT * FROM Student" )
    list = cur.fetchall()
    for i in list:
        tree.insert('', tk.END, values=i)



class frame1(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Label(self, text="NHÓM 9", font="20", relief='raised').grid(row=0)
        lst = ("All", "L01", "L02", "L03", "L04", "L05")
        global combox, data
        data = StringVar()
        combox = ttk.Combobox(self, textvariable=data)
        combox['value'] = lst 
        combox['state'] = 'readonly'
        combox.grid(row=1)
        combox.bind('<<ComboboxSelected>>', ok)
class frame2(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        global tree
        colums = ('#1', '#2', '#3', '#4', '#5')
        tree = ttk.Treeview(self, columns=colums, show='headings')
        # define heading
        tree.heading('#1', text="StudentID")
        tree.heading('#2', text="StudentName")
        tree.heading('#3', text="StudentAddress")
        tree.heading('#4', text="PhoneNumber")
        tree.heading('#5', text="ClassID")
        tree.grid(row=0, column=0, sticky='nsew')
        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.config(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')





class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        kk = frame1(self).pack()

        kkk = frame2(self).pack()
ap = App()
ap.mainloop()
