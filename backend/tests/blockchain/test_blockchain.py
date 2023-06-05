import pytest

from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA

def testBlockchainInstance():
    blockchain = Blockchain()
    assert blockchain.chain[0].hash == GENESIS_DATA['hash']

def testAddBlock():
    blockchain = Blockchain()
    data = "test-data"
    blockchain.addBlock(data)
    assert blockchain.chain[-1].data == data

@pytest.fixture
def returnBlockchain3Blocks():
    blockchain = Blockchain()
    for i in range(3):
        blockchain.addBlock(i)
    return blockchain

def testIsValidChain(returnBlockchain3Blocks):
    # bch = return_blockchain_three_blocks()
    Blockchain.isValidChain(returnBlockchain3Blocks.chain)

def testIsValidChainBadGeneis(returnBlockchain3Blocks):
    # bch = return_blockchain_three_blocks()
    returnBlockchain3Blocks.chain[0].hash = "bad-hash"
    with pytest.raises(Exception, match="The genesis block must be valid"):
        Blockchain.isValidChain(returnBlockchain3Blocks.chain)

def testReplaceChain(returnBlockchain3Blocks):
    blockchain = Blockchain()
    blockchain.replaceChain(returnBlockchain3Blocks.chain)
    assert blockchain.chain == returnBlockchain3Blocks.chain

def testReplaceChainCheckLength(returnBlockchain3Blocks):
    blockchain = Blockchain()
    with pytest.raises(Exception, match="The incoming chain must be longer."):
        returnBlockchain3Blocks.replaceChain(blockchain.chain)

def testReplaceChainBadChain(returnBlockchain3Blocks):
    blockchain = Blockchain()
    returnBlockchain3Blocks.chain[1].hash = "bad-hash"
    with pytest.raises(Exception, match="The incoming chain must be valid"):
        blockchain.replaceChain(returnBlockchain3Blocks.chain)




# def testIsValidChain():
#     blockchain = Blockchain()
#     for i in range (3):
#         blockchain.addBlock(i+1)
#
#     Blockchain.isValidChain(blockchain.chain)


# def testIsValidChainBadBlock(returnChain3Blocks):
#     blockchain = Blockchain()
#     for i in range (3):
#         blockchain.addBlock(i+1)
#
#     Blockchain.isValidChain(blockchain.chain)