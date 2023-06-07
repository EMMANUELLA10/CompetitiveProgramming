num_eng_news = int(input())

roll_num_eng = set(list(map(int, input().split())))

num_frnch_news = int(input())

roll_num_frnch = set(list(map(int, input().split())))

print(len(roll_num_eng.difference(roll_num_frnch)))