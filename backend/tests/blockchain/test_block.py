
import time
import pytest

from backend.blockchain.block import Block, GENESIS_DATA
from backend.utils.hex2bin import hexToBinary
from backend.config import MINE_RATE, SECONDS

def testMineBlock():
    lastBlock = Block.genesis()
    data = "test-data"
    block = Block.mineBlock(lastBlock, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.lastHash == lastBlock.hash
    assert hexToBinary(block.hash)[:block.difficulty] == "0" * block.difficulty


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

@pytest.fixture
def lastBlock():
    return Block.genesis()

@pytest.fixture
def block(lastBlock):
    return Block.mineBlock(lastBlock, "test_data")

def testIsValidBlock(lastBlock, block):
    Block.isValidBlock(lastBlock, block)

def testIsValidBlockBadLastHash(lastBlock, block):
    # lastBlock = Block.genesis()
    # block = Block.mineBlock(lastBlock, "test_data")
    block.lastHash = "evilHash"
    # Block.isValidBlock(lastBlock, block)
    # with pytest.raises(Exception):
    with pytest.raises(Exception, match="last_hash must be correct"):
        Block.isValidBlock(lastBlock, block)

def testIsValidBlockBadProofOfWork(lastBlock, block):
    block.hash = "fffff"
    with pytest.raises(Exception, match="The proof of work requirement was not met"):
        Block.isValidBlock(lastBlock, block)

def testIsValidBlockJumpedDifficulty(lastBlock, block):
    block.difficulty += 3
    jumpedDifficulty = block.difficulty
    block.hash = f'{"0" * jumpedDifficulty}111abc'
    print(f'\nLast block difficulty: {lastBlock.difficulty}')
    print(f'Next block difficulty: {block.difficulty}')
    with pytest.raises(Exception, match="The block difficulty must only adjust by 1"):
        Block.isValidBlock(lastBlock, block)

def testIsValidBlockBadBlockHash(lastBlock, block):
    block.hash = "000000000000000000123abc"
    with pytest.raises(Exception, match="The black hash must be valid"):
        Block.isValidBlock(lastBlock, block)