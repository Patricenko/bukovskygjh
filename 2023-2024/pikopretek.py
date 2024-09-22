f = open("rocnik5.txt", "r")
data = f.read()
f.close()
data = data.split("\n")

def find_pairs(words):
    pairs = []
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if not set(words[i]) & set(words[j]):  # Check if there are no common letters
                pairs.append((words[i], words[j]))
    return pairs

words = data
print(find_pairs(words))