# ===================================
#     Excelに書き出すプログラム
# pandasを使用しているので、ダウンロードがまだの方はダウンロードを先にお願いします。
# pip install pandas openxl
# ===================================

import pandas as pd

header = [1, 2, 3, 4, 5, 6]

main = [["a", "b", "c", "d", "e", "f"], ["a", "b", "c", "d", "e", "f"],
        ["a", "b", "c", "d", "e", "f"], ["a", "b", "c", "d", "e", "f"],
        ["a", "b", "c", "d", "e", "f"], ["a", "b", "c", "d", "e", "f"]]

df = pd.DataFrame(main)
with pd.ExcelWriter('./test.xlsx', mode='a') as writer:
    df.to_excel(writer, sheet_name='sheet1', index=False, header=False)
