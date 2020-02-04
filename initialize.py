import hashlib


def getFile(file):
    File = open(file,"r")
    string = File.read()
    return string

def getHash(str):
    hashed = hashlib.sha256(str.encode())
    return hashed.hexdigest()


def sepStr():
    mem_f_s = getFile("mempoolFull.txt")
    #Delete Spaces and line break
    if (mem_f_s.find("\n") != -1):
        mem_sp_s = mem_f_s.replace("\n","")
    else:
        mem_sp_s = mem_f_s

    if (mem_sp_s.find(" ") != -1):
        mem_cln_s = mem_sp_s.replace(" ","")
    else:
        mem_cln_s = mem_sp_s

    memf_lst = mem_cln_s.split(",")
    memf_str = ','.join(memf_lst)
    return memf_str



def writeFile(file,string):
    file = open(file,"w")
    file.write(string)
    file.close()


writeFile("memHashedFull.txt",sepStr())
writeFile("updatedMem.txt",sepStr())

writeFile("prevBlock.txt",getFile("firstBlock.txt"))
writeFile("historyChain.txt",getFile("prevBlock.txt")+"\n")
