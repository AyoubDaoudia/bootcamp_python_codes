class TinyStatitician:
    def mean(self,array):
        if len(array)==0:
            return None
        result=0
        for i in array:
            result+=i
        return round(result/len(array),2)
    
    def median(self,array):
        if len(array)==0:
            return None
        array.sort()
        if len(array)%2==1:
            return array[(len(array)-1)//2]
        return round((array[len(array)//2-1]+array[len(array)//2])/2,2)
    
    def quantile(self,array,percentile):
        if len(array)==0:
            return None
        array.sort()
        lst=[]
        perc=0
        for i in range(len(array)):
            lst.append(perc)
            perc+=round(100/(len(array)-1),2)
        arr_perc=list(zip(array,lst))
        result=None
        if arr_perc[0][1]<=percentile<arr_perc[1][1]:
            return array[0]
        for i in range(1,len(arr_perc)):
            if arr_perc[i-1][1]<=percentile<arr_perc[i][1]:
                return array[i-1]
        return array[len(array)-1]
    
    def var(self,array)==0:
        return None
        if len(array)
        mean=self.mean(array)
        result=0
        for i in array:
            result+=(i-mean)**2
        return round(result/len(array),2)
    
    def std(self,array):
        if len(array)==0:
            return None
        return round((self.var(array))**0.5,2)