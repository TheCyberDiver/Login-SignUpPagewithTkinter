from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from SignUp import mainSignUp
import mysql.connector
import time

#Defining the main login window
main = Tk()

#Setting the screen size and title
main.geometry("925x500+300+200")

#Creates the Title, Background color, Title, and Image
main.title("Login Page")
main.configure(bg='white')
heading = Label(main, text='Sign In', fg='blue', bg='white', font=('Microsoft Yahei UI Light',23,'bold'))
img = ImageTk.PhotoImage(Image.open("financialbull.jpg"))
logo = Label(main, image=img, border=0, bg='white')
logo.place(x='-75', y='0')
heading.place(x=495,y=15)


# Names for Username and Password on Login GUI and location
Userfield = Label(main, text = 'Username: ')
Passfield = Label(main, text = 'Password: ')
Userfield.place(x=500,y=80)
Passfield.place(x=500, y=150)

# Input fields for Username and Password and location
Input1 = Entry(main, fg='black', border=2, bg='white')
Input2 = Entry(main, fg='black', border=2, bg='white', show="*")
Input1.place(x=575, y=80)
Input2.place(x=575, y=150)

# Login function // Use this instead of SQL DB if wanted
# def loginClick():
#     username = Input1.get()
#     password = Input2.get()
#
#     if (username=='' and password==''):
#         messagebox.showinfo("", "Username and Password are required" )
#
#     elif (username=='Brett' and password=='H'):
#         messagebox.showinfo("", "Thank you " + username + ", You have successfully authenticated!")
#
#     else:
#         messagebox.showinfo("", "Incorrect Username or Password")

# Sign Up hyperlink
label= Label(main, text="Don't have an account?", fg='black', bg='white',font=('blue',9))
label.place(x=500, y=300)
signin = Button(main, width=6, text='Sign Up', border= 0, bg='white', cursor='hand2', fg='#57a1f8', command=mainSignUp)
signin.place(x=635, y=300)

#Setting up MYSQL
def SQLSETUP():
    mydb = mysql.connector.connect(
        host='azuredblink',
        user='User',
        password='Pass',
        database='mldb'
        )
    mycursor= mydb.cursor()
    sql = "select * from login where binary username = '%s' and binary password = '%s'" % (Input1.get(),Input2.get())
    mycursor.execute(sql)
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("", 'login successful')
        time.sleep(1)
        main.destroy()
    else:
        messagebox.showinfo("", "Incorrect username or password")

#Login button and placement on the GUI
loginButton = Button(main, text='Login', command=SQLSETUP)
loginButton.place(x=500, y=180)


main.mainloop() # main window in a loop
