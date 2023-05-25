#Programmer: Jason Drake
#email: jdrake16@cnm.edu

#imports
from encodings import search_function
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import customtkinter
import sqlite3

# connects/creates database
conn = sqlite3.connect('student.db')
curs = conn.cursor()

def search_name():
    try:        
        #get user input
        name_input =  name_entry.get()
        
        #store our info into a var to use with LIKE clause
        infovar = (f'%{name_input}%')
        
        curs.execute("SELECT * FROM student_data WHERE name LIKE ?",(infovar,))
        info = curs.fetchall()
        
        #clear contents of ScrolledText
        results_area.delete(1.0, END)
        
        #display our results into our ScrolledText area
        for i in info:
            results_area.insert(INSERT, i)
            results_area.insert(INSERT, "\n")
        
        #save changes to the database
        conn.commit()
        
    except Exception as exc:
        results_area.delete(1.0, END)
        results_area.insert(INSERT, "PLEASE SPELL CORRECTLY!\n")
        results_area.insert(INSERT, exc)
        results_area.insert(INSERT, "\n")

def search_lang():    
    try:        
        #get user input
        lang_input =  lang_entry.get()
        
        #store our info into a var to use with LIKE clause
        infovar = (f'%{lang_input}%')
        
        curs.execute("SELECT * FROM student_data WHERE lang LIKE ?",(infovar,))
        info = curs.fetchall()
        
        #clear contents of ScrolledText
        results_area.delete(1.0, END)
        
        #display our results into our ScrolledText area
        for i in info:
            results_area.insert(INSERT, i)
            results_area.insert(INSERT, "\n")
        
        #save changes to the database
        conn.commit()
        
    except Exception as exc:
        results_area.delete (1.0, END)
        results_area.insert(INSERT, "PLEASE SPELL CORRECTLY!\n")
        results_area.insert(INSERT, exc)
        results_area.insert(INSERT, "\n")

def search_date():    
    try:        
        #get user input
        date_input =  date_entry.get()
        
        #store our info into a var to use with LIKE clause
        infovar = (f'%{date_input}%')
        
        curs.execute("SELECT * FROM student_data WHERE date LIKE ?",(infovar,))
        info = curs.fetchall()
        
        #clear contents of ScrolledText
        results_area.delete(1.0, END)
        
        #display our results into our ScrolledText area
        for i in info:
            results_area.insert(INSERT, i)
            results_area.insert(INSERT, "\n")
        
        #save changes to the database
        conn.commit()
        
    except Exception as exc:
        results_area.delete (1.0, END)
        results_area.insert(INSERT, "PLEASE SPELL CORRECTLY!\n")
        results_area.insert(INSERT, exc)
        results_area.insert(INSERT, "\n")

def search_time():    
    try:        
        #get user input
        time_input =  time_entry.get()
        
        #store our info into a var to use with LIKE clause
        infovar = (f'%{time_input}%')
        
        curs.execute("SELECT * FROM student_data WHERE time LIKE ?",(infovar,))
        info = curs.fetchall()
        
        #clear contents of ScrolledText
        results_area.delete(1.0, END)
        
        #display our results into our ScrolledText area
        for i in info:
            results_area.insert(INSERT, i)
            results_area.insert(INSERT, "\n")
        
        #save changes to the database
        conn.commit()
        
    except Exception as exc:
        results_area.delete (1.0, END)
        results_area.insert(INSERT, "PLEASE SPELL CORRECTLY!\n")
        results_area.insert(INSERT, exc)
        results_area.insert(INSERT, "\n")

