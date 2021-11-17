from ast import Str
from tkinter import* 
import random
from tkinter import font 

# Tạo cửa sổ 
keobuabao = Tk() 
keobuabao.geometry('400x400')
keobuabao.resizable(0, 0)
keobuabao.title('Trò chơi kéo búa bao')
keobuabao.config(bg='seashell3')

# Tiêu đề 
Label(keobuabao, text='Kéo, Búa, Bao', font='arial 20 bold', bg='seashell2').pack()

# Lựa chọn của người chơi
nguoi = StringVar() 
Label(keobuabao, text='Hãy chọn 1: Kéo, Búa, Bao', font='arial 15 bold', bg='seashell2').place(x=70, y=70)
Entry(keobuabao, font='arial 15', textvariable=nguoi, bg='antiquewhite2').place(x=90, y=130)

# Lựa chọn của máy
may = random.randint(1,3)
if may == 1: 
    may = 'Búa'
elif may == 2: 
    may = 'Bao'
else: 
    may = 'Kéo'

# Hàm để thực thi trò chơi
ketqua = StringVar()
def choi(): 
    nguoichoi = nguoi.get() 
    if nguoichoi == may: 
        ketqua.set('Hoà nhau nha, máy cũng chọn giống bạn')
    elif nguoichoi == 'Búa' and may == 'Bao': 
        ketqua.set('Bạn thua rồi! Máy chọn Bao')
    elif nguoichoi == 'Búa' and may == 'Kéo': 
        ketqua.set('Bạn thắng rồi! Máy chọn Kéo')
    elif nguoichoi == 'Bao' and may == 'Kéo': 
        ketqua.set('Bạn thua rồi! Máy chọn Kéo')
    elif nguoichoi == 'Bao' and may == 'Búa': 
        ketqua.set('Bạn thắng rồi! Máy chọn Búa')
    elif nguoichoi == 'Kéo' and may == 'Búa': 
        ketqua.set('Bạn thua rồi! Máy chọn Búa')
    elif nguoichoi == 'Kéo' and may == 'Bao': 
        ketqua.set('Bạn thắng rồi! Máy chọn Bao')
    else: 
        ketqua.set('Không hợp lệ! Hãy chọn một: Kéo, Búa, Bao')
                   
# Thoát trò chơi
def thoat(): 
    keobuabao.destroy()

# Tạo nút nhấn
Entry(keobuabao, font='arial 10 bold', textvariable=ketqua, bg='antiquewhite2', width=50).place(x=25, y=250)
Button(keobuabao, font='arial 13 bold', text='CHƠI', padx=5, bg='seashell4', command=choi).place(x=150, y=190)
Button(keobuabao, font='arial 13 bold', text='THOÁT', padx=5, bg='seashell4', command=thoat).place(x=150, y=310)

keobuabao.mainloop()