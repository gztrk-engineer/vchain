import hashlib
import json

def cryptoHash(*args):
    """
    Return a SHA256 hash of the given arguments
    """
    # stringifiedData = json.dumps(args)
    # stringifiedArgs = map(stringify, args)
    stringifiedArgs = sorted(map(lambda data: json.dumps(data), args))
    # print(f'args: {args}')
    # joinedData = "".join(args)
    # print(f'args: {stringifiedArgs}')
    joinedData = "".join(stringifiedArgs)
    # print(f'joinedData: {joinedData}')

    return hashlib.sha256(joinedData.encode('utf-8')).hexdigest()

def main():
    print( f'Cryptohash ("one", 2, [3]): {cryptoHash("one", 2, [3])}' )
    print( f'Cryptohash (2, "one", [3]): {cryptoHash(2, "one", [3])}' )

if __name__ == "__main__":
    main()
