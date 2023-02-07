# リストから削除
array = [0, 1, 2, 3, 4, 5, 6, "a", "a", "a", "a"]

# 配列の0番目を削除
array.pop(0)
print(array)  # [1, 2, 3, 4, 5, 6, "a", "a", "a", "a"]

# 一番最後の[a]を削除
array.remove('a')  # [ 1, 2, 3, 4, 5, 6, "a", "a", "a",]
print(array)
