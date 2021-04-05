class Vector:
    def __init__(self,info):
        if type(info)==list:
            for i in info:
                if type(i)!=int :
                    raise TypeError
                if type(i)==int:
                    i=float(i)
            self.values=info
        elif type(info)==int:
            if info<0:
                raise ValueError
            vec=[]
            for i in range(info):
                vec.append(float(i))
            self.values=vec
        elif type(info)==tuple:
            if len(info)!=2 or info[0]>info[1]:
                raise ValueError
            vec=[float (i) for i in range(info[0],info[1])]
            self.values=vec
        else:
            raise TypeError
        self.size=len(self.values)
        
    def __add__(self,second):
        result=Vector(0)
        if type(second)==Vector:
            for i in range(self.size):
                result.values.append(self.values[i]+second[i])
            return result
        elif type(second)==int or type(second)==float:
            for i in range(self.size):
                result.values.append(self.values[i]+second)
            return result
        else:
            raise TypeError
    def __radd__(self,second):
        return Vector.__add__(self,second)
    def __sub__(self,second):
        result=Vector(0)
        if type(second)==Vector:
            for i in range(self.size):
                result.values.append(self.values[i]-second[i])
            return result
        elif type(second)==int or type(second)==float:
            for i in range(self.size):
                result.values.append(self.values[i]-second)
            return result
        else:
            raise TypeError
    def __rsub__(self,second):
        return Vector.__sub__(self,other)
    def __mul__(self,other):
        result=Vector(0)
        if type(second)==int or type(second)==float:
            for i in range(self.size):
                result.values.append(self.values[i]*second)
            return result
        else:
            raise TypeError
    def __rmul__(self,second):
        return Vector.__mul__(self,other)
    def __truediv__(self,second):
        if second==0:
            raise ZeroDivisionError
        return Vector.__mul__(self,1/second)
    def __rtruediv__(self,second):
        return Vector.__truediv__(self,second)
    def __str__(self):
        for i in range(self.size):
            print("| {} |".format(self.values[i]))
        return ""
    
        