import hashlib  
import json  
from time import time     
class Block_chain(object):  
    def __init__(self):  
        self.chain = []  
        self.pendingTransactions = []  
        self.newBlock(previousHash = "İlk Rassal Değer", the_proof = 100)
    def newBlock(self, the_proof, previousHash = None):  
        the_block = {  
            'ID': len(self.chain) + 1,  
            'timestamp': time(),  
            'transaction': self.pendingTransactions, 
            'proof': the_proof,  
            'previous_hash': previousHash or self.hash(self.chain[-1]),  
        }  
        self.pendingTransactions = []  
        self.chain.append(the_block)   
        return the_block  
    @property  
    def lastBlock(self):     
        return self.chain[-1]  
    def newTransaction(self, gonderici, alici, deger):  
        kayit = {  
            'Gönderen Musteri ':  gonderici,  
            'Alan Musteri ': alici,  
            'Gönderilen Bitcoin Değeri ': deger  
        }  
        self.pendingTransactions.append(kayit)  
        return self.lastBlock['ID'] + 1    
    def hash(self, the_block):  
        stringObject = json.dumps(the_block, sort_keys = True)   
        blockString = stringObject.encode()  
        rawHash = hashlib.sha256(blockString)
        hexHash = rawHash.hexdigest()   
        return hexHash  

block_chain = Block_chain()  
transaction1 = block_chain.newTransaction("Musteri_1", "Musteri_2", '10 BTC')
transaction2 = block_chain.newTransaction("Musteri_2", "Musteri_1", '2 BTC')
transaction3 = block_chain.newTransaction("Musteri_3", "Musteri_1", '6 BTC')
block_chain.newBlock(10123) 
transaction4 = block_chain.newTransaction("Musteri_2", "Musteri_3", '2 BTC') 
transaction5 = block_chain.newTransaction("Musteri_3", "Musteri_3", '3 BTC') 
block_chain.newBlock(10384)
transaction6 = block_chain.newTransaction("Musteri_4", "Musteri_1", '8 BTC')  
block_chain.newBlock(10472) 
print( block_chain.chain)
