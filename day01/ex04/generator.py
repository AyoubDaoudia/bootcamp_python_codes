import  random

def words_filter(text,sep=" "):
    words=[]
    c=""
    j=0
    while text[j].isspace():
        j+=1
    for i in range(j,len(text)):
        if text[i]!=sep:
            c+=text[i]
        if i==len(text)-1:
            words.append(c.strip())
        if text[i]==sep:
            words.append(c.strip())
            c=""
    words_f=[]
    for i in words:
        if i.isalnum() :
            words_f.append(i)
    return words_f


def generator(text,sep=" ",option=None):
    if type(text)!=str:
        return "Error"
    words=words_filter(text,sep)
    if option=="shuffle" :
        num=[]
        for i in words:
            t=random.randint(0,len(words)-1)
            while t in num:
                t=random.randint(0,len(words)-1)
            i=words[t]
            num.append(t)
            yield i
    elif option=="unique" :
        seen=[]
        for i in words:
            if i not in seen:
                seen.append(i)
                yield i
    elif option=="ordered" :
        words.sort()
        for i in words:
            yield i
    elif  option==None:
        for i in words:
            yield i
    else:
        return "Error"