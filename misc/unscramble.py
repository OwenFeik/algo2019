def unscramble(word,dictionary):
    l=len(word)
    p=[]

    for w in dictionary:
        if len(w)==l:
            p.append(w)
    
    for w in p:
        t=[word[i] for i in range(0,len(word))]
        for c in w:
            if not c in t:
                p.remove(w)
                break
            else:
                t.remove(c)

    return p

dictionary=['apple','aardvark','banana','boat','orange','cabbage']
scrambled_words=['pplea','nanaba','eroang']

for word in scrambled_words:
    print(word,unscramble(word,dictionary))