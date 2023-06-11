
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

    def replaceChain(self, chain):
        """
        Replace the local chain if:
        - The incoming chain is longer.
        - The incoming chain is formatted properly
        """
        if len(chain) <= len(self.chain):
            raise Exception("Cannot replace the chain. The incoming chain must be longer.")
        try:
            Blockchain.isValidChain(chain)
        except Exception as e:
            raise Exception(f'Cannot replace the chain. The incoming chain must be valid: {e}.')

        self.chain = chain

    def toJson(self):
        """
        Serialize a blockchain into the list of blocks
        """
        # blockList = []
        # for block in self.chain:
        #     blockList.append(block.toJson())

        return list(map(lambda block: block.toJson(), self.chain))







    @staticmethod
    def isValidChain(chain):
        if chain[0] != Block.genesis():
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