from tkinter import *
h={}
def convert():
    sentence=str(english.get())
    morce={'a':'*-','b':'-***','c':'-*-*','d':'-**','e':'*','f':'**-*','g':'--*','h':'****','i':'**','j':'*---','k':'-*-','l':'*-**','m':'--','n':'-*','o':'---','p':'*--*','q':'--*-',
       'r':'*-*','s':'***','t':'-','u':'**-','v':'***-','w':'*--','x':'-**-','y':'-*--','z':'--**',' ':' '}
    m=""
    
    for i in sentence:
        m += morce[i]
    h[sentence]=m
    morsecode.set(m)
    
    
def clear():
    english.set("")
    morsecode.set("")
    
def history():
    if h=={}:
	histor.set("history is empty")
    else:
    	histor.set(h)
    
def clearhistory():
    histor.set("")
    h.clear()
     
    
window=Tk()
window.title("Morse Code Generator")
english=StringVar()
morsecode=StringVar()
histor=StringVar()
label1=Label(text="welcome",foreground="black",background="pink",width="100",height="5").pack()
label2=Label(text="Enter your sentence").pack()
entry=Entry(textvariable=english,fg="black",bg="white", width="100").pack()
button=Button(text="convert",fg="black",bg="green",command=convert).place(x=1000,y=100)
label3=Label(text="Your Morse Code").pack()
label4=Label(textvariable=morsecode).pack()
clrbutton=Button(text="reset",command=clear).pack()


historybutton=Button(text="history",command=history).pack()
label5=Label(textvariable=histor).pack()
button=Button(text="clear history",command=clearhistory).pack()


window.mainloop()



