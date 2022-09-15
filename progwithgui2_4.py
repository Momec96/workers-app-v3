
from fileinput import close
import os
os.system('cls')
from tkinter import *
from PIL import ImageTk
import PIL.Image
import sys
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('workers.sqlite')
cur = conn.cursor()




handle=open('text.txt',"a")
from tkinter import *
from tkinter import ttk
import tkinter as tk
root=Tk()
root.title("Welcome to Workers app")
root.geometry("800x570")
bg = PIL.Image.open("Rute_logo.png")
img=bg.resize((350, 350))
my_img=ImageTk.PhotoImage(img)
label1 = Label( root, image = my_img)
label1.place(x = 360,y = 170)
########################

text=Text(root, width=35, height=22,bg = "light cyan")
text.place(x=5,y=200)

sifirmi=0

""" def confirm():
    answer = askyesno(title='Onay',message='Verileri silmek istediğinen emin misin ?')
    if answer:
        root.destroy() """
def sifirla():
    answer = askyesno(title='Onay',message='Verileri silmek istediğinen emin misin ?')
    if answer:
        handle=open('text.txt',"w")
        text.delete('1.0', END)
        text.insert(END, "isim soyisim    yapabildiği işler\n-----------------------------------")
        sifirmi=1
new = tk.Button(
    root,
    text='Verileri sıfırla.',height=4, width=10,bg='red',
    command=sifirla
)
new.place(x=10, y=80)
########################




text.insert(END, "isim soyisim    yapabildiği işler\n-----------------------------------")
f= open("text.txt")
#t is a Text widget
text.insert(END, f.read())

#text.insert(END,"\n")


ttk.Label(root,text="Hoş Geldiniz\nLütfen görevler arasında sadece virgül(,) yazınız.",font=("Arial Bold", 12)).pack()


ttk.Label(root,text ="isim soyisim:",font=("Arial Bold", 10)).pack()
entry1=ttk.Entry(root,width=25)
entry1.pack()

ttk.Label(root,text ="Yapmaya yatkın olduğu görevler:",font=("Arial Bold", 10)).pack()
entry2=ttk.Entry(root,width=25)
entry2.pack()

bu1=ttk.Button(root,text="Ekle",width=25)

bu1.pack()
bu2=tk.Button(root,text="Bu kadar.",height=4, width=10,bg='green')
bu2.pack()
bu2.place(x=600, y=75)
#txtlist=tk.Text(root).pack()
#txtlist.place(x = 180,y = 170)


def buclick():
    isim=entry1.get()
    isler=entry2.get()
    print(isim,isler)


    Text(root)
    handle.write(isim)
    handle.write("\t")
    handle.write(isler)
    handle.write("\n")
    entry1.delete(0,END)
    entry2.delete(0,END)
    #text.get(isim)
    #text.insert(entry1.get())
    text.insert(END, isim+"        "+isler+"\n")


def buclick2():
    cur.execute('DROP TABLE IF EXISTS workers')
    root.destroy()
    time.sleep(4)
def disable_event():
   sys.exit()

root.protocol("WM_DELETE_WINDOW", disable_event)   # programın x tuşu or alt+f4
bu1.config(command=buclick)

bu2.config(command=buclick2)
root.resizable(width=False, height=False)



root.mainloop()

handle=open('text.txt',"r")

######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################

print("\n\n\n")
import os
import re
import time
import random
import linecache
import itertools
import sqlite3
from tkinter.tix import COLUMN
os.system('cls')

#############################
conn = sqlite3.connect('workers.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS workers')

cur.execute('CREATE TABLE workers (isim TEXT, count TEXT,yapilan TEXT)')

#############################
#filename=input("file name:")
#if len(filename)<1:
filename='text.txt'
handle =open(filename)
adlar=list() #adlar
satir=0      #satır sayısı
isler2=list() #işleri listeye eklemek
isler=list()

