word = str(input("Give me a word"))
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
count = 0
for char in word:
    if char in vowels:
        count += 1
    else:
        continue

print(count)