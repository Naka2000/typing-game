import random
import time

words = ['apple', 'banana', 'orange', 'grape', 'watermelon', 'pineapple', 'strawberry']
score = 0

print("タイピングゲームを開始します！")
time.sleep(1)

while True:
    word = random.choice(words)
    print("【", word, "】")
    start_time = time.time()
    user_input = input()

    end_time = time.time()
    elapsed_time = end_time - start_time

    if user_input == word:
        score += 1
        print("正解です！ 経過時間: {:.2f}s  得点: {}".format(elapsed_time, score))
    else:
        print("間違いです！ 経過時間: {:.2f}s  得点: {}".format(elapsed_time, score))
        break

print("ゲーム終了！ 最終得点: {}".format(score))
