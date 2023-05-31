
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



    @staticmethod
    def isValidChain(chain):
        if chain[0] != Block.genesis():
            print(chain[0])
            print("incorrect genesis")
            raise Exception("The genesis block must be valid")

        for i in range(1, len(chain)):
            block = chain[i]
            lastBlock = chain[i-1]
            Block.isValidBlock(lastBlock, block)

        # for i in range(1, len(chain):
        #     block = chain[i]
        #     lastBlock = chain[i-1]
        #     Block.isValidBlock(lastBlock, block)

def main():

    blockchain = Blockchain()
    blockchain.addBlock("one")
    blockchain.addBlock("two")
    blockchain.addBlock("three")
    blockchain.isValidChain(blockchain.chain)
    #
    # print(blockchain)
    #
    # print(f"blockchain.py __name__: {__name__}")

if __name__ == "__main__":
    main()