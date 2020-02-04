"""PoW Mining Simulation for MIS3560
by Alexis Wu
"""
"""Paste the genesis block and transaction pool into "firstBlock.txt" and "memPoolFull.txt"

and Run initilize.py first
"""


import tkinter as tk
from tkinter import simpledialog, messagebox
import pyperclip
import hashlib
import random

application_window = tk.Tk()

def askInput():
    newBlock = simpledialog.askstring("Input", "input the block to be verified",
                                    parent=application_window)
    return newBlock

def getHash(str):
    hashed = hashlib.sha256(str.encode())
    return hashed.hexdigest()

def loadFile(file):
    f = open(file,'r')
    string = f.read()
    f.close()
    return string

def filterBlock():
    newBlock = askInput()
    if (newBlock.find("\n") != -1):
        newBlock = newBlock.replace("\n","")
    return newBlock

def getOldHash():
    oldBlock = loadFile("prevBlock.txt")
    
    oldHash = getHash(oldBlock)
    return oldHash

def readoldBlock():
    block = loadFile("prevBlock.txt")
    blockElement = block.split(",")
    num = int(blockElement[0])
    prevHash = blockElement[1]
    transacHash = blockElement[2]
    return block,num,prevHash, transacHash

def readnewBlock():
    block = filterBlock()
    blockElement = block.split(",")
    num = int(blockElement[0])
    prevHash = blockElement[1]
    transacHash = blockElement[2]
    return block,num,prevHash, transacHash

def updateMem(newTransac):
    f = open("updatedMem.txt","rw")
    string = f.read()
    if (string.find(newTransac) != -1):
        mem = ","+newTransac
        string = string.replace(mem,'')
    else:
        f.close()
        return False
    f.write(string)
    f.close()
    print("memupdated")
    return True


def getMemLst():
    memStr = loadFile("updatedMem.txt")
    memLst = memStr.split(",")
    return memLst

def rewriteFile(content,file):
    f = open(file,'w+')
    f.write(content)
    f.close()

def popMem(string):
    Mem = getMemLst()
    Mem.remove(string)
    newLst = ','.join(Mem)
    rewriteFile(newLst,"updatedMem.txt")

def saveHistory(string):
    f = open("historyChain.txt",'a+')
    f.write("\n"+"\n"+string)
    f.close()

def generate():
    oldblock,oldnum,oldprevHash,oldtransacHash = readoldBlock()
    num = oldnum+1
    prevHash = getOldHash()
    transacLst = getMemLst()
    transaction = random.choice(transacLst)
    popMem(transaction)
    Miner = "Alexis Wu"
    incompBlock = str(num)+","+prevHash+","+getHash(transaction)+","+Miner
    i = 0
    while True:
        #m位开始k个是str n
   
        nonce = i
        untestedBlock = incompBlock+","+str(nonce)
        hashedNewblock = getHash(untestedBlock)

        #m位开始k个都是str n
        m = 2
        k = 2
        n = "00"
        # #incase有跳位
        p = 1
        q = 2
        s = "00"
        # if (hashedNewblock[m-1:m-1+k] == n or (hashedNewblock[p-1:p-1+q] == s)):
        if (hashedNewblock[m-1:m-1+k] == n):
            success = untestedBlock+"\n"+hashedNewblock+"\n"+transaction
            pyperclip.copy(success)
            messagebox.showinfo("You Made it!", success)
            saveHistory(success)
            rewriteFile(untestedBlock,"prevBlock.txt")
            break;
        else:
            i = i+1
        
for a in range(30):
    generate()
