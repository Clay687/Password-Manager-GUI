from tkinter import *
from tkinter.messagebox import showerror,showinfo
import win32gui,win32con

root = Tk()
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide,win32con.SW_HIDE)

se = 1

root.geometry("550x400")
root.maxsize(550,400)
root.minsize(550,400)
root.title("Password Manager")
root.iconbitmap("C:\\Users\\prince\\Desktop\\GUI\\Required files\\Password.ico")

def about_func():
    showinfo("About","Dear user Passwrod Manager\n securely save your passwords and username.")

about = Menu(root)
about.add_command(label="About",command=about_func)
root.config(menu=about)

val = 0

# ALL FUCTION FOR THIS PROGRAM

def search():
    select_lbl.config(text="")
    register_btn.destroy()
    search_pass.destroy()

    pin_lbl = Label(root,text="Enter you 6-Digit PIN to login : ",font="lucida 15")
    pin_lbl.place(x=50,y=150)

    pin_entry = Entry(root,font="lucida 13",width=12)
    pin_entry.place(x=80,y=200)

    def reset_password():
        pin_lbl.config(text="")
        pin_entry.destroy()
        proceed_btn.destroy()
        reset_pass.destroy()

        q = Label(root,text="Answer the Security Question to \nchange your PIN.",font="lucida 15 bold underline")
        q.place(x=30,y=70) 

        q1 = Label(root,text="Where you were Born : ",font="lucida 13")
        q1.place(x=20,y=170)
        q1_entry = Entry(root,font="lucida 15",width=12)
        q1_entry.place(x=250,y=170)

        q2 = Label(root,text="What is your first pet name : ",font="lucida 13")
        q2.place(x=20,y=250)
        q2_entry = Entry(root,font="lucida 15",width=12)
        q2_entry.place(x=250,y=250)

        def submit_func():
            if q1_entry.get()=="Gorakhpur" and q2_entry.get()=="Sheru":
                q.config(text="")
                q1.config(text="")
                q1_entry.destroy()
                q2.config(text="")
                q2_entry.destroy()
                submit.destroy()

                l5 = Label(root,text="Enter your new 6-Digit PIN :",font="lucida 15")
                l5.place(x=30,y=100)

                new_pin = Entry(root,font="lucida 15",width=8)
                new_pin.place(x=40,y=150)

                def pin_change():
                    new_pin_text = new_pin.get()
                    path3 = "C:\\Users\\prince\\Documents\\PIN.txt"
                            
                    if len(new_pin_text)==6:
                        with open(path3,"w") as f:
                            f.write(new_pin_text)
                            showinfo("PIN changed successfully",f"Dear user now your PIN is changed to {new_pin_text}")
                            f.close()
                           
                    else:
                        showinfo("Invalid","Please enter 6-digit PIN")

                set_pin_btn = Button(root,text="Set your new PIN",font="lucida 15",fg="blue",command=pin_change)
                set_pin_btn.place(x=270,y=350)

            else:
                showinfo("Wrong Answers","Dear user you have answered security question incorrectly")
        

        submit = Button(root,text="Submit",fg="blue",font="lucida 15",command=submit_func)
        submit.place(x=350,y=350) 


    reset_pass = Button(root,text="Reset your Password",font="lucida 10",fg="white",bg="red",command=reset_password)
    reset_pass.place(x=20,y=350)

    def proceed():
        path4 = "C:\\Users\\prince\\Documents\\PIN.txt"
        with open(path4,"r") as g:
            pin = g.read()
        if pin_entry.get()==pin:
            pin_lbl.config(text="")
            pin_entry.destroy()
            proceed_btn.destroy()
            reset_pass.destroy()

            provide_lbl = Label(root,text="Please enter the required information",font="lucida 15 bold underline")
            provide_lbl.place(x=20,y=100)

            web_lbl = Label(root,text="Enter the Website or App name : ",font="lucida 13")
            web_lbl.place(x=30,y=150)

            web_entry = Entry(root,font="lucida 13",width=15)
            web_entry.place(x=305,y=153)

            def search_func():
                path1 = "C:\\Users\\prince\\Documents\\Password.txt"
                with open(path1,"r") as f:
                    lst = f.readlines()
                    app_lst = []
                    user_email_lst = []
                    password_lst = []

                    web_name = str(web_entry.get())
                    web_name1 = web_name.lower()
            
                    for i in lst:
                        l = i.split("-")
                        name = l[0]
                        user = l[1]
                        password = l[2]

                        app_lst.append(name)
                        user_email_lst.append(user)
                        password_lst.append(password)

                    for j in app_lst:
                        ind = app_lst.index(j)
                        if web_name1==j.lower():
                            global se
                            se = 0
                            user_lbl = Label(root,text=f"Username or E-Mail : {user_email_lst[ind]}",font="lucida 13")
                            user_lbl.place(x=30,y=200)
                            pass_lbl = Label(root,text=f"Password is : {password_lst[ind]}",font="lucida 13")
                            pass_lbl.place(x=30,y=250)
                            break

                    if se==1:
                        showerror("Password not found",f"Dear user you have not registered \nany password or user name with\n {web_name1}")
                    else:
                        pass

                        

            search = Button(root,text="Search",font="lucida 15",fg="blue",command=search_func)
            search.place(x=350,y=350)


        else:
            showinfo("Invalid PIN","Dear User you have entered wrong pin.Change it now if you forget it or re-enter it.")

    proceed_btn = Button(root,text="Proceed",font="lucida 15",fg="blue",width=7,command=proceed)
    proceed_btn.place(x=350,y=350)

    exit_btn = Button(root,text="Exit",font="lucida 15",fg="white",bg="red",width=7,command=exit)
    exit_btn.place(x=450,y=350)
            

