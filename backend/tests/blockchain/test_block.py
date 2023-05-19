from backend.blockchain.block import Block, GENESIS_DATA

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
