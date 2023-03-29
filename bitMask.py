chainToBit = { "Chain 0": 0, "Chain 1": 1, "Chain 2": 2, "Chain 3": 3, "Chain 4": 4, "Chain 5": 5,
               "Chain 6": 6, "Chain 7": 7, "CRX chain": 8 } 

def bitMaskForChain(chainToValueArray):
    result = 0
    errorLog = ""
    checkDuplicate = {}
    for chain, value in chainToValueArray:
        if value < 0 or value > 3:
            errorLog += chain + "is invalid. Value shoud be inclusively between 0 ~ 3.\n"
            continue
        if chain in checkDuplicate:
            raise Exception("Deplicated chain: " + chain)
        bitPosition = chainToBit[chain]
        result |= value << (bitPosition * 2)
    
    if errorLog != "":
        raise Exception(errorLog)
    return result
    

userInput = [("Chain 0", 2), ("Chain 5", 1), ("Chain 7", 3)]

print(bitMaskForChain(userInput))
