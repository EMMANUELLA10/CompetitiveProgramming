word = str(input("please enter a word: "))
letter = str(input("please enter a letter: "))
total_letters = len(word)
letter_count = word.count(letter)
result = (letter_count/total_letters)*100
print(f"The percent of {letter} in {word} is: {result}%")
