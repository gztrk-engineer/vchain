from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain


app = Flask(__name__)
blockchain = Blockchain()
for i in range(3):
    blockchain.addBlock(i+1)
print(blockchain.__repr__())

@app.route("/")
def routeDefault():
    return "Welcome to blockchain"

@app.route("/blockchain")
def routeBlockchain():
    return jsonify(blockchain.toJson())
    # return blockchain.__repr__()
    # return blockchain.chain



app.run()