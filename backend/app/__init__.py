import os
import random
# import socket

from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub


app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub()
print(blockchain.__repr__())

@app.route("/")
def routeDefault():
    return "Welcome to blockchain"

@app.route("/blockchain/")
def routeBlockchain():
    return jsonify(blockchain.toJson())
    # return blockchain.__repr__()
    # return blockchain.chain


@app.route("/blockchain/mine/")
def routeBlockchainMine():
    transactionData = "example-transaction-data"
    blockchain.addBlock(transactionData)
    block = blockchain.chain[-1]
    pubsub.broadcastBlock(block)

    return jsonify(block.toJson())

PORT = 5000

if os.environ.get('PEER') == "True":
    PORT = random.randint(5001, 6000)


app.run(port=PORT)