def register():
    select_lbl.config(text="")
    register_btn.destroy()
    search_pass.destroy()

    new_pass_lbl = Label(root,text="Register new password",font="lucida 15 bold underline")
    new_pass_lbl.place(x=20,y=100)

    web_app_lbl = Label(root,text="1. Enter the Website or App name",font="lucida 13")
    web_app_lbl.place(x=30,y=150)

    web_app_entry = Entry(root,font="lucida 13",width=15)
    web_app_entry.place(x=305,y=153)

    user_name_lbl = Label(root,text="2. Enter the User or E-mail \n you have set",font="lucida 13")
    user_name_lbl.place(x=30,y=200)

    user_entry = Entry(root,font="lucida 13",width=23)
    user_entry.place(x=305,y=203)

    pass_lbl = Label(root,text="3. Enter the Password you have set : ",font="lucida 13")
    pass_lbl.place(x=30,y=260)

    pass_entry = Entry(root,font="lucida 13",width=15)
    pass_entry.place(x=310,y=263)

    path = "C:\\Users\\prince\\Documents\\Password.txt"

    def save():
        if web_app_entry.get()=="":
            showerror("Invalid","Please enter the Website or App name")

        elif user_entry.get()=="":
            showerror("Invalid","Please enter the User name")

        elif pass_entry.get()=="":
            showerror("Invalid","Please enter the Password")

        else:
            with open(path,"a") as a:
                web_app = web_app_entry.get()
                user_name = user_entry.get()
                password = pass_entry.get()

                a.write(web_app)
                a.write("-")
                a.write(user_name)
                a.write("-")
                a.write(password)
                a.write("\n")
                showinfo("Successfully Saved","Dear user your information is securely saved")

    save_btn = Button(root,text="Save",font="lucida 15",fg="blue",width=7,command=save)
    save_btn.place(x=350,y=350)

    exit_btn = Button(root,text="Exit",font="lucida 15",fg="white",bg="red",width=7,command=exit)
    exit_btn.place(x=450,y=350)

Label(root,text="Password Manager",fg="red",font="lucida 20 bold underline").pack(pady=20)

select_lbl = Label(root,text="Please Select One Option : ",font="lucida 15")
select_lbl.place(x=20,y=170)

register_btn = Button(root,text="Register new password",font="lucida 13",fg="blue",command=register)
register_btn.place(x=50,y=220)

search_pass = Button(root,text="Search for saved passwords",font="lucida 13",fg="blue",command=search)
search_pass.place(x=50,y=270)

root.mainloop()
