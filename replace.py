# =====================================
# 文字を変換するプログラム
# 特定の文字を指定して違う文字に変換する処理
# =====================================

sentence = "AAAAAAAAABBBBBBBBBCCCCCCC"

sentence = sentence.replace('B','Z')
print(sentence)


"""
# 単語の変換を間違えたときに、修正するプログラム

sentence = "今月は柿がおいしい季節ですね。柿のおいしい広島に行って、柿食べ放題をしたいですね！"
before_word = "柿"
after_word  = "牡蠣"

sentence = sentence.replace(before_word,after_word)

print(sentence)

"""