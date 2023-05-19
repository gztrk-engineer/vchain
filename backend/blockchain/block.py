import time
from backend.utils.crypto_hash import cryptoHash

GENESIS_DATA = {
    "timestamp": 1,
    "lastHash": "genesisLastHash",
    "hash": "genesisHash",
    "data": [],
    "difficulty": 3,
    "nonce": "genesisNonce"
}

class Block:
    """
    Block: a unit of storage
    Store blocks ina chain that supports the cryptocurrency
    """

    def __init__(self, timestamp, lastHash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.lastHash = lastHash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'lastHash: {self.lastHash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce})'
        )

    @staticmethod
    def mineBlock(lastBlock, data):
        """
        Mine a block based on the given lastBlock and data
        Until it find a block hash that meets the PoW requirement
        """
        timestamp = time.time_ns()
        lastHash = lastBlock.hash
        difficulty = lastBlock.difficulty
        nonce = 0
        hash = cryptoHash(timestamp, lastHash, data, difficulty, nonce)
        while hash[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            hash = cryptoHash(timestamp, lastHash, data, difficulty, nonce)
        return Block(timestamp, lastHash, hash, data, difficulty, nonce)

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