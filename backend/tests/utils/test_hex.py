from backend.utils.hex2bin import hexToBinary

def testHexToBinary():
    originalNum = 789
    hexNum = hex(originalNum)[2:]
    binaryNum = hexToBinary(hexNum)

    assert int(binaryNum, 2) == originalNum