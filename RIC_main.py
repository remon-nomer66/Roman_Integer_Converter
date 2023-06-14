import tkinter as tk
from tkinter import messagebox
import re

def validate_roman(roman):
    pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    return bool(re.match(pattern, roman))

def main(roman):
    num = 0
    r_n = {'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    pre = 0
    
    # validate roman numeral
    if not validate_roman(roman):
        raise Exception('Invalid Roman numeral: {}'.format(roman))

    for i in range(len(roman) - 1, -1, -1):
        c = roman[i]
        if not c in r_n:
            raise Exception('Invalid character in Roman numeral: {}'.format(c))
        n = r_n[c]
        if n >= pre:
            num += n
            pre = n
        else:
            if (pre == 10 and n == 1 and c != "I") or (pre == 100 and n == 10 and c != "X") or (pre == 1000 and n == 100 and c != "C"):
                raise Exception('Invalid order in Roman numeral: {}'.format(roman))
            num -= n
    return num

# 「変換」ボタンをクリックしたときの動作
def convert_roman_to_int():
    roman = entry.get()
    try:
        num = main(roman)
        result_label["text"] = "結果: " + str(num)
    except Exception as e:
        messagebox.showerror("エラー", e)

# GUIの生成
root = tk.Tk()
root.title("Roman Numeral → Integer Number")
root.geometry("300x600")

# ロゴ
logo = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(root, image=logo)
logo_label.pack()

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

#区分け
separate_label = tk.Label(root, text="------------------------")
separate_label.pack()

# 簡易的なローマ数字と整数の対応表
table_label = tk.Label(root, text="ローマ数字と整数の対応表")
table_label.pack()

# ローマ数字と整数の対応表を表示
table = tk.Text(root, height=10, width=20)
table.insert(tk.END, "I: 1\n")
table.insert(tk.END, "V: 5\n")
table.insert(tk.END, "X: 10\n")
table.insert(tk.END, "L: 50\n")
table.insert(tk.END, "C: 100\n")
table.insert(tk.END, "D: 500\n")
table.insert(tk.END, "M: 1000\n")
table.pack()

#区分け
separate_label = tk.Label(root, text="------------------------")
separate_label.pack()

#ローマ数字のルール
rule_label = tk.Label(root, text="ローマ数字のルール")
rule_label.pack()

# ローマ数字のルールを表示
rule = tk.Text(root, height=10, width=60)
rule.insert(tk.END, "1. I, X, C, M は3つまで並べることができる。\n")
rule.insert(tk.END, "2. V, L, D は1つ前の文字の右側にしか置くことができない。\n")
rule.insert(tk.END, "3. I は V, X の前に置くことができる。\n")
rule.insert(tk.END, "4. X は L, C の前に置くことができる。\n")
rule.insert(tk.END, "5. C は D, M の前に置くことができる。\n")
rule.pack()

# GUIの起動
root.mainloop()
