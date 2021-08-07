import time
import pickle
import sys
from pearhash import PearsonHasher
########
class Transacation:
    def __init__(self,sender,reciver,amount):
        self.sender=sender
        self.reciver=reciver
        self.amount=amount
    def __str__(self):
        return self.sender+" "+self.reciver+" "+ str(self.amount)
######
def hashp(message):
     hashe=PearsonHasher(4)
     message=message.encode()
     return hashe.hash(message).hexdigest

class Block:
    def __init__(self,index,transaction,previous_hash):
        self.index=index
        self.transaction=transaction
        self.tima_stamp=time.strftime('%X %x ')
        self.previous_hash=previous_hash
        if index!=0:
            o= str(self.index)+str(self.transaction)+str(self.tima_stamp)+str(self.previous_hash)
            self.hash=hashp(o)
        else:
            o= str(self.index)+str(self.transaction)+str(self.tima_stamp)
            self.hash=hashp(o)
    def hashBlock(self):
        return self.hash
#########
class BlockChain:
    def  __init__(self):
        self.chain=[]
        self.addres=[]
    def addBlock(self,transacatio):
        if self.chain!=[]:
            index1=len(self.chain)
            previous_hash1=self.chain[-1].hash
            new=Block(index1,transacatio,previous_hash1)
            self.chain+=[new]
        else:
            new=Block(0,transacatio,None)
            self.chain+=[new]
    def save(self,address):
        file=open(address,"wb")
        pickle.dump(self,file)
        file.close
        self.addres+=[address]
    def load(self,address):
        file=open(address,"rb")
        d=pickle.load(file)
        self.chain=d.chain
        file.close
        self.addres+=[address]
    def validationCheck(self):
        d=self.chain
        for i in range(0,len(self.chain)-1):
            if d[i+1].previous_hash!=d[i].hash:
                return  False
        return True

def vum():
    p=input("Hi. Welcome to my Project. Enter your request:\n 1.add newe transactions \n 2.check the valididty of the chain\n 3.show\n 4.save\n 5.load\n 6.Exite\n")
    tui=BlockChain()
    while p!="6":
        if p=="1":
            sender1=input("enter the sender's name:")
            reciver1=input("enter the reciver name:")
            t=input("enter amount transfer value:")
            try:
                amount1=int(t)
            except:
                amount1=float(t)
            d=Transacation(sender1,reciver1,amount1)
            tui.addBlock(d)
            p=input("\ntransactions is successful, Enter your request:\n 1.add newe transactions \n 2.check the valididty of the chain\n 3.show\n 4.save\n 5.load\n 6.Exite\n")
            pass
        if p=="2":
            t=tui.validationCheck()
            if t:
                p=input("Security is established, Enter your request:\n 1.add newe transactions \n 2.check the valididty of the chain\n 3.show\n 4.save\n 5.load\n 6.Exite\n")
                pass
            if  not t:
                print("The security problem of the BlockChina",file=sys.stderr)
                tui.save()
                raise
        if p=="3":
            if tui.chain==[]:
                print("not any transactions","\n",file=sys.stderr)
                p=input( "Enter your request:\n 1.add newe transactions \n 2.check the valididty of the chain\n 3.show\n 4.save\n 5.load\n 6.Exite\n")
                pass
            t=input(" 1.show last transactions\n 2.Show all transactions\n")
            print("sender","\t","reciver","\t","amount","\t","tmie")
            if t=="1":
                print(tui.chain[-1].transaction.sender,"\t",tui.chain[-1].transaction.reciver,"\t",tui.chain[-1].transaction.amount,"\t",tui.chain[-1].tima_stamp,"\n")
                p=input( "Enter your request:\n 1.add newe transactions \n 2.check the valididty of the chain\n 3.show\n 4.save\n 5.load\n 6.Exite\n")
                pass
            if t=="2":
                for t in range(len(tui.chain)):
                    print(str(t+1),tui.chain[-1].transaction.sender,"\t",tui.chain[-1].transaction.reciver,"\t",tui.chain[-1].tima_stamp,"\n")
                p=input( "Enter your request:\n 1.add newe transactions \n 2.check the valididty of the chain\n 3.show\n 4.save\n 5.load\n 6.Exite\n")
                pass
        if p=="4":
            add=input("Enter address:")
            tui.save(add)
            p=input("save is successful, Enter your request:\n 1.add newe transactions \n 2.check the valididty of the chain\n 3.show\n 4.save\n 5.load\n 6.Exite\n")
            if add not in tui.addres:
                t=input("Are you sure you want to change the"+str(add)+":1.Yes\t2 No")
            
        if p=="5":
            add=input("Enter address:")
            tui.load(add)
            p=input("load is successful, Enter your request:\n 1.add newe transactions \n 2.check the valididty of the chain\n 3.show\n 4.save\n 5.load\n 6.Exite\n")
            pass
        else:
            print("this key not difin","\n",file=sys.stderr)
            p=input( "Enter your request:\n 1.add newe transactions \n 2.check the valididty of the chain\n 3.show\n 4.save\n 5.load\n 6.Exite\n")
            pass
    
vum()      
        


        
        
        
        
        



