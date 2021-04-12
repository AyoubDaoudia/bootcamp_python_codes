import sys

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep=sep
        self.header = header
        self.skip_top=skip_top
        self.skip_bottom=skip_bottom
        self.file=None
        
    def __enter__(self):
        try:
            self.file=open(self.filename,'r')
        except FileNotFoundError:
            sys.exit("File not found")
        return self
        
    def __exit__(self,exc_type, exc_val, exc_tb):
        self.file.close()
        
    def getdata(self):
        self.file.seek(self.skip_top)
        data_line=[]
        all_data=[]
        filedata=self.file.readlines()
        if self.skip_bottom!=0:
            filedata=filedata[:len(filedata)-self.skip_bottom]
        for data in filedata:
            data_line.append(data.replace('\n',''))
            info_line=data_line[0].split(self.sep)
            for info in info_line:
                if info == '' :
                    sys.exit("File corrupted")
                all_data.append(info)
            data_line=[]
        return all_data
    
    def getheader(self):
        if self.header==True:
            self.file.seek(0)
            return self.file.readline()
        return None
    

if __name__ == "__main__":
    with CsvReader('good.csv',sep=';',header=True,skip_bottom=1) as file:
        data = file.getdata()
        print(data)
        header = file.getheader()
        print(header)
        
    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")