#ライブラリーのインポート
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re

# ローマ数字の入力が正しいかどうかをチェック
def validate_roman(roman):
    # ローマ数字の正規表現
    pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    # ローマ数字の正規表現にマッチするかどうかをチェック
    return bool(re.match(pattern, roman))

# ローマ数字を整数に変換
def main(roman):
    # 変換結果を格納する変数
    num = 0
    # ローマ数字の文字と整数の対応表
    r_n = {'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    # 前の文字の整数
    pre = 0
    
    # ローマ数字の入力が正しいかどうかをチェック
    if not validate_roman(roman):
        raise Exception('ローマ数字の表記ルールをご確認ください: {}'.format(roman))

    # ローマ数字を整数に変換
    for i in range(len(roman) - 1, -1, -1):
        c = roman[i]
        # ローマ数字に使われていない文字が含まれていないかチェック
        if not c in r_n:
            raise Exception('Invalid character in Roman numeral: {}'.format(c))
        # ローマ数字の文字を整数に変換
        n = r_n[c]
        if n >= pre:
            num += n
            pre = n
        # ローマ数字の文字の並びが正しいかどうかをチェック
        else:
            if (pre == 10 and n == 1 and c != "I") or (pre == 100 and n == 10 and c != "X") or (pre == 1000 and n == 100 and c != "C"):
                raise Exception('Invalid order in Roman numeral: {}'.format(roman))
            num -= n
    return num

# 「変換」ボタンをクリックしたときの動作
def convert_roman_to_int():
    romans = entry.get()
    romans = romans.replace(" ", "").upper()  # 入力から空白を除去し、大文字に変換
    # 最後がカンマで終わっている場合は、それを削除する
    if romans.endswith(","):
        romans = romans[:-1]

    roman_list = romans.split(",")  # カンマで分割
    
    # 一度に変換できるローマ数字は5つまで
    if len(roman_list) > 5:
        messagebox.showerror("エラー", "一度に変換できるローマ数字は5つまでです。")
        return
    
    # 結果表示ラベルを初期化
    result_label["text"] = "結果: \n"

    try:
        for roman in roman_list:
            num = main(roman)
            result_label["text"] += roman + " → " + str(num) + "\n"
            add_to_history(roman, num)
    except Exception as e:
        messagebox.showerror("エラー", e)

# 履歴に追加
def add_to_history(roman, num):
    global history  # global変数を使用することを明示
    # 履歴に追加
    history.insert(0, (roman, num))
    # 履歴が5つ以上になったら、古い履歴を削除
    history = history[:5]
    # 履歴ラベルを更新
    update_history_labels()

# 履歴ラベルを更新
def update_history_labels():
    for i in range(5):
        if i < len(history):
            labels[i]['text'] = "履歴{}: {} → {}".format(i+1, history[i][0], history[i][1])
        else:
            labels[i]['text'] = "履歴{}: ".format(i+1)


# GUIの生成
root = tk.Tk()
root.title("Roman Numeral → Integer Number")
root.geometry("400x950")
root.minsize(400, 950)

# 履歴を格納するリスト
history = []

# 履歴ラベル
labels = [tk.Label(root, text="履歴{}: ".format(i+1)) for i in range(5)]

# ロゴラベル
logo_label = tk.Label(root, text="ROMAN\nNUMERAL\nCONVERTER", 
                      font=("Helvetica", 16, "bold"),
                      justify='center',
                      borderwidth=2, 
                      relief="solid")
logo_label.pack(padx=10, pady=10)

# 説明ラベル
description_label = tk.Label(root, text="ローマ数字を入力してください。")
description_label.pack()

# ローマ数字入力欄
entry = tk.Entry(root)
entry.insert(0, "")
entry.pack()

# 変換ボタン
convert_button = tk.Button(root, 
                           text="変換", 
                           command=convert_roman_to_int)
convert_button.pack()

# 結果表示ラベル
result_label = tk.Label(root, 
                        fg="blue", 
                        font=("Helvetica", 16, "bold"),
                        text="結果: ")
result_label.pack()

# 履歴表示ラベル
for label in labels:
    label.pack()

#区分け
separate_label = tk.Label(root, text="------------------------")
separate_label.pack()

# 簡易的なローマ数字と整数の対応表
table_label = tk.Label(root, text="簡易的なローマ数字と整数の対応表")
table_label.pack()

# 簡易的なローマ数字と整数の対応表を表示

tree = ttk.Treeview(root, columns=("roman", "number"), show="headings")
tree.column("roman", width=100)
tree.column("number", width=100)
tree.heading("roman", text="ローマ数字")
tree.heading("number", text="数字")

# データの追加
data = [("I", "1"), ("V", "5"), ("X", "10"), ("L", "50"), ("C", "100"), ("D", "500"), ("M", "1000")]
for i in data:
    tree.insert("", "end", values=i)
tree.pack()

#区分け
separate_label = tk.Label(root, text="------------------------")
separate_label.pack()

#ローマ数字のルール
rule_label = tk.Label(root, text="ローマ数字のルール")
rule_label.pack()

# ローマ数字のルールを左詰めで表示
rule = tk.Label(root, text= "1.基本的に数字は大きい順に並べる。\n"
                            "小さい順で並べてもよいもの[IV,IX,XC,CD,CM]"
                            "\n""\n"
                            "2. I, X, C, M は3つまで並べることができる。\n"
                            "\n"
                            "3. V, L, D は,単体で置くか,1つ前の文字の右側に置くことができる。\n"
                            "\n"
                            "4. I は V, X の前に置くことができる。\n"
                            "\n"
                            "5. X は L, C の前に置くことができる。\n"
                            "\n"
                            "6. C は D, M の前に置くことができる。\n")
rule.pack()

# GUIの起動
root.mainloop()
