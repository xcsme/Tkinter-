from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, showwarning
def registration():
    login_1 = login.get()
    email_1 = email.get()
    password_1 = password.get()
    try:
        index = l1.curselection()
        lan = l1.get(index)
    except:
        lan = ''

    if lan == '':
        print('yes')
        showerror('Выберите язык', 'Выберите язык')
        return

    
    if len(login_1)>0:
        if len(email_1)>0:
            if len(password_1)>0:
                cursor.execute("SELECT * FROM users WHERE login=?",(login_1,))
                if cursor.fetchone():
                    showwarning(title="Логин занят",message="Такой логин уже существует")
                else:
                    cursor.execute("insert into users (login, email, password,lang) values(?,?,?,?)",(login_1,email_1,password_1,lan))
                    con.commit()
                    showinfo(title="Успешная регистрация",message=" Вы успешно зарегистрированы ")
            else:
                showerror(title='Error password', message='Error password')
        else:
            showerror(title='Error email', message='Error email')
    else:
        showerror(title='Error login', message='Error login')
def auth():
    def authorization():
        login_1 = login1.get()
        password_1 = password1.get()
        cursor.execute("SELECT * FROM users WHERE login=? and password=?",(login_1,password_1))
        user = cursor.fetchone()
        if user:
            showinfo("Такой пользователь существует",f'id = {user[0]} login = {user[1]} password = {user[2]} email = {user[3]}')
        else:
            showerror('Заданы некорректные данные')

    reg.destroy()
    global auth
    auth = Tk()
    auth.geometry("600x600")
    auth.resizable(False, False)
    auth.title('Авторизация')
    login_label1 = ttk.Label(auth, text='Логин')
    login_label1.pack()
    login1 = ttk.Entry(auth)
    login1.pack()

    password_label1 = ttk.Label(auth,text='Пароль')
    password_label1.pack()
    password1 = ttk.Entry(auth, show='*')
    password1.pack()
    button2=ttk.Button(auth,text="Авторизация",command=authorization)
    button2.pack()
    button3=ttk.Button(auth,text="Регистрация",command=delete)
    button3.pack()

    c1 = ttk.Checkbutton(text='Согласиться')
    c1.pack()
    c2 = ttk.Radiobutton(text='1')
    c2.pack()
reg = Tk()
reg.geometry("250x400")
reg.resizable(False, False)
reg.title('Регистрация')
'''clicks = 0
def click_button():
    global clicks
    clicks += 1
    btn1['text'] = f"{clicks}"
'''
con = sqlite3.connect("users.db")
cursor = con.cursor()
def delete():
    global auth
    auth.destroy()

    reg = Tk()
    reg.geometry("300x400")
    reg.resizable(False, False)
    reg.title('Регистрация')
    login_label = ttk.Label(reg, text='Логин')
    login_label.pack()
    login = ttk.Entry()
    login.pack()

    password_label = ttk.Label(reg, text='Пароль')
    password_label.pack()
    password = ttk.Entry(reg, show='*')
    password.pack()

    email_label = ttk.Label(reg,text='Email')
    email_label.pack()
    email = ttk.Entry()
    email.pack()

    button1 = ttk.Button(reg, text="Регистрация", command=registration)
    button1.pack()
    button1 = ttk.Button(reg, text="Авторизация", command=auth)
    button1.pack()
#icon = PhotoImage(file='icon.png')
#root.iconphoto(icon)
'''
btn1 = ttk.Button(text='+', command=click_button)
btn1.pack()

label1 = ttk.Label(text='ФИО' )
label1.pack()

login = ttk.Entry()
login.pack()'''

login_label = ttk.Label(text='Логин')
login_label.pack()
login = ttk.Entry()
login.pack()

password_label = ttk.Label(text='Пароль')
password_label.pack()
password = ttk.Entry(show='*')
password.pack()

email_label = ttk.Label(text='Email')
email_label.pack()
email = ttk.Entry()
email.pack()
#Выбор языка
lang = ['Python', 'JS', 'C#']
lang_var = Variable(value=lang)
l1 = Listbox(listvariable=lang_var)
l1.pack()

button1=ttk.Button(text="Регистрация",command=registration)
button1.pack()
button1=ttk.Button(text="Авторизация",command=auth)
button1.pack()
reg.mainloop()