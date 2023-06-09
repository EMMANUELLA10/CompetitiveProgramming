def total_subscriptions(english_subscriptions, french_subscriptions):
    
    english_set = set(english_subscriptions)
    french_set = set(french_subscriptions)

    
    combined_set = english_set | french_set

    
    return len(combined_set)


num_english = int(input())
english_subs = list(map(int, input().split()))
num_french = int(input())
french_subs = list(map(int, input().split()))


result = total_subscriptions(english_subs, french_subs)

print(result)
