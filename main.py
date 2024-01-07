import time
from multiprocessed import HashProcesser
import os

if __name__ == '__main__' :

    print(f"{20*'-'}Cryptocurency Minner{20*'-'}")
    block_number = int(input("Block Number : "))
    previous_hash = input("previous Hash : ")
    transactions = input("Transactions : ")
    difficulty = int(input("difficulty Level : "))
    max_nonce = int(input("Max Nonce :"))

    cpu_count = os.cpu_count()
    cores = cpu_count / 2
    core_size = max_nonce // cores

    all_nonces = []
    for i in range(max_nonce) :
        all_nonces.append(i)

    
    sliceed_nonces = []
    for i in range(0, len(all_nonces), int(core_size)) :
        n = all_nonces[i : i + int(core_size)] 
        sliceed_nonces.append(n)

    pro_counter = []

    start = time.time()
    
    for i in range(0,int(cores)) :
        pro = HashProcesser(f'Process - {i}', block_number, transactions, previous_hash, difficulty, sliceed_nonces[i])
        pro.start()
        pro_counter.append(pro)

    for pro in pro_counter :
        pro.join()

    end = time.time()

    print(f"Duration : {end - start} Seconds")