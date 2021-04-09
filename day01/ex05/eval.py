class Evaluator:
    @staticmethod
    def zip_evaluate(words,coeffs):
        if not isinstance(words,list) and not isinstance(coeffs,list):
            raise TypeError
        if len(words)!=len(coeffs):
            raise ValueError
        words=tuple(words)
        for i in words:
            if not isinstance(i,str):
                raise TypeError
        coeffs=tuple(coeffs)
        for i in coeffs:
            if not isinstance(i,int) and not isinstance(i,float):
                raise TypeError
        lst=tuple(zip(words,coeffs))
        result=0
        for i in range(len(lst)):
            result+=lst[i][1]*len(lst[i][0])
        return result
    
    @staticmethod
    def enumerate_evaluate(words,coeffs):
        if not isinstance(words,list) and not isinstance(coeffs,list):
            raise TypeError
        if len(words)!=len(coeffs):
            raise ValueError
        for i in words:
            if not isinstance(i,str):
                raise TypeError
        for i in coeffs:
            if not isinstance(i,int) and not isinstance(i,float):
                raise TypeError
        words=list(enumerate(words))
        for i in range(len(words)):
            words[i]=list(words[i])
            words[i][0]=coeffs[i]
        result=0
        for i in range(len(words)):
            result+=len(words[i][1])*words[i][0]
        return result