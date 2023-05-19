



import time
from backend.blockchain.block import Block, GENESIS_DATA
from backend.config import MINE_RATE, SECONDS

def testMineBlock():
    lastBlock = Block.genesis()
    data = "test-data"
    block = Block.mineBlock(lastBlock, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.lastHash == lastBlock.hash
    assert block.hash[:block.difficulty] == "0" * block.difficulty


def testGenesis():
    genesis = Block.genesis()
    assert isinstance(genesis, Block)
    for key, value in GENESIS_DATA.items():
        assert getattr(genesis, key) == GENESIS_DATA[key]
    # assert genesis.timestamp == GENESIS_DATA['timestamp']
    # assert genesis.lastHash == GENESIS_DATA['lastHash']
    # assert genesis.hash == GENESIS_DATA['hash']
    # assert genesis.data == GENESIS_DATA['data']

def testQuickMinedBlock():
    lastBlock = Block.mineBlock(Block.genesis(), "foo")
    nextBlock = Block.mineBlock(lastBlock, "bar")
    assert nextBlock.difficulty == lastBlock.difficulty + 1

def testSlowMinedBlock():
    lastBlock = Block.mineBlock(Block.genesis(), "foo")
    time.sleep(MINE_RATE / SECONDS)
    nextBlock = Block.mineBlock(lastBlock, "bar")
    assert nextBlock.difficulty == lastBlock.difficulty - 1

def testDifficultyLevelAt1():
    lastBlock = Block(
        time.time_ns(),
        'testLastHash',
        'testHash',
        'testData',
        1,
        0
    )
    time.sleep(MINE_RATE / SECONDS)
    nextBlock = Block.mineBlock(lastBlock, "bar")
    assert nextBlock.difficulty == 1