def search_inst():    
    try:        
        #get user input
        inst_input =  inst_entry.get()
        
        #store our info into a var to use with LIKE clause
        infovar = (f'%{inst_input}%')
        
        curs.execute("SELECT * FROM student_data WHERE inst LIKE ?",(infovar,))
        info = curs.fetchall()
        
        #clear contents of ScrolledText
        results_area.delete(1.0, END)
        
        #display our results into our ScrolledText area
        for i in info:
            results_area.insert(INSERT, i)
            results_area.insert(INSERT, "\n")
        
        #save changes to the database
        conn.commit()
        
    except Exception as exc:
        results_area.delete (1.0, END)
        results_area.insert(INSERT, "PLEASE SPELL CORRECTLY!\n")
        results_area.insert(INSERT, exc)
        results_area.insert(INSERT, "\n")

def exitapp():
    #close DB
    conn.close()
    top.destroy()

#customkinter setup
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#top = Tk()
top = customtkinter.CTk()
top.geometry("600x550") #600,400
top.title('Student Database')

#frame for labels, entrys, and buttons
main_frame = customtkinter.CTkFrame(top, corner_radius=10)
main_frame.pack(pady=10)


#label for name
name_label = customtkinter.CTkLabel(main_frame, text="Enter Name")
name_label.grid(row=0, column=0, padx=10, pady=10)
#entry for name 
name_entry = customtkinter.CTkEntry(main_frame)
name_entry.grid(row=0, column=1, padx=10, pady=10)
#button for name
name_button = customtkinter.CTkButton(main_frame, text = 'Search Name', command = search_name)
name_button.grid(row=0, column=2, padx=10, pady=10)


#label for lang
lang_label = customtkinter.CTkLabel(main_frame, text="Enter Lang")
lang_label.grid(row=1, column=0, padx=10, pady=10)
#entry for lang 
lang_entry = customtkinter.CTkEntry(main_frame)
lang_entry.grid(row=1, column=1, padx=10, pady=10)
#button for lang
lang_button = customtkinter.CTkButton(main_frame, text = 'Search Lang', command = search_lang)
lang_button.grid(row=1, column=2, padx=10, pady=10)


#label for date
date_label = customtkinter.CTkLabel(main_frame, text="Enter Date")
date_label.grid(row=2, column=0, padx=10, pady=10)
#entry for date
date_entry = customtkinter.CTkEntry(main_frame)
date_entry.grid(row=2, column=1, padx=10, pady=10)
#button for date
date_button = customtkinter.CTkButton(main_frame, text = 'Search Date', command = search_date)
date_button.grid(row=2, column=2, padx=10, pady=10)

#label for time
time_label = customtkinter.CTkLabel(main_frame, text="Enter Time")
time_label.grid(row=3, column=0, padx=10, pady=10)
#entry for time
time_entry = customtkinter.CTkEntry(main_frame)
time_entry.grid(row=3, column=1, padx=10, pady=10)
#button for time
time_button = customtkinter.CTkButton(main_frame, text = 'Search Time', command = search_time)
time_button.grid(row=3, column=2, padx=10, pady=10)

#label for instructor
inst_label = customtkinter.CTkLabel(main_frame, text="Enter Inst")
inst_label.grid(row=4, column=0, padx=10, pady=10)
#entry for instructor
inst_entry = customtkinter.CTkEntry(main_frame)
inst_entry.grid(row=4, column=1, padx=10, pady=10)
#button for instructor
inst_button = customtkinter.CTkButton(main_frame, text = 'Search Inst', command = search_inst)
inst_button.grid(row=4, column=2, padx=10, pady=10)

#frame for results ScrolledText
results_frame = customtkinter.CTkFrame(top, corner_radius=10)
results_frame.pack(pady=10)

#ScrolledText area for our results
results_area = ScrolledText(results_frame, width=60,height=10, bg='#292929', fg='silver') #65,14
results_area.pack(pady=10)
#look up how to make scrolledtext read-only

#button for exitapp
exit_button = customtkinter.CTkButton(master=top, text = 'EXIT', command = exitapp)
exit_button.pack(pady=20)

#run the app 
top.mainloop()

# name TEXT,
# lang TEXT,
# date TEXT,
# time TEXT,
# inst TEXT
