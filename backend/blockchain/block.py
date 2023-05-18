import time
from backend.utils.crypto_hash import cryptoHash

GENESIS_DATA = {
    "timestamp": 1,
    "lastHash": "genesisLastHash",
    "hash": "genesisHash",
    "data": []
}

class Block:
    """
    Block: a unit of storage
    Store blocks ina chain that supports the cryptocurrency
    """

    def __init__(self, timestamp, lastHash, hash, data):
        self.timestamp = timestamp
        self.lastHash = lastHash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp},'
            f'lastHash: {self.lastHash},'
            f'hash: {self.hash},'
            f'data: {self.data})'
        )

    @staticmethod
    def mineBlock(lastBlock, data):
        """
        Mine a block based on the given lastBlock and data
        """
        timestamp = time.time_ns()
        lastHash = lastBlock.hash
        hash = cryptoHash(timestamp, lastHash, data)
        return Block(timestamp, lastHash, hash, data)

    @staticmethod
    def genesis():
        return Block(**GENESIS_DATA)
        # return Block(
        #     GENESIS_DATA["timestamp"],
        #     GENESIS_DATA["lastHash"],
        #     GENESIS_DATA["hash"],
        #     GENESIS_DATA["data"]
        # )
def main():

    genesisBlock = Block.genesis()
    block = Block.mineBlock(genesisBlock, "foo")
    print(block)

if __name__ == '__main__':
    main()