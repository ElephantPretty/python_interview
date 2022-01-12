# 正则表达式 数据匹配 属于CPU密集型
import re
import tkinter as tk
# url地址解析 这个我需要了解 urllib.parse - 解析 URL urllib.request - 打开和读取 URL
from urllib import parse
# 消息盒子 看起来像是GUI里面的东西
import tkinter.messagebox as msgbox
# 控制浏览器
import webbrowser


# https://www.bilibili.com/video/BV1GA411H7Nr
class App():
    """
    重写构造函数,被称为魔术方法
    什么是魔术方法？
    在Python中，所有以双下划线 __ 包起来的方法，统称为 Magic Method（魔术方法）
    """
    def __init__(self, width=500, height=300):
        # 创建自定义类熟悉
        self.w = width
        self.h = height
        # 软件名称
        self.title = '视频解析助手'
        # tk对象 可以使用tk创建一个界面 这个和我练习的目的无关
        self.root = tk.Tk(className=self.title)
        # 变量接受用户输入的电影地址，并且对地址做处理
        """
       url-地址是字符串-表示视频老师过于基础  
       """
        self.url = tk.StringVar()# StringVar()是专门接收字符串的
        # 控制单选框默认选中的属性框
        self.v = tk.IntVar()
        self.v.set(1)
        # 软件空间划分
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        # 软件控件内容设置
        group = tk.Label(frame_1, text='播放通道:', padx=10, pady=10)
        tb = tk.Radiobutton(frame_2, text='唯一通道', variable=self.v, value=1, width=10, height=3)

        label = tk.Label(frame_2, text='请输入视频播放地址:')
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1,width=30)
        play = tk.Button(frame_2, text='播放', font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)

        # 控件布局
        # 激活空间
        frame_1.pack()
        frame_2.pack()
        # 位置确定
        group.grid(row=0, column=0)
        tb.grid(row=1, column=1)
        """
        空间2的控件位置无需看空间1的位置
        空间与空间之间是独立的
        """
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        play.grid(row=0, column=2, ipadx=10, ipady=10)
    # 定义播放按钮的事件函数
    """
    解析电影
    """
    def video_play(self):
        # 第三方播放解析api，我还以为是调python内部的解析呢！
        port = 'http://www.wmxz.wang/video.php?url='
        # 判断用户输入的电影地址是否合法?
        # https://www.iqiyi.com/v_19rr7ram14.html 粤语版-爱奇艺
        if re.match(r'https?:/{2}\w.+$', self.url.get()):
            ip = self.url.get()
            ip = parse.quote_plus(ip)
            # 自动打开浏览器
            webbrowser.open(port + ip)
        else:
            msgbox.showerror(title='错误', message='视频地址无效，请重新输入。。。')

    """
    如何启动软件
    """
    def loop(self):
        # tkinter里面的知识-我不关心
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.loop()