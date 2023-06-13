import time


from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.exceptions import PubNubException
from pubnub.callbacks import SubscribeCallback


from backend.pskeys import subscribeKey, publishKey

pnConfig = PNConfiguration()
pnConfig.subscribe_key = subscribeKey
pnConfig.publish_key = publishKey
# pnConfig.user_id = "my-user-id-vissaly"
pubnub = PubNub(pnConfig)

# print(pnConfig.__dict__)
# // This will send a network request to the online public application in the pub sub network, informing that
# // this public instance that we have instantiated is now subscribe to all rather is now subscribed
# // to all the designated channels.
# // See pubnub.subscribe() first.
# Define a method to occur as response to a message event on the subscribe channel
# messageObject - specific event around the subscribed channel

TEST_CHANNEL = "TEST_CHANNEL"
data = {"foo": "bar"}

# print("before subscribe")

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

# print("after subscribe")

class Listener(SubscribeCallback):
    # print("inside listener")
    # time.sleep(2)
    def message(self, pubnub, messageObject):
        # print("inside message()")
        print(f"\n--- Incoming message object: {messageObject}")

# time.sleep(2)
# print("before initializng the listener")
listener = Listener()

# print("before add listener")
pubnub.add_listener(listener)
# time.sleep(2)
# print("after adding listener")
# print(__name__ == "__main__")

def main():
    # print("inside main")
    time.sleep(1)
    pubnub.publish().channel((TEST_CHANNEL)).message(data).sync()

    
if __name__ == "__main__":
    main()