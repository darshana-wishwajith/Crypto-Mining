from multiprocessing import Process
from hashlib import sha256

class HashProcesser(Process) :
    def __init__(self, process_id, block_number, transactions, previous_hash, difficulty, nonce) :
        super(HashProcesser, self).__init__()
        self.process_id = process_id
        self.block_number = block_number
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonce = nonce

    
    def run(self) :
        self.mine(self.block_number, self.transactions, self.previous_hash,self.difficulty)
    
    def SHA256(self, data) :
        return sha256(data.encode('ascii')).hexdigest()

    def mine(self, block_number, transactions, previous_hash, difficulty) :
        prefix_zeros = '0' * difficulty

        for nonce in self.nonce :
            data = str(block_number) + transactions + previous_hash + str(nonce)
            new_hash = self.SHA256(data)
            print(self.process_id, nonce, new_hash)
            if new_hash.startswith(prefix_zeros) :
                print(f'Congratulations! You have successfully mined Bitcoins whith nonce value : {nonce}')
                print(new_hash)
                return new_hash
        
        raise BaseException(f"Couldn't find correct hash after trying {self.nonce} times." )

