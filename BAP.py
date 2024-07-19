#!/usr/bin/env python
# coding: utf-8

# In[65]:


from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox #* imports classes, variables, functions but doesn't import sub-module
import time
import sqlite3
import re

#exception handling---------->
try:
    conobj=sqlite3.connect(database='bank.sqlite')
    curobj=conobj.cursor()
    curobj.execute('create table acn(acn_no integer primary key autoincrement,acn_name text,acn_pass text,acn_email text,acn_mob text,acn_bal float,acn_opendate text,acn_gender text)')
    conobj.close()
    print('table created')
except:
    print('something went wrong! table may be already created.')

win =Tk()
win.state('zoomed')
win.configure(bg='pink')
win.resizable(width=False,height=False)
title=Label(win,text='Banking Automation',font=('arial',50,'bold','underline'),bg='pink')
title.pack()

dt=time.strftime('%d %B,%Y, %A')
date = Label(win,text=f"{dt}",font=('arial',20,'bold'),bg='pink',fg='blue')
date.place(relx=.77,rely=.1)

#-------------------------------------------->

def main_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def forgotpass():
        frm.destroy()
        forgotpass_screen()
        
    def newuser():
        frm.destroy()
        newuser_screen()
        
    def login():
        global gacn
        gacn=e_acn.get()
        pwd=e_pass.get()
        if len(gacn)==0 or len(pwd)==0:
            messagebox.showwarning('validation','cells are not filled!')
            return
        else:
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute('select * from acn where acn_no=? and acn_pass=?',(gacn,pwd))
            tup=curobj.fetchone()
            conobj.close()
            if tup==None:
                messagebox.showerror('Login Screen','Invalid credentials')
            else:
                frm.destroy()
                welcome_screen()
    
    def clear():
        e_acn.delete(0,'end')
        e_pass.delete(0,'end')
        e_acn.focus()
        
    
    #account label at mainscreen
    lbl_acn=Label(frm,text='ACN',font=('arial',20,'bold'),bg='powder blue')
    lbl_acn.place(relx=.3,rely=.1)
    
    #text field of account
    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.4,rely=.1)
    e_acn.focus()
    
    #password label at mainscreen
    lbl_pass=Label(frm,text='Pass',font=('arial',20,'bold'),bg='powder blue')
    lbl_pass.place(relx=.3,rely=.2)
    
    #text field of password
    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    e_pass.place(relx=.4,rely=.2)
    
    #login button at mainscreen
    btn_login=Button(frm,text='login',font=('arial',20,'bold'),bd=5,command=login)
    btn_login.place(relx=.41,rely=.3)
    
    #clear button at mainscreen
    btn_clear=Button(frm,text='clear',font=('arial',20,'bold'),bd=5,command=clear)
    btn_clear.place(relx=.52,rely=.3)
    
    #forgot password button at mainscreen
    btn_fp=Button(frm,width=16,text='forgot password',font=('arial',20,'bold'),bd=5,command=forgotpass)
    btn_fp.place(relx=.4,rely=.4)
    
    #new user button at mainscreen
    btn_new=Button(frm,command=newuser,width=18,text='open new account',font=('arial',20,'bold'),bd=5)
    btn_new.place(relx=.39,rely=.5)

    #title created by
    title=Label(frm,text='Developed by: Neetesh Kumar',font=('arial',20,'bold'),bg='powder blue',fg='black')
    title.place(relx=.72,rely=.92)
#-------------------------------------------->
    
