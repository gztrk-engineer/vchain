import time


from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from pubnub.exceptions import PubNubException


from backend.pskeys import subscribeKey, publishKey

pnConfig = PNConfiguration()
pnConfig.subscribe_key = subscribeKey
pnConfig.publish_key = publishKey
# pnConfig.user_id = "my-user-id-vissaly"
# pubnub = PubNub(pnConfig)

# print(pnConfig.__dict__)
# // This will send a network request to the online public application in the pub sub network, informing that
# // this public instance that we have instantiated is now subscribe to all rather is now subscribed
# // to all the designated channels.
# // See pubnub.subscribe() first.
# Define a method to occur as response to a message event on the subscribe channel
# messageObject - specific event around the subscribed channel

TEST_CHANNEL = "TEST_CHANNEL"
testMessage = {"foo": "bar"}

class Listener(SubscribeCallback):
    def message(self, pubnub, messageObject):
        # print("inside message()")
        print(f"\n--- Incoming data---")
        print(f"Channel: {messageObject.channel}")
        print(f"Message: {messageObject.message}")
        print("*" * 20 )

class PubSub():
    """
    Handles the publish / subscribe layer of the application
    Provides the comm between the nodes on the blockchain network
    """
    def __init__(self):
        self.pubnub = PubNub(pnConfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, data):
        self.pubnub.publish().channel(channel).message(data).sync()
        # self.pubnub.publish().channel((TEST_CHANNEL)).message(data).sync()

def main():
    # print("inside main")
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(TEST_CHANNEL, testMessage)
    # pubnub.publish().channel((TEST_CHANNEL)).message(data).sync()

    
if __name__ == "__main__":
    main()