'''
This is trading application code
this module covers vendor enrollment and billing process
vendor enrollment is constructor call with two required arguments
billing process is non-constructor
'''
import time
class Vendor:
    '''This is vendor class docs section'''
    def __init__(self,vname,vGST):
        '''this is vendor initialization block - two args required'''
        self.vname = vname
        self.vGST = vGST
        print(f'Vendor {self.vname} enrollment is done!')
    def billing(self,pName,pCost=0.0,pQty=0):
        '''this is billing methods one required arg and two default args'''
        self.pName = pName
        self.pCost = pCost
        self.pQty = pQty
        self.tax = 0.18
        self.total = self.pQty * self.pCost
        self.gs = self.total + self.tax
        self.purchase_info()
    def purchase_info(self):
        wobj = open("purchase_info.log","a")
        wobj.write(f'{self.vname}\t{self.vGST}\t{self.pName}\t{self.pCost}\t')
        wobj.write(f'{self.pQty}\t{self.total}\t{self.gs}\t
                   Billing date:{time.ctime()}\n\n')
        wobj.close()
