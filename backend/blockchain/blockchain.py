
from backend.blockchain.block import Block

class Blockchain:
    """
    Blockchain: a public ledger of transactions
    Implemented as a list of blocks - datasets of transaction
    """
    def __init__(self):
        self.chain = [Block.genesis()]

    def addBlock(self, data):
        lastBlock = self.chain[-1]
        self.chain.append(Block.mineBlock(lastBlock, data))

    def __repr__(self):
        return f"Blockchain {self.chain}"

def main():
    blockchain = Blockchain()
    blockchain.addBlock("one")
    blockchain.addBlock("two")

    print(blockchain)

    print(f"blockchain.py __name__: {__name__}")

if __name__ == "__main__":
    main()