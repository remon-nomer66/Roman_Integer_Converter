import tkinter as tk
from tkinter import messagebox

# ローマ数字を整数に変換する関数
def roman_to_int(roman_numeral):
    # ローマ数字の各文字に対応する整数の辞書
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    #初期化
    total = 0
    prev_value = 0

    # ローマ数字を後ろから見ていく
    for char in reversed(roman_numeral):
        # 無効な文字が含まれていたらエラーを出す
        if char not in roman_values:
            raise ValueError(f"無効なローマ数字です: {char}")
        
        # 無効な組み合わせのチェック
        invalid_combination = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM', 'IL', 'IC', 'ID', 'IM', 'VX', 'VL', 'VC', 'VD', 'VM', 'XD', 'XM', 'LC', 'LD', 'LM', 'DM']
        for combination in invalid_combination:
            if combination in roman_numeral:
                raise ValueError(f"このローマ数字は有効ではありません: {combination}")
            
        # 現在の文字の値を取得
        value = roman_values[char]
        # 現在の文字の値が前の文字の値以上ならば足し合わせる
        if value >= prev_value:
            total += value
        # 現在の文字の値が前の文字の値より小さければ引き算を行う
        else:
            total -= value
        # 現在の文字の値をprev_valueに代入
        prev_value = value

    # 結果を返す
    return total

# 「変換」ボタンをクリックしたときの動作
def convert_roman_to_int():
    # ローマ数字を整数に変換して結果を表示
    try:
        roman_numeral = entry.get()
        number = roman_to_int(roman_numeral)
        result_label['text'] = f"結果: {number}"
    # エラーが発生したらメッセージボックスを表示
    except ValueError:
        messagebox.showerror("エラー", "正しいローマ数字を入力してください。I, V, X, L, C, D, M の文字を使用します。")

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