#### altındaki 2 loppun(program ve program 1 deki loopların birleşimi) birleşimi
for x in handle:
    x=x.strip()  #\n kaldırmak için
    z=x.split("\t") #ikiye bölmek
    iss=z[1] #2.kısım işler  # isler listesinden farklı olması için o adı verdim
    add=z[0] #1.kısım isimler

    isler.append(iss) #2.kısım işler
    adlar.append(z[0]) #1.kısım isimler
    a=isler[satir].split(",")   #işlerin numarasını almak
    satir+=1 #satır sayısı
    isler2.append(a) #işleri listeye kaydetmek

    row = cur.fetchone()
    if row is None:
	    cur.execute('''INSERT INTO workers (isim, count) VALUES ( ?, ? )''', (add,iss ) )
""" for x,y in zip(adlar,isler):
    print(x ,"yapmaya yatkın oldukları işler: ",y) """

yapilan_görev=list()
yapankisiler=list()
min=1
#deneme ###############################
#print("isler2=",isler2)
"""print("isler 2 unsuru",isler[2])
print(type(isler[2])) """

#######################################
#bir görevin kaç kişi yapabildiğini görmek
gorevler=dict()
for x in isler2:
    for a in x:
        gorevler[a]=gorevler.get(a,0)+1
g = sorted(gorevler.items(), key=lambda x: x[1]) # görevlerin tekrarını sıralamak için
#print(len(g))
enazgorev=list()
for x in g:
    enazgorev.append(x[0])
#print("values= ",gorevler.values())
birler=0
for x in gorevler.values():
    if x==1:
        birler=birler+1
#print("birleeeeeeeer:",birler)
#print(len(isler2))
#print("\n\n")
print("görevler:",gorevler)
#print(g)
print("sırasıyla en az bulunan görev:",enazgorev)


kisigorevsayisi=dict()
min2=0
for z in range(birler):#range(birler):#range(enazgorev):#isler2:
    for x in isler2:
        for a in x:# or len(x)==1: # x eşittir sırayla işler2 nın içindeki listelerin elemanları
            if a ==enazgorev[min2]:# or len(x)==1:# and gorevler[a]==2:
                pos=isler2.index(x)
                yapan=adlar[pos]
                yapilan_görev.append(a)
                yapankisiler.append(yapan) 
                kisigorevsayisi[yapan]=kisigorevsayisi.get(yapan,0)+1
                #print(a,"görevi",yapan,"yaptı.")
    min2+=1

templist=list()#tek görevli kişiye görevini verildiğinde görevi yapılmış olarak işaretlemek
#print(len(isler[4]))
for z in isler2:
    if len(z)==1:
        for a in z:
            cur.execute("UPDATE workers SET yapilan =? WHERE isim =?",(a,adlar[isler2.index(z)])) #tek görevli kişiye görevini veriyor
            if a not in yapilan_görev: # uniqu görev oldmadığında eklemek çünkü görev tekrarlanabilir
                templist.append(a)


print("yapılan görevler: ",yapilan_görev,templist) 
print("yapan kişiler : ",yapankisiler)

kisigorevsayisi=dict()
for x in yapankisiler:
    kisigorevsayisi[x]=kisigorevsayisi.get(x,0)+1

ll=kisigorevsayisi.values()
#print(kisigorevsayisi) 
#print("\n\n")

kalangorev=list()
#################################
for x in enazgorev:
    if x in yapilan_görev or x in templist:
        continue
    kalangorev.append(x)
print("henüz yapılmayan görev:",kalangorev)
###########################################################################
#alttaki kısım birden fazla görev yapan kişinin adını silmek için
yapankisisayisi=list()
for x in yapankisiler:
    if x not in yapankisisayisi:
        yapankisisayisi.append(x)
#print("yapan kişiler ve sayısı: ",yapankisisayisi,len(yapankisisayisi))

tt=0
if len(yapankisisayisi)>2:
    while tt<len(yapankisisayisi):
        if yapankisiler[tt]==yapankisiler[tt-1]:
            yapankisiler.pop(tt) # or tt-1
            tt=tt-1
            yapilan_görev[tt] =yapilan_görev[tt]+","+yapilan_görev[tt+1]
            yapilan_görev.remove(yapilan_görev[tt+1]) 
        tt=tt+1
