import time

from backend.utils.crypto_hash import cryptoHash
from backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}

class Block:
    """
    Block: a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """
    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce})'
        )

    @staticmethod
    def mineBlock(last_block, data):
        """
        Mine a block based on the given last_block and data, until a block hash
        is found that meets the leading 0's proof of work requirement.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        nonce = 0
        hash = cryptoHash(timestamp, last_hash, data, difficulty, nonce)

        while hash[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hash = cryptoHash(timestamp, last_hash, data, difficulty, nonce)

        return Block(timestamp, last_hash, hash, data, difficulty, nonce)

    @staticmethod
    def genesis():
        """
        Generate the genesis block.
        """
        return Block(**GENESIS_DATA)

    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        """
        Calculate the adjusted difficulty according to the MINE_RATE.
        Decrease the difficulty for slowly mined blocks.
        Increase the difficulty for quickly mined blocks.
        """
        if (new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1

        if (last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1

        return 1

if __name__ == "__main__":
    genesis_block = Block.genesis()
    block = Block.mineBlock(genesis_block, 'foo')
    print(block)




# import time
# from backend.utils.crypto_hash import cryptoHash
# from backend.config import MINE_RATE, SECONDS
#
# GENESIS_DATA = {
#     "timestamp": 1,
#     "lastHash": "genesisLastHash",
#     "hash": "genesisHash",
#     "data": [],
#     "difficulty": 3,
#     "nonce": "genesisNonce"
# }
#
# class Block:
#     """
#     Block: a unit of storage
#     Store blocks ina chain that supports the cryptocurrency
#     """
#
#     def __init__(self, timestamp, lastHash, hash, data, difficulty, nonce):
#         self.timestamp = timestamp
#         self.lastHash = lastHash
#         self.hash = hash
#         self.data = data
#         self.difficulty = difficulty
#         self.nonce = nonce
#
#     def __repr__(self):
#         return (
#             'Block('
#             f'timestamp: {self.timestamp}, '
#             f'lastHash: {self.lastHash}, '
#             f'hash: {self.hash}, '
#             f'data: {self.data}, '
#             f'difficulty: {self.difficulty}, '
#             f'nonce: {self.nonce})'
#         )
#
#     @staticmethod
#     def mineBlock(lastBlock, data):
#         """
#         Mine a block based on the given lastBlock and data
#         Until it find a block hash that meets the PoW requirement
#         """
#         timestamp = time.time_ns()
#         lastHash = lastBlock.hash
#         difficulty = Block.adjustDifficulty(lastBlock, timestamp)
#         nonce = 0
#         hash = cryptoHash(timestamp, lastHash, data, difficulty, nonce)
#         while hash[0:difficulty] != '0' * difficulty:
#             nonce += 1
#             timestamp = time.time_ns()
#             hash = cryptoHash(timestamp, lastHash, data, difficulty, nonce)
#         return Block(timestamp, lastHash, hash, data, difficulty, nonce)
#
#     @staticmethod
#     def genesis():
#         return Block(**GENESIS_DATA)
#         # return Block(
#         #     GENESIS_DATA["timestamp"],
#         #     GENESIS_DATA["lastHash"],
#         #     GENESIS_DATA["hash"],
#         #     GENESIS_DATA["data"]
#         # )
#
#     @staticmethod
#     def adjustDifficulty(lastBlock, newTimestamp):
#         """
#         Calculate the adjusted difficulty according to the MINE_RATE
#         """
#         if (newTimestamp - lastBlock.timestamp) < MINE_RATE:
#             return lastBlock.difficulty + 1
#         if (lastBlock.difficulty - 1) > 0:
#             return lastBlock.difficulty - 1
#         return 1
#
#
#
# def main():
#
#     genesisBlock = Block.genesis()
#     block = Block.mineBlock(genesisBlock, "foo")
#     print(block)
#
# if __name__ == '__main__':
#     main()