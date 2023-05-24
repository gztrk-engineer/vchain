import time


from backend.utils.crypto_hash import cryptoHash
from backend.utils.hex2bin import hexToBinary
from backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp': 1,
    'lastHash': 'genesis_last_hash',
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

        while hexToBinary(hash)[0:difficulty] != '0' * difficulty:
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

    @staticmethod
    def isValidBlock(lastBlock, block):
        """
        Validate a block by enforcing rules
          * Must have a proper lastHash reference
          * Must meet the proof of work requirement
          * Difficulty must adjust by 1
          * Valid block hash
        """

        if block.lastHash != lastBlock.hash:
            raise Exception("last_hash must be correct")
        if hexToBinary(block.hash)[0:block.difficulty] != "0"* block.difficulty:
            raise Exception("The proof of work requirement was not met")
        if abs(lastBlock.difficulty - block.difficulty) != 1:
            raise Exception("The block difficulty must only adjust by 1")

        reconstructedHash = cryptoHash(
            block.timestamp,
            block.lastHash,
            block.data,
            block.nonce,
            block.difficulty
        )

        if block.hash != reconstructedHash:
            raise Exception("The black hash must be valid")


if __name__ == "__main__":
    genesisBlock = Block.genesis()
    badBlock = Block.mineBlock(genesisBlock, "foo")
    # badBlock.lastHash = "evilHash"
    try:
        Block.isValidBlock(badBlock, genesisBlock)
    except Exception as e:
        print(f"Is valid block: {e}")
    # Block.isValidBlock(badBlock, genesisBlock)
    # block = Block.mineBlock(genesis_block, 'foo')
    # print(block)




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