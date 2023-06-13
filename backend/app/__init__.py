from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain


app = Flask(__name__)
blockchain = Blockchain()
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

    return jsonify(blockchain.chain[-1].toJson())


app.run()