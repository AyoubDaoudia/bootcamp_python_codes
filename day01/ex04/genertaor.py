import  random

def words_filter(text,sep=" ",option=None):
    words=[]
    c=""
    j=0
    while text[j].isspace():
        j+=1
    for i in range(j,len(text)):
        if text[i].isalpha():
            c+=text[i]
            if i==len(text)-1:
                words.append(c)
        else:
            if (text[i]==sep and text[i-1].isalpha()):
                words.append(c)
            c=""
        
    return words



def generator(text,sep=" ",option=None):
    words=words_filter(text,sep)
    if option=="shuffle" :
        seen=[]
        for i in range(len(words)):
            while i==len(seen):
                t=random.randint(0,len(words))
                if words[t] not in seen:
                    seen.append(words[t])
                    print(words[t])
            yield i
    elif option=="unique" :
        seen=[]
        for i in range(len(words)):
            if words[i] not in seen:
                seen.append(words[i])
                print(words[i])
            yield i
    elif option=="ordered" :
        words.sort()
        for i in range(len(text)):
            print(words[i])
            yield i
    elif  option==None:
        for i in range(len(words)):
            print(words[i])
            yield  i
    else:
        exit ("Error")