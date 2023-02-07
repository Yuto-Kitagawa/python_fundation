"""
pythonを実行する際に、引数を指定することができる。
引数を指定できることによって、bashファイルなど外部からpythonに値を格納することができる(他のプログラムと連携がスムーズになる)

python argv.py Hello World

"""

import sys

for i in range(len(sys.argv)):
    print(sys.argv[i])