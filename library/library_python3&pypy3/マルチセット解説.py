# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
"""
s.a
SortedSet の中身です。list の list になっていて、中には要素が昇順に並んでいます。各バケットには要素が存在することが保証されます。

len(s)
 時間

x in s / x not in s
 時間

s.add(x)
x が s に含まれていなければ x を追加し、True を返します。償却  時間

s.discard(x)
x が s に含まれていれば x を削除し、True を返します。償却  時間

s.lt(x) / s.le(x) / s.gt(x) / s.ge(x)
x より小さい / 以下 / より大きい / 以上 で 最小 / 最大 の要素を返します。存在しなければ None を返します。  時間

s[x]
下から x 番目 / 上から ~x 番目 の要素を返します。存在しない場合は IndexError を返します。  時間

s.index(x)
x より小さい要素の数を返します。x が s に含まれている場合は list(s).index(x) に相当します。  時間

s.index_right(x)
x 以下の要素の数を返します。  時間

s.add(x)

x が s に含まれているかどうかに関わらず x を追加します。償却

時間
s.discard(x)

x が s に含まれていれば x を 1 個 削除し、True を返します。償却

時間 (C++ の std::multiset::erase には x を全て削除してしまうという罠があります。)
s.count(x)

s に含まれる x の個数を返します。
時間
"""