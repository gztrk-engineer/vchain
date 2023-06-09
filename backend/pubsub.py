import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

from backend.pskeys import subscribeKey, publishKey

pnConfig = PNConfiguration()
pnConfig.subscribe_key = subscribeKey
pnConfig.publish_key = publishKey

# Optimization for broadcasting blocks
# Previous state - pubsub01 backup
CHANNELS = {
    "TEST": "TEST",
    "BLOCK": "BLOCK"
}

testMessage = {"foo": "bar"}

class Listener(SubscribeCallback):
    def message(self, pubnub, messageObject):
        print(f"\n--- Incoming data---")
        print(f"Channel: {messageObject.channel}")
        print(f"Message: {messageObject.message}")
        print("*" * 20)

class PubSub():
    """
    Handles the publish / subscribe layer of the application
    Provides the comm between the nodes on the blockchain network
    """
    def __init__(self):
        self.pubnub = PubNub(pnConfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, data):
        self.pubnub.publish().channel(channel).message(data).sync()

    def broadcastBlock(self, block):
        """
        Broadcast a Block object to all nodes
        """
        # print(CHANNELS['BL'])
        self.publish(CHANNELS["BLOCK"], block.toJson())



def main():
    # print("inside main")
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(CHANNELS["TEST"], testMessage)

    
if __name__ == "__main__":
    main()