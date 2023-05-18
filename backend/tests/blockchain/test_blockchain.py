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