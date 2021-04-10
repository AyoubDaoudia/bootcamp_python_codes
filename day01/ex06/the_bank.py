class Account:

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    
    def transfer(self, amount):
        self.value += amount
        
def corrupted_account(account):
    if not isinstance(account,Account):
        raise TypeError
    acc_prop=dir(account)
    if len(acc_prop)%2!=0:
        return True
    bank_prop=[]
    for i in acc_prop:
        if i[0] == 'b' :
            return True
        if i == 'name' or i == 'id' or i == 'value' or i[:3] == 'zip' or i[:4] == 'addr':
            bank_prop.append(i)
    if 'name' not in bank_prop or 'id' not in bank_prop  or 'value' not in bank_prop:
        return True
    for i in bank_prop:
        if i[:3]=='zip' :
            return False
        if i[:4]== 'addr' :
            return False
    return True
        
            
            

class Bank:
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        if isinstance(account,Account):
            self.account.append(account)
        else:
            return "Unacceptable"

    def transfer(self, origin, dest, amount):
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        if not isinstance(origin,int) and not isinstance(origin,str):
            return False
        
        if not isinstance(dest,int) and not isinstance(dest,str):
            return False
        
        origin_acc=None
        dest_acc=None
        
        for acc in self.account:
            if acc.name==origin or acc.id==origin:
                origin_acc=acc
            elif acc.name==dest or acc.id==dest:
                dest_acc=acc
        
        if origin_acc==None or dest_acc==None:
            return False
        
        if corrupted_account(origin_acc) or corrupted_account(dest_acc):
            return False
        
        if origin_acc.value<amount or origin_acc.value==0:
            return False
        
        origin_acc.value-=amount
        dest_acc.transfer(amount)
        return True
        
        

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        if not isinstance(account,int) and not isinstance(account,str):
            return False
        if not corrupted_account(account):
            return True
        corr_acc=None
        for acc in self.account:
            if acc.name==account or acc.id==account:
                corr_acc=acc
        if corr_acc==None:
            return False
        for i in dir(corr_acc):
            if i[0]=='b' :
                delattr(corr_acc,i)
        if not hasattr(corr_acc,'zip') and not hasattr(corr_acc,'addr'):
            corr_acc.zip=""
        if not hasattr(corr_acc,'name'):
            return False
        if not hasattr(corr_acc,'id'):
            return False
        if not hasattr(corr_acc,'value'):
            corr_acc.value=0
        
        return True