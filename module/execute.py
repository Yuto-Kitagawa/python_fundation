"""
__name__についてのプログラム
pythonを実行するときのファイルの__name__は__main__が格納される。
他のファイルをモジュールとして呼び出した時は、その呼出したファイル名が格納される
他のファイルを呼び出すときはファイル名をimportする
"""

import sample
#sampleFunc()では、sampleファイルでの__name__を表示させている
sample.sampleFunc()


#実行するファイルの__name__を表示させている
print(__name__)


