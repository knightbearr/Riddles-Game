# ---IMPORT PACKAGE---
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame
from pygame import mixer

# ---SETTING TKINTER---
root = Tk()
root.title('A Simple Riddles Game')
root.geometry('500x700')
root.iconbitmap("icon.ico")

# ---IMPORT PYGAME AS BACKSOUND---
pygame.mixer.init()
mixer.music.load('audio.mp3')
mixer.music.play(-1)

# ---CREATE AND EXPORT IMAGE BACKGROUND AS LABEL---
bg1 = PhotoImage(file='1.png')
lbl1 = Label(root, image=bg1)
lbl1.place(x=0, y=0)


# ---CREATE A FUNCTION FOR BUTTON MUSIC---
def music():
    music.load('audio.mp3')
    music.play(-1)


def music2():
    music.load('audio2.mp3')
    music.play(-1)


def stopmusic():
    mixer.music.stop()


# ---CREATE A FUNCTION FOR BUTTON PILIH---
def pilih():
    global img

    # ---SET NEW WINDOW---
    root2 = Toplevel()
    root2.title('A Simple Riddles Game')
    root2.geometry('500x700')

    # ---SET BACKGROUND---
    img = PhotoImage(file='1.png')
    lbl2 = Label(root2, image=img)
    lbl2.place(x=0, y=0)

    # ---FUNCTION---
    def soall1():
        go = soal1
        game = root2.destroy
        go()
        game()

    def soall2():
        go = soal2
        game = root2.destroy
        go()
        game()

    def soall3():
        go = soal3
        game = root2.destroy
        go()
        game()

    def soall4():
        go = soal4
        game = root2.destroy
        go()
        game()

    def kembali():
        game = root2.destroy
        game()

    # ---SET BUTTON---
    button1 = Button(root2, text='SOAL 1', bg='brown', fg='white', bd=0, font=('Helevatica 10 bold'), padx=120, pady=10,
                     command=soall1)
    button2 = Button(root2, text='SOAL 2', bg='brown', fg='white', bd=0, font=('Helevatica 10 bold'), padx=120, pady=10,
                     command=soall2)
    button3 = Button(root2, text='SOAL 3', bg='brown', fg='white', bd=0, font=('Helevatica 10 bold'), padx=120, pady=10,
                     command=soall3)
    button4 = Button(root2, text='SOAL 4', bg='brown', fg='white', bd=0, font=('Helevatica 10 bold'), padx=120, pady=10,
                     command=soall4)
    button5 = Button(root2, text="Kembali", padx=20, pady=5, bd=0, command=kembali, bg="aqua", fg="black")

    # ---DEFINE BUTTON---
    button1.place(x=105, y=280)
    button2.place(x=105, y=340)
    button3.place(x=105, y=400)
    button4.place(x=105, y=460)
    button5.place(x=0, y=0)


# ---CREATE A FUNCTION FOR SOAL 1 - 4---
def soal1():
    global img1
    # ---SET NEW WINDOW---
    root1 = Toplevel()
    root1.title('A Simple Riddles Game')
    root1.geometry('500x700')

    # ---SET BACKGROUND---
    img1 = PhotoImage(file='2.png')
    lbl2 = Label(root1, image=img1)
    lbl2.place(x=0, y=0)

    # ---SET ENTRY LABEL---
    e = Entry(root1, width=50, bg="white")
    e.place(x=110, y=340)
    e.insert(0, "Masukkan jawaban anda disini ^-^")

    def soall1():
        hello = e.get().lower()

        if hello == 'katak beradik':
            messagebox.askokcancel('Info', 'Jawaban anda benar ^-^')
            go = pilih
            game = root1.destroy
            go()
            game()
        else:
            messagebox.askokcancel('Info', 'Jawaban anda salah T_T')
            go = soal1
            game = root1.destroy
            go()
            game()

    def kembali1():
        go = pilih
        game = root1.destroy
        go()
        game()

    button1 = Button(root1, text="Cek Jawaban", padx=100, pady=10, bd=0, command=soall1, bg="brown", fg="white")
    button2 = Button(root1, text="Kembali", padx=20, pady=5, bd=0, command=kembali1, bg="aqua", fg="black")
    button1.place(x=122, y=420)
    button2.place(x=0, y=0)


