# Solution 2: Mistakes

words = ["banana", "jackfruit", "berry", "strawberry", "mango"]
line = ""

for i in range(len(words)):
    line += words[i]
    if i != len(words) - 1:
        line += ','

print(line)
