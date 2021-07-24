"""
Group: 'bio'
Login test v1
Yixin Zhang
"""
import tkinter as tk
import pickle
#Window
window=tk.Tk()
window.title('Bio group\'s vpn')
window.geometry('450x300')
#Locate Canvas
canvas=tk.Canvas(window,height=300,width=500)
imagefile=tk.PhotoImage(file='background.png')
image=canvas.create_image(0,0,anchor='nw',image=imagefile)
canvas.pack(side='top')
#Password
tk.Label(window,text='Users name:').place(x=100,y=150)
tk.Label(window,text='Password:').place(x=100,y=190)
#users name frame
var_usr_name=tk.StringVar()
entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=150)
#password frame
var_usr_pwd=tk.StringVar()
entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=160,y=190)
 
#login function
def usr_log_in():
    #get info
    usr_name=var_usr_name.get()
    usr_pwd=var_usr_pwd.get()
    #locally info
    try:
        with open('usr_info.pickle','rb') as usr_file:
            usrs_info=pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle','wb') as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    #check unser
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='welcome',
                                   message='Welcome：'+usr_name)
        #password wrong
        else:
            tk.messagebox.showerror(message='Please check login infomation.')
    #empty return
    elif usr_name=='' or usr_pwd=='' :
        tk.messagebox.showerror(message='Users name and Password cannot be empty.')
    #not found
    else:
        is_signup=tk.messagebox.askyesno('Welcome to use bio group\'s VPN','Do you want to sign up now?')
        if is_signup:
            usr_sign_up()
#reg function
def usr_sign_up():
    #check reg function
    def signtowcg():
        #get info
        nn=new_name.get()
        np=new_pwd.get()
        npf=new_pwd_confirm.get()
 
        #double check
        try:
            with open('usr_info.pickle','rb') as usr_file:
                exist_usr_info=pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info={}           
            
        #check user info
        if nn in exist_usr_info:
            tk.messagebox.showerror('wrong','user exist')
        elif np =='' or nn=='':
            tk.messagebox.showerror('wrong','user and password could not empty')
        elif np !=npf:
            tk.messagebox.showerror('wrong','not ')
        #registrate to database
        else:
            exist_usr_info[nn]=np
            with open('usr_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo('welcome','registrate success')
            #reg sucususs 
            window_sign_up.destroy()
    #new canvas
    window_sign_up=tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('registrate')
    #user tag and frame
    new_name=tk.StringVar()
    tk.Label(window_sign_up,text='user\'name：').place(x=10,y=10)
    tk.Entry(window_sign_up,textvariable=new_name).place(x=150,y=10)
    #password tag and frame
    new_pwd=tk.StringVar()
    tk.Label(window_sign_up,text='Please enter password：').place(x=10,y=50)
    tk.Entry(window_sign_up,textvariable=new_pwd,show='*').place(x=150,y=50)    
    #re-type password tag and frame
    new_pwd_confirm=tk.StringVar()
    tk.Label(window_sign_up,text='Please enter password again：').place(x=10,y=90)
    tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*').place(x=150,y=90)    
    #confirm buttom and position
    bt_confirm_sign_up=tk.Button(window_sign_up,text='Information confrimed',
                                 command=signtowcg)
    bt_confirm_sign_up.place(x=150,y=130)
#exit function
def usr_sign_quit():
    window.destroy()
#login and reg buttom
bt_login=tk.Button(window,text='Sign in',command=usr_log_in)
bt_login.place(x=140,y=230)
bt_logup=tk.Button(window,text='Regstrate',command=usr_sign_up)
bt_logup.place(x=210,y=230)
bt_logquit=tk.Button(window,text='Exit',command=usr_sign_quit)
bt_logquit.place(x=280,y=230)
#main function
window.mainloop()