while len(yapilan_görev)>len(yapankisisayisi):
    yapilan_görev[len(yapilan_görev)-2]=yapilan_görev[len(yapilan_görev)-1]+","+yapilan_görev[len(yapilan_görev)-2]  #sondan önceki eleman =son eleman + virgül + sondan bir önceki eleman
    yapilan_görev.pop(len(yapilan_görev)-1) # son elemanı silme
############################################################################
#print(yapankisiler)
#print(yapilan_görev)
##############################
#DÜZENLENMİŞ LİSTELERİ VERİ TABANINA YÜKLEMEK
for x,y in zip(yapankisiler,yapilan_görev):
    cur.execute("UPDATE workers SET yapilan =? WHERE isim =?",(y,x))
#############################
cur.execute('''ALTER TABLE workers ADD COLUMN Kalan_görevler''')
cur.execute('''ALTER TABLE workers RENAME COLUMN count TO Yapmaya_yatkın_olduğu_görevler''')
cur.execute('''ALTER TABLE workers RENAME COLUMN yapilan TO Yapacağı_görevler_Zorunlu''')


#os.system('cls')

 
templist2=list()
tempstr=""
for y in isler2:
    for z in y:
        if z in kalangorev :
            templist2.append(z)
            """ cur.execute('UPDATE workers set kalan_görevler =? WHERE isim=?',(x,adlar[isler.index(y)])) """
        else:
            continue
    #print(templist2)
    if len(templist2)>1:
        for u in templist2:
            tempstr=u+","+tempstr
    elif len(templist2)==1 :
        tempstr=templist2[0]
    if len(tempstr)>1 and tempstr[-1]==",":
        tempstr=tempstr[:-1]
    #print(tempstr)
    if len(tempstr)>=1:
        cur.execute('UPDATE workers set kalan_görevler =? WHERE isim=?',(tempstr,adlar[isler2.index(y)]))
    tempstr=""
    templist2.clear()

conn.commit()

from tabulate import tabulate

cur=cur.execute('''SELECT * FROM workers  ''')
myresult = cur.fetchall()

sontable=tabulate(myresult,headers=['isim','Yapmaya_yatkın_olduğu_görevler', 'Yapacağı_görevler_Zorunlu','Kalan_görevler'], tablefmt='psql')#,showindex="always"
print(sontable)


""" from tkinter import *
window = Tk()
window.geometry("800x550")
window.title("Welcome to Workers app")
lbl1=Label(text=('henüz yapılmayan görev=',kalangorev),font=("Arial Bold", 10))
lbl = Label(window, text=sontable)
lbl1.grid(column=0, row=0)
lbl.grid(column=0, row=2)

window.mainloop() """
##################################################

from tkinter import *
from tkinter import ttk





# Create an instance of tkinter frame
win = Tk()
win.title("işlerin listesi")
# Set the size of the tkinter window
win.geometry("800x350")

# Create an object of Style widget
style = ttk.Style()
style.theme_use('winnative')#winnative#clam

# Add a Treeview widget
tree = ttk.Treeview(win, column=("isim", "Yapmaya_yatkın_olduğu_görevler", "Yapacağı_görevler_Zorunlu",'Kalan_görevler'), show='headings', height=satir)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="isim")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Yapmaya_yatkın_olduğu_görevler")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Yapacağı_görevler_Zorunlu")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="Kalan_görevler")



#tree.insert('', 'end', text="1", values=('Amit', 'Kumar', '17701'))

conn = sqlite3.connect("workers.sqlite")
cur = conn.cursor()
cur.execute("SELECT * FROM workers")
rows = cur.fetchall()
for row in rows:
    print(row)
    tree.insert("", tk.END, values=row)
    #tree.insert("", tk.END, text=row[0], values=row[1:])
conn.close()

tree.pack()

win.mainloop()
