import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox

# 記錄鍵盤按鍵
key = ""
def key_down(e):
    global key
    key = e.keysym  # 記錄按下的按鍵

def key_up(e):
    global key
    key = ""   # 鍵放開時清除記錄

# 角色初始位置
mx = 1
my = 1
yuka=0   # 記錄已塗色的地板數量
def main_proc():
    global mx, my, yuka

    #重置遊戲
    if key == "Shift_L" and yuka>1:
        canvas.delete("PAINT")
        mx=1
        my=1
        yuka=0
        for y in range(7):
            for x in range(10):
                if maze[y][x]==2:
                    maze[y][x]=0

    # 依照按鍵移動角色（只能移動到 0 的位置）
    if key == "Up" and maze[my-1][mx] == 0:
        my -= 1
    if key == "Down" and maze[my+1][mx] == 0:
        my += 1
    if key == "Left" and maze[my][mx-1] == 0:
        mx -= 1
    if key == "Right" and maze[my][mx+1] == 0:
        mx += 1
    if maze[my][mx]==0:
        maze[my][mx]=2
        yuka=yuka+1
        canvas.create_rectangle(mx*80,my*80,mx*80+79,my*80+79,fill="pink",width=0,tag="PAINT")

    # 重新繪製角色
    canvas.delete("cat")
    canvas.create_image(mx*80+40,my*80+40,image=tk_img,tag="cat")

    if yuka==30:
        canvas.update()
        tkinter.messagebox.showinfo("恭喜!","所有地板都塗色了")
    else:
        root.after(300, main_proc)

# 初始化 Tkinter 視窗 
root = tk.Tk()
root.title("塗滿迷宮地板")
# 綁定鍵盤事件
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
#創建畫布
canvas = tk.Canvas(width=800, height=560, bg="white")
canvas.pack()

#迷宮地圖
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x*80, y*80, x*80+79, y*80+79, fill="skyblue", width=0)

# 使用 Pillow 加載圖像
img_path = "nini.png"  
pil_img = Image.open(img_path)
# 調整圖像大小(寬度 80，高度 80)
new_size = (80, 80)
pil_img_resized = pil_img.resize(new_size, Image.LANCZOS)
# 將 Pillow 圖像物件轉換為 Tkinter 相容的圖像物件
tk_img = ImageTk.PhotoImage(pil_img_resized)
# 確保圖像物件不被垃圾回收
canvas.create_image(mx*80+40, my*80+40, image=tk_img, tag="cat")

# 啟動遊戲
main_proc()
root.mainloop()
