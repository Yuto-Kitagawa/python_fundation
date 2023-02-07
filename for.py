# ======================================
#               重要
# 　　　　　　　 for文
# =====================================

# 回数を指定して繰り返したいときに使用します。

number = 5 # 繰り返す回数を代入
for i in range(number): #range()の中に数値を入れるとその分だけ繰り返し処理が行われます)
    print(i)


"""
# 文章の中に、句読点が何個あるかを数える処理

sentence = "貧困、紛争、気候変動、感染症。人類は、これまでになかったような数多くの課題に直面しています。このままでは、人類が安定してこの世界で暮らし続けることができなくなると心配されています。そんな危機感から、世界中のさまざまな立場の人々が話し合い、課題を整理し、解決方法を考え、2030年までに達成すべき具体的な目標を立てました。それが「持続可能な開発目標(Sustainable Development Goals:SDGs）」です。"

counter = 0 # 句読点を数える変数
number = len(sentence) # 文章の文字の数を代入

for i in range(number):
    if(sentence[i] == "、" ): #「、」の時にカウンターを1追加
        counter += 1
    elif(sentence[i] == "。"):#「。」の時にカウンターを1追加
        counter += 1
    else:
        pass

print(counter) # 句読点の数を表示

"""