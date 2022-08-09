"""
A program that stores movie information:
title,director,genre,year,rating

User can:
View all records
Search an entry
Add entry
Update entry
Delete
"""

from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        title_entry.delete(0, END)
        title_entry.insert(END, selected_tuple[1])
        director_entry.delete(0, END)
        director_entry.insert(END, selected_tuple[2])
        genre_entry.delete(0, END)
        genre_entry.insert(END, selected_tuple[3])
        year_entry.delete(0, END)
        year_entry.insert(END, selected_tuple[4])
        rating_entry.delete(0, END)
        rating_entry.insert(END, selected_tuple[5])
    except IndexError:
        pass

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), director_text.get(), genre_text.get(), year_text.get(), rating_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), director_text.get(), genre_text.get(), year_text.get(), rating_text.get())
    list1.insert(0, END)
    list1.insert(END,(title_text.get(), director_text.get(), genre_text.get(), year_text.get(), rating_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(), director_text.get(), genre_text.get(), year_text.get(), rating_text.get())

window = Tk()

window.wm_title("Movie Inventory")

title=Label(window, text="Title")
title.grid(row=0, column=0)

director=Label(window, text="Director")
director.grid(row=0, column=1)

genre=Label(window, text="Genre")
genre.grid(row=0, column=2)

year=Label(window, text="Year")
year.grid(row=0, column=3)

RotatingFileHandler=Label(window, text="Rating")
RotatingFileHandler.grid(row=0, column=4)

title_text=StringVar()
title_entry=Entry(window,textvariable=title_text,width=30)
title_entry.grid(row=1, column=0)

director_text=StringVar()
director_entry=Entry(window,textvariable=director_text,width=30)
director_entry.grid(row=1, column=1)

genre_text=StringVar()
genre_entry=Entry(window,textvariable=genre_text,width=30)
genre_entry.grid(row=1, column=2)

year_text=StringVar()
year_entry=Entry(window,textvariable=year_text,width=30)
year_entry.grid(row=1, column=3)

rating_text=StringVar()
rating_entry=Entry(window,textvariable=rating_text,width=30)
rating_entry.grid(row=1, column=4)

list1 = Listbox(window, height=6,width=150)
list1.grid(row=3, column=0, rowspan=6, columnspan=5)

list1.bind('<<ListboxSelect>>', get_selected_row)

sb1=Scrollbar(window)
sb1.grid(row=3,column=5,rowspan=6)

list1.configure(yscrollcommand=sb1)
sb1.configure(command=list1.yview)

b1=Button(window, text="View all", width=12,command=view_command)
b1.grid(row=2,column=0)

b2=Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=2,column=1)

b3=Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=2,column=2)

b4=Button(window, text="Update", width=12,command=update_command)
b4.grid(row=2,column=3)

b5=Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=2,column=4)

# b6=Button(window, text="Close", width=12,command=window.destroy)
# b6.grid(row=2,column=5)

window.mainloop()