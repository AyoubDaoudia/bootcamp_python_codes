class Vector:
    def __init__(self,info):
        if type(info)==list:
            for i in range(len(info)):
                if type(info[i])!=int :
                    raise TypeError
                if type(info[i])==int:
                    info[i]=float(info[i])
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
        result=Vector(self.size)
        for i in range(self.size):
            result.values[i]=0
        if type(second)==Vector:
            if self.size!=second.size:
                raise ValueError
            for i in range(self.size):
                result.values[i]=self.values[i]+second.values[i]
            return result
        elif type(second)==int or type(second)==float:
            for i in range(self.size):
                result.values[i]=self.values[i]+second
            return result
        else:
            raise TypeError
    def __radd__(self,second):
        return Vector.__add__(self,second)
    def __sub__(self,second):
        result=Vector(self.size)
        for i in range(self.size):
            result.values[i]=0
        if type(second)==Vector:
            if self.size!=second.size:
                raise ValueError
            for i in range(self.size):
                result.values[i]=self.values[i]-second.values[i]
            return result
        elif type(second)==int or type(second)==float:
            for i in range(self.size):
                result.values[i]=self.values[i]-second
            return result
        else:
            raise TypeError
    def __rsub__(self,second):
        return Vector.__sub__(self,other)
    def __mul__(self,second):
        result=Vector(self.size)
        for i in range(self.size):
            result.values[i]=0
        if type(second)==int or type(second)==float:
            for i in range(self.size):
                result.values[i]=self.values[i]*second
            return result
        elif type(second)==Vector:
            if self.size!=second.size:
                raise ValueError
            result=0
            for i in range(self.size):
                result+=self.values[i]*second.values[i]
            return result
        else:
            raise TypeError
    def __rmul__(self,second):
        return Vector.__mul__(self,other)
    def __truediv__(self,second):
        if type(second)==Vector:
            raise TypeError
        if second==0:
            raise ZeroDivisionError
        return Vector.__mul__(self,1/second)
    def __rtruediv__(self,second):
        return Vector.__truediv__(self,second)
    def __str__(self):
        for i in range(self.size):
            print("| {} |".format(self.values[i]))
        return ""
    def __repr__(self):
        for i in range(self.size):
            print("| {} |".format(self.values[i]))
        return ""