def forgotpass_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def back():
        frm.destroy()
        main_screen()
        
    def clear():
        e_acn.delete(0,'end')
        e_pass.delete(0,'end')
        e_email.delete(0,'end')
        e_mob.delete(0,'end')
        cb_gender.delete(0,'end')
        e_acn.focus()
    
    def forgotpass_db():
        acn=e_acn.get()
        email=e_email.get()
        mob=e_mob.get()
        
        conobj=sqlite3.connect(database='bank.sqlite')
        conobj=conobj.cursor()
        curobj.execute('select acn_pass from acn where acn_no=? and acn_email=? and acn_mob=?',(acn,email,mob))
        tup=curobj.fetchone()
        if tup==None:
            messagebox.showerror('Forgot pass','record not found')
        else:
            messagebox.showinfo('Forgot pass',f'your password: {tup[0]}')
        conobj.close()
        e_acn.delete(0,'end')
        e_email.delete(0,'end')
        e_mob.delete(0,'end')
        e_acn.focus()
        
        
        
    
    #back button at forgotpass_screen, will lead to main screen
    btn_new=Button(frm,width=15,text='back',font=('arial',20,'bold'),bd=5,command=back)
    btn_new.place(relx=0,rely=0)
    
    #account label at forgotpass_screen
    lbl_acn=Label(frm,text='ACN',font=('arial',20,'bold'),bg='powder blue')
    lbl_acn.place(relx=.3,rely=.1)
    
    #text field of account at forgotpass_screen
    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.4,rely=.1)
    e_acn.focus()
    
    #email label at forgotpass_screen
    lbl_email=Label(frm,text='Email',font=('arial',20,'bold'),bg='powder blue')
    lbl_email.place(relx=.3,rely=.2)
    
    #text field of email label at forgotpass_screen
    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.4,rely=.2)
    
    #Mobile label at forgotpass_screen
    lbl_Mob=Label(frm,text='Mobile',font=('arial',20,'bold'),bg='powder blue')
    lbl_Mob.place(relx=.3,rely=.3)
    
    #text field of Mobile at forgotpass_screen
    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.4,rely=.3)
    
    #details of submit button at forgotpass_screen
    btn_submit=Button(frm,text='Submit',font=('arial',20,'bold'),bd=5,command=forgotpass_db)
    btn_submit.place(relx=.42,rely=.45)
    
    #details of clear button at forgotpass_screen
    btn_clear=Button(frm,command=clear,text='clear',font=('arial',20,'bold'),bd=5)
    btn_clear.place(relx=.52,rely=.45)
    
#-------------------------------------------->
    
