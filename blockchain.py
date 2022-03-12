import hashlib

def hashGenerator(data):
    result=hashlib.sha256(data.encode())
    return result.hexdigest()


class Block:
    def __init__(self,data,hash,prevHash):
        self.data=data
        self.hash=hash
        self.prevHash=prevHash


class Blockchain:
    def __init__(self):
        hashLast=hashGenerator('gen_last')
        hashStart=hashGenerator('gen_hash')

        genesis=Block('gen-data', hashStart, hashLast)
        self.chain= [genesis]

    def add_block(self,data):
        # saving the previous hash
        prevHash=self.chain[-1].hash

        # createing unique hash
        hash=hashGenerator(data+prevHash) 
        block=Block(data,hash,prevHash)
        self.chain.append(block)


# let the name of our blockchain be "Kushino(KSH)"

KSH=Blockchain()
KSH.add_block('1')
KSH.add_block('2')
KSH.add_block('3')
KSH.add_block('4')
KSH.add_block('4')
KSH.add_block('5')


# checking the elements in our blockchain
for block in KSH.chain:
    print(block.__dict__)

