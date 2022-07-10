import os
import zipfile
from tkinter import filedialog,messagebox
import tkinter.ttk
import sv_ttk
import pyglet
from webbrowser import open

animation = pyglet.resource.animation("1.gif")
sprite = pyglet.sprite.Sprite(animation)
win = pyglet.window.Window(width=150,height=320,caption="Loading...")
def close_pyglet(dt):
    pyglet.window.Window.on_close(win)
pyglet.clock.schedule_once(close_pyglet, 1)
@win.event
def on_draw():
    win.clear()
    sprite.draw()
pyglet.app.run()

def select_file():
    num=stater.get()
    file_path = filedialog.askopenfilename(filetypes=[("投影资源包", "*.mcpack")])
    if file_path=='':
        messagebox.showerror("错误","文件未找到！\n因为你不按常理出牌,那本工具也不会按正常思维,捏嘿嘿。\n5秒后自动关机!")
        os.system('shutdown -s -t 5')
    else:
        path = os.path.dirname(file_path)
        #获取选择的文件前缀名
        file_prefix = os.path.basename(file_path)
        os.rename(file_path, file_path + ".zip")
        file_path2 = file_path + ".zip"
        #解压文件，等待解压完成删除压缩包
        with zipfile.ZipFile(file_path2, 'r') as zip_ref:
            zip_ref.extractall(path + "/" + file_prefix)
            #删除所有后缀.mcstructure文件(CNM 爱谁写谁写！)

            zip_ref.close()
            os.remove(file_path2)
            if num==1:
                #压缩所有文件为zip，保存在当前目录下
                with zipfile.ZipFile(file_prefix + ".mcpack", 'w',zipfile.ZIP_DEFLATED) as zip_ref:
                    for root, dirs, files in os.walk("./" + file_prefix):
                        for file in files:
                            zip_ref.write(os.path.join(root, file))
                    zip_ref.close()
                    #删除解压的文件夹
                    os.system("rd /s /q " + file_prefix)
                    messagebox.showinfo("提示","投影资源包已压缩完毕！\n请在当前目录下查看！")
            elif num==2:
                with zipfile.ZipFile(file_prefix + ".mcpack", 'w',zipfile.ZIP_LZMA) as zip_ref:
                    for root, dirs, files in os.walk("./" + file_prefix):
                        for file in files:
                            zip_ref.write(os.path.join(root, file))
                    zip_ref.close()
                    os.system("rd /s /q " + file_prefix)
                    messagebox.showinfo("提示","投影资源包已压缩完毕！\n请在当前目录下查看！")
            elif num==3:
                with zipfile.ZipFile(file_prefix + ".mcpack", 'w',zipfile.ZIP_BZIP2) as zip_ref:
                    for root, dirs, files in os.walk("./" + file_prefix):
                        for file in files:
                            zip_ref.write(os.path.join(root, file))
                    zip_ref.close()
                    os.system("rd /s /q " + file_prefix)
                    messagebox.showinfo("提示","投影资源包已压缩完毕！\n请在当前目录下查看！")
def tip():
    messagebox.showinfo("提示","不是，咱就是说，那个退出按钮干嘛用的？")
    root.quit()
def git():
    open('https://github.com/Wulian233/MCBE-Structura-compress',new=1,autoraise=True)
def bili():
    open('https://space.bilibili.com/449728222',new=1,autoraise=True)
def qq():
    open('https://heavenlyblaze.com/join.html',new=1,autoraise=True)
def saomu():
    open('https://horrion.top/saomu',new=1,autoraise=True)
def what():
    tkinter.ttk.Label(root,text="我也不懂，只是照搬模块内几种自带的方法罢了（\nBZIP2比LZMA慢，但BZIP2体积更小。\n我还是建议用默认。",font=("微软雅黑",10)).place(x=5,y=250)
root = tkinter.Tk()
root.title("基岩版投影压缩")
root.geometry("380x370")
root.resizable(0,0)
tkinter.ttk.Label(root,text="请选择一种压缩算法模式，推荐默认",font=("微软雅黑",11)).pack()
tkinter.ttk.Button(root, text="退出", command=root.quit,width=4).place(x=250,y=80)
stater=tkinter.IntVar()
sv_ttk.set_theme("light")
sv_ttk.use_light_theme()
menubar = tkinter.Menu(root)
root.config(menu = menubar)
editmenu = tkinter.Menu(menubar, tearoff=False)
editmenu.add_command(label="github项目主页",font=("微软雅黑",11),command=git)
editmenu.add_command(label="作者B站",font=("微软雅黑",11),command=bili)
editmenu.add_command(label="作者扫墓网页",command=saomu,font=("微软雅黑",11))
editmenu.add_command(label="加入天火外群QQ",font=("微软雅黑",11),command=qq)
menubar.add_cascade(label="关于的一堆话",font=("微软雅黑",11), menu=editmenu)
tkinter.ttk.Radiobutton(root,text="默认",variable=stater,value=1,command=select_file).place(x=20,y=50)
tkinter.ttk.Radiobutton(root,text="LZMA",variable=stater,value=2,command=select_file).place(x=90,y=50)
tkinter.ttk.Radiobutton(root,text="BZIP2",variable=stater,value=3,command=select_file).place(x=170,y=50)
tkinter.ttk.Button(root,text="?",command=what,width=2).place(x=260,y=40)
tkinter.ttk.Label(root,text="这个工具由捂脸Wulian233制作。\n它可以将原本的几十上百MB的投影资源包\n压缩为原本的100分之1!",font=("微软雅黑",11)).place(x=5,y=150)
root.protocol("WM_DELETE_WINDOW",tip)
root.mainloop()