def soal2():
    global img2

    # ---SET NEW WINDOW---
    root2 = Toplevel()
    root2.title('A Simple Riddles Game')
    root2.geometry('500x700')

    # ---SET BACKGROUND---
    img2 = PhotoImage(file='3.png')
    lbl3 = Label(root2, image=img2)
    lbl3.place(x=0, y=0)

    # ---SET ENTRY LABEL---
    e = Entry(root2, width=50, bg="white")
    e.place(x=110, y=340)
    e.insert(0, "Masukkan jawaban anda disini ^-^")

    def soall2():
        hello = e.get().lower()

        if hello == 'sabun colek':
            messagebox.askokcancel('Info', 'Jawaban anda benar ^-^')
            go = pilih
            game = root2.destroy
            go()
            game()
        else:
            messagebox.askokcancel('Info', 'Jawaban anda salah T_T')
            go = soal2
            game = root2.destroy
            go()
            game()

    def kembali2():
        go = pilih
        game = root2.destroy
        go()
        game()

    button1 = Button(root2, text="Cek Jawaban", padx=100, pady=10, bd=0, command=soall2, bg="brown", fg="white")
    button2 = Button(root2, text="Kembali", padx=20, pady=5, bd=0, command=kembali2, bg="aqua", fg="black")
    button1.place(x=122, y=420)
    button2.place(x=0, y=0)


def soal3():
    global img3

    # ---SET NEW WINDOW---
    root3 = Toplevel()
    root3.title('A Simple Riddles Game')
    root3.geometry('500x700')

    # ---SET BACKGROUND---
    img3 = PhotoImage(file='4.png')
    lbl4 = Label(root3, image=img3)
    lbl4.place(x=0, y=0)

    # ---SET ENTRY LABEL---
    e = Entry(root3, width=50, bg="white")
    e.place(x=110, y=340)
    e.insert(0, "Masukkan jawaban anda disini ^-^")

    def soall3():
        hello = e.get().lower()

        if hello == '13 gajah':
            messagebox.askokcancel('Info', 'Jawaban anda benar ^-^')
            go = pilih
            game = root3.destroy
            go()
            game()
        else:
            messagebox.askokcancel('Info', 'Jawaban anda salah T_T')
            go = soal3
            game = root3.destroy
            go()
            game()

    def kembali3():
        go = pilih
        game = root3.destroy
        go()
        game()

    button1 = Button(root3, text="Cek Jawaban", padx=100, pady=10, bd=0, command=soall3, bg="brown", fg="white")
    button2 = Button(root3, text="Kembali", padx=20, pady=5, bd=0, command=kembali3, bg="aqua", fg="black")
    button1.place(x=122, y=420)
    button2.place(x=0, y=0)


def soal4():
    global img4

    # ---SET NEW WINDOW---
    root4 = Toplevel()
    root4.title('A Simple Riddles Game')
    root4.geometry('500x700')

    # ---SET BACKGROUND---
    img4 = PhotoImage(file='5.png')
    lbl5 = Label(root4, image=img4)
    lbl5.place(x=0, y=0)

    # ---SET ENTRY LABEL---
    e = Entry(root4, width=50, bg="white")
    e.place(x=110, y=340)
    e.insert(0, "Masukkan jawaban anda disini ^-^")

    def soall4():
        hello = e.get().lower()

        if hello == 'buah naga':
            messagebox.askokcancel('Info', 'Jawaban anda benar ^-^')
            go = pilih
            game = root4.destroy
            go()
            game()
        else:
            messagebox.askokcancel('Info', 'Jawaban anda salah T_T')
            go = soal4
            game = root4.destroy
            go()
            game()

    def kembali4():
        go = pilih
        game = root4.destroy
        go()
        game()

    button1 = Button(root4, text="Cek Jawaban", padx=100, pady=10, bd=0, command=soall4, bg="brown", fg="white")
    button2 = Button(root4, text="Kembali", padx=20, pady=5, bd=0, command=kembali4, bg="aqua", fg="black")
    button1.place(x=122, y=420)
    button2.place(x=0, y=0)


# ---CREATE A BUTTON---
btn1 = Button(root, text='Start Game', font=('Helevatica 10 bold'), bg='orange', pady=15, padx=100, bd=0, command=pilih)
btn2 = Button(root, text='Exit Game', font=('Helevatica 10 bold'), bg='orange', pady=15, padx=100, bd=0,
              command=root.quit)
btn3 = Button(root, text='Ikson Music', font=('Helevatica 7 bold'), bg='aqua', pady=5, padx=20, bd=0, command=music)
btn4 = Button(root, text='Stop Music', font=('Helevatica 7 bold'), bg='aqua', pady=5, padx=20, bd=0, command=stopmusic)
btn5 = Button(root, text='Tiesto Music', font=('Helevatica 7 bold'), bg='aqua', pady=5, padx=20, bd=0, command=music2)

# ---DEFINE THE BUTTON---
btn1.place(x=110, y=340)
btn2.place(x=112, y=420)
btn3.place(x=0, y=0)
btn4.place(x=408, y=0)
btn5.place(x=80, y=0)

# ---MESSAGE BUTTON---
messagebox.askokcancel('Info Permainan', 'Selamat bermain... ^-^')

# ---MAINLOOP---
root.mainloop()
