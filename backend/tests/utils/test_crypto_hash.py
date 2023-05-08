from backend.utils.crypto_hash import cryptoHash

def testCryptoHash():
    # Accepts different data types
    # The hash value doesn't depend on the args order
    assert cryptoHash(1, [2], "three") == cryptoHash([2], "three", 1)
    assert cryptoHash("foo") == "abcde"