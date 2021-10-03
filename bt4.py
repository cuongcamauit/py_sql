from sqlite3.dbapi2 import DatabaseError
import tkinter as tk
from tkinter import Button, Entry, Label, Message, StringVar, ttk
from tkinter import messagebox
import sqlite3
# return a list from sql statement
def returnlist(s):
    con = sqlite3.connect('QuanLySinhVien.db')
    cur = con.cursor()
    cur = cur.execute(s)
    return cur.fetchall()
# commit sql
def commitsql(s):
    con = sqlite3.connect('QuanLySinhVien.db')
    cur = con.cursor()
    try:
        cur = cur.execute(s)
        con.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Error",e)
# create a string
def chuoi(id, name, address, phone, clas):
    s = ""
    if (id!=""):
        s = s + " StudentID='%s'" %(id)
    if (name!=""):
        if (s!=""):
            s = s + " AND StudentName='%s'" %(name)
        else:
            s = s + " StudentName='%s'" %name
    if (address!=""):
        if (s!=""):
            s = s + " AND StudentAddress='%s'" %(address)
        else:
            s = s + " StudentAddress='%s'" %(address)
    if (phone!=""):
        if (s!=""):
            s = s + " AND PhoneNumber='%s'" %(phone)
        else:
            s = s + " PhoneNumber='%s'" %(phone)
    if (clas!=""):
        if (s!=""):
            s = s + " AND ClassID='%s'" %(clas)
        else:
            s = s + " ClassID='%s'" %(clas)
    return s
def settree(list):
    for i in tree.get_children():
        tree.delete(i)
    for i in list:
        tree.insert('',tk.END,values=i)
def ok(f):
    s = "SELECT * FROM Student "
    if (data.get()!='All'):
        s = s + "WHERE" + chuoi("","","","",data.get())
    settree(returnlist(s))






def okinsert():
    pass
def okdelete():
    pass
def okupdate():
    if (name.get()+address.get()+phone.get()+clas.get()=="" or id.get()==""):
        messagebox.showerror("Error", "Chưa nhập đủ")
        return
    s = "UPDATE Student SET" + chuoi("",name.get(), address.get(), phone.get(), clas.get()) + " WHERE" + chuoi(id.get(),"","","","")
    print(s)
    commitsql(s)
    settree(returnlist("SELECT * FROM Student WHERE" + chuoi("","","","",data.get())))
def oksearch():
    s = "SELECT * FROM Student WHERE" + chuoi(id.get(), name.get(), address.get(), phone.get(), clas.get())    
    settree(returnlist(s))











def insert():
    ap = app2("insert", okinsert)
    ap.mainloop()
def delete():
    ap = app2("delete", okdelete)
    ap.mainloop()
def update():
    ap = app2("update", okupdate)
    ap.mainloop()
def search():
    ap = app2("search", oksearch)
    ap.mainloop()
def xuat():
    print(id.get())
class app2(tk.Toplevel):
    def __init__(self,st,dk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        global id, name, address, phone, clas
        id=StringVar() 
        name=StringVar()
        address=StringVar()
        phone=StringVar()
        clas= StringVar()
        self.title(st)
        Label(self, text="StudentID").grid(row=0, column=0)
        Entry(self, textvariable=id).grid(row=0, column=1)
        Label(self, text="StudentName").grid(row=1, column=0)
        Entry(self, textvariable=name).grid(row=1, column=1)
        Label(self, text="StudentAddress").grid(row=2, column=0)
        Entry(self, textvariable=address).grid(row=2, column=1)
        Label(self, text="PhoneNumber").grid(row=3, column=0)
        Entry(self, textvariable=phone).grid(row=3, column=1)
        Label(self, text="ClassID").grid(row=4, column=0)
        Entry(self, textvariable=clas).grid(row=4, column=1)
        Button(self, text="OK", command=dk).grid(row=5, column=0)
        Button(self, text="Quit", command=self.destroy).grid(row=5, column=1)




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


class frame3(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        Button(self, text="Thêm", width=15, command=insert).grid(row=0, column=0)
        Button(self, text="Xóa", width=15, command=delete).grid(row=0, column=1)
        Button(self, text="Sửa", width=15, command=update).grid(row=0, column=2)
        Button(self, text="Tìm kiếm", width=15, command=search).grid(row=0, column=3)
        Button(self, text="Quit", width=15, command=parent.destroy).grid(row=0, column=4)




class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        frame1(self).pack()
        frame2(self).pack()
        frame3(self).pack()
ap = App()
ap.mainloop()
