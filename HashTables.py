# I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity.
# Terence Jiang(20353261)

import random
import string

def toInteger(codeword):
    result = ord(codeword[0])
    for i in range (1, len(codeword)):
        result = result * 2 + ord(codeword[i])
    return result

class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size

    def hashFuncOne(self,key, i):
        hashOne = key%self.size
        hashTwo = key*2
        if(hashTwo%2==1):
            return (hashOne + hashTwo*i) % self.size
        else:
            return (hashOne + (hashTwo+1)*i) % self.size
        
    def hashFuncTwo(self,key, i):
        hashOne = key%self.size
        hashTwo = 3 - (key%3) # a prime that smaller than the table size
        return (hashOne + hashTwo*i) % self.size
        
    def hashFuncThree(self,key, i):
        hashOne = key%self.size
        hashTwo = (key**2)%self.size - 3
        return (hashOne + hashTwo*i) % self.size
           
    def insert(self, codename):
        i = 0
        keyInt = toInteger(codename) # codename into integer
        key = self.hashFuncThree(keyInt, i) # integer codename into hash 
        a=key
        
        while (i < self.size and self.slots[int(a)] != None):
            i+=1
            a = self.hashFuncThree(key, i)
        if self.slots[int(a)] is None:
            self.slots[int(a)] = codename
            return i
        else:
            print("insertion failed")
            return False
        

class QuadraticProbeHashTable:
    def __init__(self, size, c1, c2):
        self.size = size
        self.slots = [None] * self.size
        self.c1 = c1
        self.c2 = c2
    
    def hash(self, integer):
        return integer%self.size

    def quadraticProbe(self, hashVal, i):
        return (hashVal + self.c1 * i + self.c2 * i**2) % self.size
    
    def insert(self, key):
        i = 0
        keyInt = toInteger(key) # codename into integer
        v = self.hash(keyInt) # integer codename into hash 
        a=v
        try:
            while (i < self.size and self.slots[int(a)] != None):
                i+=1
                a = self.quadraticProbe(v, i)
            if self.slots[int(a)] is None:
                self.slots[int(a)] = key
                return i
            else:
                print("insertion failed")
                return False
        except TypeError:
            print(a)

def generate_random_word():
    length = random.randint(7, 8)
    return ''.join(random.choices(string.ascii_letters, k=length))
  

'''for c1, c2 in [(1, 1), (2, 1/2), (3, 1/3)]:  # Combinations of c1 and c2
    print("Quadratic Probing")
    hash_table = QuadraticProbeHashTable(2041, c1, c2)
    count = 0
    max = 0
    for i in range(2000):
        random_word = generate_random_word()
        result = hash_table.insert(random_word)
        if (result > max):
            max = result
        count += result

    avg = count / 2000
    print("size: 2041","c1:",c1,"c2:",c2, "avg comparisons:", avg)'''

print("###############################\nDouble Hashing")

doubleTable = DoubleHashingHashTable(2477)
count = 0
max = 0
for i in range(2000):
    random_word = generate_random_word()
    result = doubleTable.insert(random_word)
    if (result != False):  
        if (result > max):
            max = result
        count += result

avg = count / 2000
print("avg comparisons:", avg)

    