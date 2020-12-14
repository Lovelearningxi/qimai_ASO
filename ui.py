import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
from js_decode_2 import indexshow
from js_decode_2 import opentext
from showplot import show

# 主体
window = tk.Tk()
window.title("王玺一拖二 —— 数据分析")
screenWidth = window.winfo_screenwidth()  # 获取显示区域的宽度
screenHeight = window.winfo_screenheight()  # 获取显示区域的高度
width = 800  # 设定窗口宽度
height = 540  # 设定窗口高度
left = (screenWidth - width) / 2
top = (screenHeight - height) / 2
window.geometry("%dx%d+%d+%d" % (width, height, left, top)) #窗口大小

# 申请所需变量
on_word = False #按钮初始状态
on_char = False
on_img = False
c = ""
v = ""

# 判断信息是否填写完成
def empty():
    if appName.get() == "" or str(item.get()) == "":
        return True
# 选择国家和版本号
def go(type):   #处理事件
    global c,v
    if type == "country":
        c = comboxcountry.get()
    elif type == "version":
        v = comboxversion.get()
    else:
        print("出问题了！！！")
# 处理"查询高指数关键词"
def find_word():
    global on_word
    flag = empty()
    if on_word == False:
        if flag != True:
            on_word = True
            resultword = indexshow(appName.get(),c,int(item.get()))
            for word in resultword:
                a ="↑【{:<45s}{}{}】".format(str(word[1])+"】","【",str(word[0]))
                showword.insert("insert", a)

                showword.insert("insert", "\n")
        else:
            tk.messagebox.showwarning(title = "Hi!", message = "信息没填完哦!")
    else:
        on_word = False
        
        showword.delete(1.0,END)
# 处理"查询高频字"
def find_char():
    global on_char
    flag = empty()
    if on_char == False:
        if flag != True:
            on_char = True
            resultchar = opentext()
            for i in range(int(item.get())):
                b ="*【{:<45s}{}{}】".format(str(resultchar[i][1])+"】","【",str(resultchar[i][0]))
                showchar.insert("insert", b)
                showchar.insert("insert", "\n")
        else:
            tk.messagebox.showwarning(title = "警告!", message = "信息没填完哦!")
    else:
        on_char = False
        showchar.delete(1.0,END)




# 标签
lb = Label(window,text='App store Optimization', fg='black',
        font=('华文新魏',20), width=20, height=2, relief=FLAT)

lb.pack()

# 国家
tk.Label(window, text = '选择国家:').place(x=150,y=70) # 提示
country=tkinter.StringVar()# 窗体自带的文本，新建一个值
comboxcountry=ttk.Combobox(window,textvariable=country) # 初始化
comboxcountry["values"]=("cn","us","uk")
comboxcountry.current(0)  # 选择第一个
comboxcountry.bind("<<ComboboxSelected>>",go("country"))  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
comboxcountry.place(x=210,y=70)
# 版本
tk.Label(window, text = '选择版本:').place(x=410,y=70)
version=tkinter.StringVar()
comboxversion=ttk.Combobox(window,textvariable=version)
comboxversion["values"]=("IOS12","IOS12","IOS12","IOS12")
comboxversion.current(0)
comboxversion.bind("<<ComboboxSelected>>",go("version"))  
comboxversion.place(x=470,y=70)
# app
tk.Label(window, text = '您需要查询的app:').place(x=150,y=110)
appName = tk.Entry(window,width=15)
appName.place(x=255,y=110)
a = appName.get()

# 条数
tk.Label(window, text = '您需要的查询结果条数:').place(x=410,y=110)
item = tk.Entry(window,show = None, width=5)
item.place(x=545,y=110)
i = item.get()


# "高指数关键词"按钮
btnword = tk.Button(window, text = "查询高指数关键词", width = 14,
                height = 1, command = find_word)
btnword.place(x=680,y=165)
# 展示"高指数关键词"的文本框
word = tk.StringVar()
showword = tk.scrolledtext.ScrolledText(window,height=5)
showword.place(x=75,y=150)

# "高频字"按钮
btnchar = tk.Button(window, text = "查询高频字", width = 14,
                height = 1, command = find_char)
btnchar.place(x=680,y=245)
# 展示"高频字"的文本框
char = tk.StringVar()
showchar = tk.scrolledtext.ScrolledText(window,height=5)
showchar.place(x=75,y=230)

# 处理"查询高频字"
def show_img():
    global on_img
    flag = empty()
    if on_img == False:
        if flag != True:
            on_img = True
            show()
            load = Image.open(r"img/img1.png")
            render= ImageTk.PhotoImage(load)
            img = Label(window,image=render)
            img.image = render
            img.place(x=130,y=320)
        else:
            tk.messagebox.showwarning(title = "警告!", message = "信息没填完哦!")
    else:
        on_img = False

# 词云
load = Image.open(r"img/loading.jpg")
render= ImageTk.PhotoImage(load)
img = Label(window,image=render)
img.image = render
img.place(x=127,y=317)
# 展示词云
btnimg = tk.Button(window, text = "展示词云", width = 14,
                height = 1, command = show_img)
btnimg.place(x=600,y=400)



window.mainloop() #刷新窗口