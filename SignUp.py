from tkinter import *
from tkinter import messagebox
import mysql.connector

def mainSignUp():
    accountCreation = Tk()

    def inputSignIn():

        mydb = mysql.connector.connect(
            host='mlstockpredictiondb.mysql.database.azure.com',
            user='MLStockPredAdmin',
            password='Sup3rStr0ngP@ss',
            database='mldb'
        )
        mycursor = mydb.cursor()

        #Input validation and insertion of data into SQL Server
        sql1 = "INSERT INTO login (username, password) values('%s','%s')" % (sInput1.get(),sInput2.get())
        sql2 = "select * from login where binary username = '%s'" % (sInput1.get())
        mycursor.execute(sql2)
        results = mycursor.fetchall()
        if results:
            messagebox.showinfo("", "Username already taken, please choose another one!")
        elif sInput2.get() != sInput3.get():
            messagebox.showinfo("", "Passwords do not match")
        else:
            mycursor.execute(sql1)
            mydb.commit()
            messagebox.showinfo("", "Account Created")
            accountCreation.destroy()


    # Setting the screen size and titles
    accountCreation.geometry("400x500")
    accountCreation.configure(bg='white')
    accountCreation.title("Signup Page")
    heading = Label(accountCreation, text='Sign Up', fg='blue', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=140, y=40)


    # Titles for each prompt
    signUser = Label(accountCreation, text='Username: ')
    passUser = Label(accountCreation, text='Password: ')
    rPassUser = Label(accountCreation, text='ReEnter Password: ')
    signUser.place(x=75, y=100)
    passUser.place(x=75, y=150)
    rPassUser.place(x=30, y=200)

    #Entry for the fields
    sInput1 = Entry(accountCreation, fg='black', border=2, bg='white')
    sInput2 = Entry(accountCreation, fg='black', border=2, bg='white', show="*")
    sInput3 = Entry(accountCreation, fg='black', border=2, bg='white', show="*")
    sInput1.place(x=140, y=100)
    sInput2.place(x=140, y=150)
    sInput3.place(x=140, y=200)

    #Self explanatory
    loginButton = Button(accountCreation, text='Sign up', command=inputSignIn)
    loginButton.place(x=170, y=240)


    accountCreation.mainloop()



