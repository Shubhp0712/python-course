def remove(l1,word):
    l2 = []
    for item in l1:
        if item != word:
            l2.append(item.strip(word))
    return l2

l1 = ['apple','banana','apple','mango','apple','orange']

print(remove(l1,"le"))