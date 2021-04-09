class Matrix:
    def __init__(self,m_info,m_second=None):
        if isinstance(m_info,list):
            if len(m_info)>0:
                if isinstance(m_info[0],int):
                    if isinstance(self,Vector):
                        for i in range (len(m_info)):
                            if type(m_info[i])!=int:
                                raise TypeError
                            m_info[i]=float(m_info[i])
                        self.shape=(1,len(m_info))
                    else:
                        raise TypeError
                elif isinstance(m_info[0],list):
                    length=len(m_info[0])
                    for i in range(len(m_info)):
                        if type(m_info[i])!=list:
                            raise TypeError
                        if len(m_info[i])!=length:
                            raise ValueError
                        for j in range(len(m_info[0])):
                            m_info[i][j]=float(m_info[i][j])
                    self.shape=(len(m_info),len(m_info[0]))
                else:
                    raise TypeError
            self.data=m_info
            if m_second !=None:
                if type(m_second)!=tuple:
                    raise TypeError
                if len(m_second)!=2:
                    raise ValueError
                if len(m_info)!=m_second[0] or len(m_info)!=m_second[1]:
                    raise ValueError
        elif type(m_info)==tuple:
            if m_second!=None:
                raise ValueError
            if len(m_info)!=2:
                raise ValueError
            if type(m_info[0])!=int or type(m_info[1])!=int:
                raise TypeError
            matrix=[]
            for i in range(m_info[0]):
                matrix.append([0.0 for i in range(m_info[1])])
            self.shape=(m_info[0],m_info[1])
            self.data=matrix
        elif isinstance(m_info,int) and isinstance(self,Vector):
            if m_info<0:
                raise ValueError
            self.data=[0.0 for i in range(m_info)]
            self.shape=(m_info,1)
        else:
            raise TypeError
    def __str__(self):
        if self.shape[0]==1:
            print("| ",end="")
            for i in range(self.shape[1]):
                print(self.data[0][i],end="  ")
            print("|")
            return ""
        for i in range(self.shape[0]):
            print("| ",end="")
            for j in range(self.shape[1]):
                print(self.data[i][j],end="  ")
            print("|",end="\n\n")
        return ""
    
    def __add__(self,other):
        result=Matrix(self.shape)
        if type(other)!=Matrix:
            raise TypeError
        if self.shape!=other.shape:
            raise ValueError
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                result.data[i][j]=self.data[i][j]+other.data[i][j]
        return result
    def __radd__(self,other):
        return Matrix.__add__(self,other)
    def __sub__(self,other):
        result=Matrix(self.shape)
        if type(other)!=Matrix:
            raise TypeError
        if self.shape!=other.shape:
            raise ValueError
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                result.data[i][j]=self.data[i][j]-other.data[i][j]
        return result
    def __rsub__(self,other):
        return Matrix,__sub__(self,other)
    def __mul__(self,other):
        if type(other)==float or type(other)==int:
            result=Matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result.data[i][j]=self.data[i][j]*other
            return result
        elif type(other)==Vector:
            if self.shape[1]!=other.shape[0]:
                raise ValueError
            result=Vector((self.shape[0],1))
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    result.data[i]+=self.data[i][k]*other.data[k]
            return result
        elif type(other)==Matrix:
            result=Matrix((self.shape[0],other.shape[1]))
            if self.shape[1]!=other.shape[0]:
                raise ValueError
            for i in range(self.shape[0]):
                for j in range(other.shape[1]):
                    for k in range(self.shape[1]):
                        result.data[i][j]+=self.data[i][k]*other.data[k][j]
            return result
        else:
            raise TypeError
    def __rmul__(self,other):
        return Matrix.__mul__(self,other)
    def ___truediv__(self,other):
        if type(other)!=int and type(other)!=float:
            raise TypeError
        if other==0:
            raise ZeroDivisionError
        return Matrix.__mul__(self,1/other)
    def __rtruediv__(self,other):
        return Matrix.__truediv__(self,other)
    def __repr__(self):
        return "A matrix of type {} to have its values please just print it".format(self.shape)
    
class Vector(Matrix):
    def __init__(self,m_info=None,m_second=None):
        super().__init__(m_info=m_info,m_second=None)
        if type(m_info)==list:
            if self.shape[0]!=1:
                raise ValueError
            if len(m_info)>0:
                for i in m_info:
                    if type(i)!=float:
                        raise TypeError
            self.shape=(self.shape[1],self.shape[0])
        if type(m_info)==tuple:
            if len(m_info)!=2 or m_info[1]!=1:
                raise ValueError
            self.data=[self.data[i][0] for i in range(self.shape[0])]
    def __str__(self):
        for i in range(self.shape[0]):
            print("| {} |".format(self.data[i]))
        return ""