def newuser_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def back():
        frm.destroy()
        main_screen()
        
    def newuser_db():
        name=e_name.get()
        pwd=e_pass.get()
        email=e_email.get()
        mob=e_mob.get()
        gender=cb_gender.get()
        #atype=cb_atype.get()
        bal=0
        opendate=time.strftime('%d %B,%Y, %A')
        
        #regex function
        match=re.fullmatch('[6-9][0-9]{9}',mob)
        if match==None:
            messagebox.showerror('validation','invalid mob no')
            return
        
        match=re.fullmatch("[a-zA-Z0-9_]+@[a-zA-Z]+[.][a-zA-Z]+",email)
        if match==None:
            messagebox.showerror('validation','invalid email')
            return
        
        #database query to insert data
        import sqlite3
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('insert into acn(acn_name,acn_pass,acn_email,acn_mob,acn_gender,acn_opendate,acn_bal) values(?,?,?,?,?,?,?)',(name,pwd,email,mob,gender,opendate,bal))
        conobj.commit()
        conobj.close()
        

        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('select max(acn_no) from acn')
        tup=curobj.fetchone()
        conobj.commit()
        conobj.close()
        
        messagebox.showinfo('New User',f'Account Created! Account No:{tup[0]}')
        e_name.delete(0,'end')
        e_pass.delete(0,'end')
        e_email.delete(0,'end')
        e_mob.delete(0,'end')
        cb_gender.delete(0,'end')
        #cb_atype.delete(0,'end')
        e_name.focus()
        
        
        
    def clear():
        e_name.delete(0,'end')
        e_pass.delete(0,'end')
        e_email.delete(0,'end')
        e_mob.delete(0,'end')
        cb_gender.delete(0,'end')
        #cb_atype.delete(0,'end')
        e_name.focus()
    
    #back button at newuser_screen, will lead to main screen
    btn_new=Button(frm,width=15,text='back',font=('arial',20,'bold'),bd=5,command=back)
    btn_new.place(relx=0,rely=0)
    
    #name label at newuser_screen
    lbl_name=Label(frm,text='Name',font=('arial',20,'bold'),bg='powder blue')
    lbl_name.place(relx=.3,rely=.1)
    
    #text field of name at newuser_screen
    e_name=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_name.place(relx=.5,rely=.1)
    e_name.focus()
    
    #password label at newuser_screen
    lbl_pass=Label(frm,text='Pass',font=('arial',20,'bold'),bg='powder blue')
    lbl_pass.place(relx=.3,rely=.2)
    
    #text field of password at newuser_screen
    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    e_pass.place(relx=.5,rely=.2)
    
    #email label at newuser_screen
    lbl_email=Label(frm,text='Email',font=('arial',20,'bold'),bg='powder blue')
    lbl_email.place(relx=.3,rely=.3)
    
    #text field of email label at newuser_screen
    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.5,rely=.3)
    
    #Mobile label at newuser_screen
    lbl_Mob=Label(frm,text='Mobile',font=('arial',20,'bold'),bg='powder blue')
    lbl_Mob.place(relx=.3,rely=.4)
    
    #text field of Mobile at newuser_screen
    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.5,rely=.4)
    
    #Gender label at newuser_screen
    lbl_gender=Label(frm,text='Gender',font=('arial',20,'bold'),bg='powder blue')
    lbl_gender.place(relx=.3,rely=.5)
    
    #dropdown field of Gender label at newuser_screen
    cb_gender=Combobox(frm,values=['--Select--','Male','Female'],font=('arial',20,'bold'))
    cb_gender.place(relx=.5,rely=.5)
    
    #account type at newuser_screen
    #lbl_atype=Label(frm,text='Account type',font=('arial',20,'bold'),bg='powder blue')
    #lbl_atype.place(relx=.3,rely=.6)
    
    #text field of account type at newuser_screen
    #cb_atype=Combobox(frm,values=['--Select--','Current Account','Saving Account'],font=('arial',20,'bold'))
    #cb_atype.place(relx=.5,rely=.6)
    
    #submit button at newuser_screen
    btn_submit=Button(frm,text='Submit',font=('arial',20,'bold'),bd=5,command=newuser_db)
    btn_submit.place(relx=.4,rely=.7)
    
    #clear button at newuser_screen
    btn_clear=Button(frm,command=clear,text='clear',font=('arial',20,'bold'),bd=5)
    btn_clear.place(relx=.5,rely=.7)

#--------------------------------------------> 

