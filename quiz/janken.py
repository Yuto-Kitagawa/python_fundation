import random

randamu = random.randint(0, 2)

janken = ["グー", "チョキ", "パー"]

aite = janken[randamu]

jibun = input("何を出しますか")

# 自分がグーを出したとき
if(jibun == "グー"):

    if(aite == "グー"):
        print("")

    if(aite == "チョキー"):
        print("")

    if(aite == "パー"):
        print("")

# 自分がチョキーを出したとき
if(jibun == "チョキー"):

    if(aite == "グー"):
        print("")

    if(aite == "チョキー"):
        print("")

    if(aite == "パー"):
        print("")

# 自分がパーを出したとき
if(jibun == "パー"):

    if(aite == "グー"):
        print("")

    if(aite == "チョキー"):
        print("")

    if(aite == "パー"):
        print("")
