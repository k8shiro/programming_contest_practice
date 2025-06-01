# ソート済みリスト
from sortedcontainers import SortedList

sl = SortedList()

sl.add(5)
sl.add(2)
sl.add(7)

print(sl)  # => SortedList([2, 5, 7])

# 二分探索的な操作も可能
print(sl.bisect_left(5))   # => 1 （5以上の最初の位置）
print(sl.bisect_right(5))  # => 2 （5より大きい最初の位置）

# 削除
sl.remove(5)
print(sl)  # => SortedList([2, 7])

# インデックスアクセス
print(sl[0])  # => 2

# 要素数
print(len(sl))  # => 2

# ソート済み辞書
from sortedcontainers import SortedDict

sd = SortedDict()
sd['banana'] = 3
sd['apple'] = 5
sd['cherry'] = 1

print(sd)  # => SortedDict({'apple': 5, 'banana': 3, 'cherry': 1})
print(sd.keys())  # => SortedKeysView(['apple', 'banana', 'cherry'])


# ソート済みセット
from sortedcontainers import SortedSet

ss = SortedSet([5, 3, 1])
print(ss)  # => SortedSet([1, 3, 5])
ss.add(4)
print(ss)  # => SortedSet([1, 3, 4, 5])