def welcome_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def logout():
        frm.destroy()
        main_screen()
    
    #Nested frame at 3rd level----------------->
    def details():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2) #shift-tab to open arguments
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.5)
        
        #this is details screen dialogue
        lbl_details=Label(ifrm,text='This is Details screen',font=('arial',20,'bold'),bg='white',fg='blue')
        #lbl_details.place(relx=0,rely=0)
        lbl_details.pack()
        
        #SQL query to show data for the specific labels
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('select acn_opendate,acn_bal,acn_gender,acn_email,acn_mob from acn where acn_no=?',(gacn,))
        tup=curobj.fetchone()
        
        #detail screen info
        lbl_open_date=Label(ifrm,text=f'Open Date: {tup[0]}',font=('arial',15,'bold'),bg='white')
        lbl_open_date.place(relx=.2,rely=.12)
        
        lbl_bal=Label(ifrm,text=f'Avl bal: {tup[1]}',font=('arial',15,'bold'),bg='white')
        lbl_bal.place(relx=.2,rely=.2)
        
        lbl_gender=Label(ifrm,text=f'Gender: {tup[2]}',font=('arial',15,'bold'),bg='white')
        lbl_gender.place(relx=.2,rely=.28)
        
        lbl_email=Label(ifrm,text=f'Email: {tup[3]}',font=('arial',15,'bold'),bg='white')
        lbl_email.place(relx=.2,rely=.36)
        
        lbl_mob=Label(ifrm,text=f'Mobile: {tup[4]}',font=('arial',15,'bold'),bg='white')
        lbl_mob.place(relx=.2,rely=.44)
        
        conobj.close()
        
        #------------------>
        
    def update():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2) #shift-tab to open arguments
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.5)
        
        #SQL query to show label's data
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('Select acn_name,acn_pass,acn_email,acn_mob from acn where acn_no=?',(gacn,))
        tup=curobj.fetchone()
        conobj.close()
        
        #this is update screen dialogue
        lbl_update=Label(ifrm,text='This is Update Screen',font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_update.pack()
        
        #name label
        lbl_name=Label(ifrm,text='Name',font=('arial',20,'bold'),bg='white')
        lbl_name.place(relx=.1,rely=.1)
    
        #text field of name
        e_name=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_name.place(relx=.1,rely=.2)
        e_name.focus()
        e_name.insert(0,tup[0])
    
        #password label
        lbl_pass=Label(ifrm,text='Pass',font=('arial',20,'bold'),bg='white')
        lbl_pass.place(relx=.1,rely=.4)
    
        #text field of password
        e_pass=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_pass.place(relx=.1,rely=.5)
        e_pass.insert(0,tup[1])
    
        #email label at newuser_screen
        lbl_email=Label(ifrm,text='Email',font=('arial',20,'bold'),bg='white')
        lbl_email.place(relx=.5,rely=.1)
    
        #text field of email label
        e_email=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_email.place(relx=.5,rely=.2)
        e_email.insert(0,tup[2])
    
        #Mobile label
        lbl_Mob=Label(ifrm,text='Mobile',font=('arial',20,'bold'),bg='white')
        lbl_Mob.place(relx=.5,rely=.4)

        #text field of Mobile
        e_mob=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_mob.place(relx=.5,rely=.5)
        e_mob.insert(0,tup[3])
        
        def update_db():
            name=e_name.get()
            pwd=e_pass.get()
            email=e_email.get()
            mob=e_mob.get()
            
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute('Update acn set acn_name=?,acn_pass=?,acn_email=?,acn_mob=? where acn_no=?',(name,pwd,email,mob,gacn))
            conobj.commit()
            conobj.close()
            
            messagebox.showinfo('Update','record updated!')
            details()
        
        #Update button
        btn_update=Button(ifrm,text='Update',font=('arial',20,'bold'),bd=5,command=update_db)
        btn_update.place(relx=.38,rely=.7)
    
    def deposit():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2) #shift-tab to open arguments
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.5)
        
        #this is deposit screen dialogue
        lbl_deposit=Label(ifrm,text='This is Deposit Screen',font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_deposit.pack()
        
        #amount label
        lbl_amt=Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.1,rely=.2)
    
        #text field of amount
        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.3,rely=.2)
        e_amt.focus()
        
        def deposit_db():
            amt=float(e_amt.get())
            
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute('Update acn set acn_bal=acn_bal+? where acn_no=?',(amt,gacn))
            conobj.commit()
            conobj.close()
            
            messagebox.showinfo('Update',f'{amt} Amount credited!')
            details()
            
        
        #deposit button
        btn_dep=Button(ifrm,text='Deposit',font=('arial',20,'bold'),bd=5,command=deposit_db)
        btn_dep.place(relx=.3,rely=.4)
    
    def withdraw():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2) #shift-tab to open arguments
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.5)
        
        #this is withdraw screen dialogue
        lbl_withdraw=Label(ifrm,text='This is Withdraw Screen',font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_withdraw.pack()
        
        #amount label
        lbl_amt=Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.1,rely=.2)
    
        #text field of amount
        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.3,rely=.2)
        e_amt.focus()
        
        def withdraw_db():
            amt=float(e_amt.get())
            
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute('Select acn_bal from acn where acn_no=?',(gacn,))
            tup=curobj.fetchone()
            avail_bal=tup[0]
            conobj.close()
            
            if avail_bal>=amt:
                conobj=sqlite3.connect(database='bank.sqlite')
                curobj=conobj.cursor()
                curobj.execute('Update acn set acn_bal=acn_bal-? where acn_no=?',(amt,gacn))
                conobj.commit()
                conobj.close()
                messagebox.showinfo('Update',f'{amt} Amount withdrawn!')
                details()
            else:
                messagebox.showwarning('Withdraw','Insufficient balance')
                details()
            
        
        #withdraw button
        btn_withd=Button(ifrm,text='Withdraw',font=('arial',20,'bold'),bd=5,command=withdraw_db)
        btn_withd.place(relx=.3,rely=.4)
        
    def transfer():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2) #shift-tab to open arguments
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.5)
        
        #this is withdraw screen dialogue
        lbl_transfer=Label(ifrm,text='This is Transfer Screen',font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_transfer.pack()
        
        ##amount label
        lbl_amt=Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.1,rely=.2)
    
        #text field of amount label
        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.3,rely=.2)
        e_amt.focus()
        
        #to account label
        lbl_to=Label(ifrm,text='To Account',font=('arial',20,'bold'),bg='white')
        lbl_to.place(relx=.1,rely=.4)
    
        #text field of to account
        e_to=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_to.place(relx=.3,rely=.4)
        
        def transfer_db():
            amt=float(e_amt.get())
            to_acn=e_to.get()
            
            if to_acn==gacn:
                messagebox.showwarning('Transfer',"Invalid Account No")
                return
            
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute('Select acn_bal from acn where acn_no=?',(gacn,))
            tup=curobj.fetchone()
            avail_bal=tup[0]
            conobj.close()
            
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute('Select acn_no from acn where acn_no=?',(to_acn,))
            tup=curobj.fetchone()
            conobj.close()
            
            if tup==None:
                messagebox.showwarning('Transfer',"Account doesn't exist!")
                return
            if avail_bal>=amt:
                conobj=sqlite3.connect(database='bank.sqlite')
                curobj=conobj.cursor()
                curobj.execute('Update acn set acn_bal=acn_bal+? where acn_no=?',(amt,to_acn))
                curobj.execute('Update acn set acn_bal=acn_bal-? where acn_no=?',(amt,gacn))
                conobj.commit()
                conobj.close()
                messagebox.showinfo('Update',f'{amt} Amount Transferred to ACN {to_acn}')
                details()
            else:
                messagebox.showwarning('Withdraw','Insufficient balance!')
                details()
        
        #withdraw button
        btn_sub=Button(ifrm,text='Submit',font=('arial',20,'bold'),bd=5,command=transfer_db)
        btn_sub.place(relx=.3,rely=.6)
        
    #----------------------->
    
    #database connect query to show account name by their account no
    conobj=sqlite3.connect(database='bank.sqlite')
    curobj=conobj.cursor()
    curobj.execute('select acn_name from acn where acn_no=?',(gacn,))
    tup=curobj.fetchone()
    conobj.close()
        
    #welcome label at welcome_screen
    lbl_wel=Label(frm,text=f'Welcome! {tup[0]}',font=('arial',20,'bold'),bg='powder blue')
    lbl_wel.place(relx=0,rely=0)
    
    #logout button at welcome_screen, will lead to main screen
    btn_logout=Button(frm,text='logout',font=('arial',20,'bold'),bd=5,command=logout)
    btn_logout.place(relx=.9,rely=0)
    
    #details button at welcome_screen
    btn_details=Button(frm,width=10,command=details,text='Details',font=('arial',20,'bold'),bd=5)
    btn_details.place(relx=0,rely=.1)
    
    #update button at welcome_screen
    btn_update=Button(frm,width=10,command=update,text='Update',font=('arial',20,'bold'),bd=5)
    btn_update.place(relx=0,rely=.2)
    
    #deposit button at welcome_screen
    btn_deposit=Button(frm,width=10,command=deposit,text='Deposit',font=('arial',20,'bold'),bd=5)
    btn_deposit.place(relx=0,rely=.3)
    
    #withdraw button at welcome_screen
    btn_withdraw=Button(frm,width=10,command=withdraw,text='Withdraw',font=('arial',20,'bold'),bd=5)
    btn_withdraw.place(relx=0,rely=.4)
    
    #transfer button at welcome_screen
    btn_transfer=Button(frm,width=10,command=transfer,text='Transfer',font=('arial',20,'bold'),bd=5)
    btn_transfer.place(relx=0,rely=.5)

    
#-------------------------------------------->    
    
main_screen()
win.mainloop()


# In[ ]:




