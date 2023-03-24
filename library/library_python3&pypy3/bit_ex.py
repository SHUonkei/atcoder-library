# ここのサイトでやった　https://qiita.com/gogotealove/items/11f9e83218926211083a
money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)
for i in range(2 ** n):
    bag = [] #bagを初期化　
    tot = 0
    for j in range(n):
        if ((i >> j) & 1): #iをj回シフトして、1か判定
            bag.append(item[j][0]) #append でリストに要素を追加、[j][0]は[行][文字側か数字側か]
            tot += item[j][1]
    if tot <= money: # <にしていてめっちゃエラー出た。。
        print(tot, bag)
    #print("pattern{}:".format(i), end="") #printのなかにこの,end"で次のprintを改行せずにつなげて出力する役割がある。
    #print(bag)