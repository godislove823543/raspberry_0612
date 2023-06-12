import tkinter as tk
#toolkit interface 圖形使用者介面工具包 

#window繼承tk
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('我的GUI') #self.xx 繼承tk的功能
        self.geometry('380x400')
        self.resizable(False,False)
        #查tk reference 的type fonts
        title_label=tk.Label(self,text="LED控制器",font=('Helvetica','16')
        )
        title_label.pack(pady=25)

        led_btn=tk.Button(self,text="LED 開",font=('Helvetica','16'),padx=20,pady=20)
        led_btn.pack(pady=(10,50))

if __name__=="__main__": #只在運行這個py檔案時執行
    window=Window() #創建window類 視窗物件
    window.mainloop() #事件迴圈 使用者輸入(按按鈕)時 執行相應的動作
