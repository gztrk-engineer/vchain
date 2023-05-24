import hashlib
import json

def cryptoHash(*args):
    """
    Return a SHA256 hash of the given arguments
    """
    stringifiedArgs = sorted(map(lambda data: json.dumps(data), args))
    joinedData = "".join(stringifiedArgs)

    return hashlib.sha256(joinedData.encode('utf-8')).hexdigest()

def main():
    print( f'Cryptohash ("one", 2, [3]): {cryptoHash("one", 2, [3])}' )
    print( f'Cryptohash (2, "one", [3]): {cryptoHash(2, "one", [3])}' )

if __name__ == "__main__":
    main()
