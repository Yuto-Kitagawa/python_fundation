"""
配列のコピーの方法
copyメソッドを使わないと、他の変数に代入したとしても、もとの配列の値を変えると代入した配列の中身も変わってしまう。
"""

# リストを宣言
array = [1, 2, 3, 4, 5]

j = array
copy = array.copy()

# 配列(array)の0番目を6に変更
array[0] = 6

print(j)  # [6,2,3,4,5]    → jの中身は変えてないけど、0番目の要素が変わっている
print(copy)  # [1,2,3,4,5] → copyメソッドを使用したため、0番目の要素は変わっていない。
