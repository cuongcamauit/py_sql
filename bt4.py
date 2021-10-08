from sqlite3.dbapi2 import DatabaseError
import tkinter as tk
from tkinter import Button, Entry, Label, Message, StringVar, ttk
from tkinter import messagebox
import sqlite3
from tkinter import font

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
        ok(0)
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
    s = "INSERT INTO Student VALUES('%s','%s','%s',%s,'%s');" %(id.get(), name.get(), address.get(), phone.get(), clas.get())
    print(s)
    commitsql(s)
def okdelete():
    s = "DELETE FROM Student WHERE" + chuoi(id.get(), name.get(), address.get(), phone.get(), clas.get())
    print(s)
    commitsql(s)
def okupdate():
    s = "UPDATE Student SET" + chuoi("",name.get(), address.get(), phone.get(), clas.get()) + " WHERE" + chuoi(id.get(),"","","","")
    s = s.replace("AND", ",")
    print(s)
    commitsql(s)
def oksearch():
    s = "SELECT * FROM Student WHERE" + chuoi(id.get(), name.get(), address.get(), phone.get(), clas.get())    
    print(s)
    settree(returnlist(s))
def insert():
    id.set("")
    name.set("")
    clas.set("")
    address.set("")
    phone.set("")
    ap = app2("insert", okinsert)
    clas.set(data.get())
    ap.mainloop()
def delete():
    ap = app3(okdelete)
    ap.mainloop()
def update():
    ap = app2("update", okupdate)
    clas.set(data.get())
    ap.mainloop()
def search():
    id.set("")
    name.set("")
    clas.set("")
    address.set("")
    phone.set("")
    ap = app2("search", oksearch)
    ap.mainloop()
def xuat():
    print(id.get())
class app3(tk.Toplevel):
    def __init__(self,dk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Label(self,text="Are you ok?", font="20").pack()
        Button(self, text="0K", command=dk, width=15).pack()
class app2(tk.Toplevel):
    def __init__(self,st,dk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        
        self.title(st)
        Label(self, text="StudentID", width=15).grid(row=0, column=0)
        Entry(self, textvariable=id).grid(row=0, column=1, sticky=tk.E + tk.W)
        Label(self, text="StudentName", width=15).grid(row=1, column=0)
        Entry(self, textvariable=name).grid(row=1, column=1, sticky=tk.E + tk.W)
        Label(self, text="StudentAddress", width=15).grid(row=2, column=0)
        Entry(self, textvariable=address).grid(row=2, column=1, sticky=tk.E + tk.W)
        Label(self, text="PhoneNumber", width=15).grid(row=3, column=0)
        Entry(self, textvariable=phone).grid(row=3, column=1, sticky=tk.E + tk.W)
        Label(self, text="ClassID", width=15).grid(row=4, column=0)
        lst2 = ("L01", "L02", "L03", "L04", "L05")
        combox2 = ttk.Combobox(self, textvariable=clas)
        combox2['value'] = lst2
        combox2['state'] = 'readonly'
        combox2.grid(row=4, column=1)
        Button(self, text="OK", command=dk, width=5).grid(row=5, column=0)
        Button(self, text="Quit", command=self.destroy, width=5).grid(row=5, column=1)
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
def item_selected(f):
    for selected_item in tree.selection():
        # dictionary
        item = tree.item(selected_item)
        # list
        record = item['values']
        print(record)
        id.set(record[0])
        name.set(record[1])
        address.set(record[2])
        phone.set(record[3])
        clas.set(record[4])
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
        tree.bind('<<TreeviewSelect>>', item_selected)
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
        global id, name, address, phone, clas, combox2
        id=tk.StringVar() 
        name=tk.StringVar()
        address=tk.StringVar()  
        phone=tk.StringVar()    
        clas= tk.StringVar()
        frame1(self).pack()
        frame2(self).pack()
        frame3(self).pack()
        self.geometry("1024x500")
        self.title("QuanLiSinhVien")
ap = App()
ap.mainloop()