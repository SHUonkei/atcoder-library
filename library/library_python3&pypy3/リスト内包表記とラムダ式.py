n = [111,222,333,444,555]

for i in range(5):
    print( i :lambda x: n[x])
    

"リスト内包表記の for 文は処理したい式を先頭に書いて、[] で囲うだけ"

"[処理 for 変数名 in イテラブルオブジェクト] "
double = [i*2 for i in range(5)]
print(double)


"[処理 for 変数名 in イテラブルオブジェクト if 条件式] "
odds = [i for i in range(10) if i % 2 == 1]
print(odds)

"以下の書き方はダメ"
"odds = [i if i % 2 == 1 for i in range(10) ]"
"print(odds)"

"[条件式が True のときの処理 if 条件式 else 条件式が False のときの処理 for 変数名 in イテラブルオブジェクト] "
odd10 = [i * 10 if i % 2 == 1 else i for i in range(10)]
print(odd10)
