# ******文字の切り取り(スライス)******
array = [0, 1, 2, 3, 4, 5, 6] # リストを宣言

print(array[0:7]) # リストの0番目から7番目まで表示
print(array[4:7]) # リストの4番目から7番目まで表示


print("あいうえおかきくけこ"[:4]) # 最初から4番目までが表示される(前の部分が省略されていると0が入る)
print("あいうえおかきくけこ"[4:]) # 最初から4番目までが表示される(後ろの部分が省略されていると配列の最後の数値が入る)