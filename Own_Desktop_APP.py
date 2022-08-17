# Tkinterでデスクトップアプリを作成
# openpyxlやtwitterなどと組み合わせて、自分のアプリを作れる
import tkinter

class Application(tkinter.Frame):   # フレームオブジェクト作成、アプリの中身を書く
    def __init__(self, root=None):
        super().__init__(root, width=380, height=280, borderwidth=1, relief='groove')   # 横幅、高さ、境界線の太さ、境界線の種類
        self.root = root    # 引数として保存、クラス内で容易に扱える
        self.pack() # 位置設定
        self.pack_propagate(0)  # サイズ調整
        self.create_widgets()

    def create_widgets(self):   # ここに部品を追加していく
        # 閉じるボタン
        quit_btn = tkinter.Button(self) # ボタンクラスオブジェクト生成
        quit_btn['text'] = '閉じる'    # 表示させる文字
        quit_btn['command'] = self.root.destroy # ボタンに押された時の処理
        quit_btn.pack(side='bottom')    # 位置設定：下

        # テキストボックス
        self.text_box = tkinter.Entry(self)
        self.text_box['width'] = 10
        self.text_box.pack()

        # 実行ボタン
        submit_btn = tkinter.Button(self)
        submit_btn['text'] = '実行'
        submit_btn['command'] = self.input_handler()
        submit_btn.pack()

        # メッセージ出力
        self.message = tkinter.Message(self)
        self.message.pack()

    def input_handler(self):
        text = self.text_box.get()
        self.message['text'] = text + '!!'


root = tkinter.Tk() # アプリの土台
root.title('Kaniのアプリ')  # タイトル
root.geometry('400x300')    # ピクセル
app = Application(root=root)    # フレーム
app.mainloop() # 起動
