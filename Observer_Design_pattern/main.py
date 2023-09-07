from channel import Channel
from Subscriber import Subscribers

mihirshah = Channel()

s1 = Subscribers("Deep")
s2 = Subscribers("Arti")
s3 = Subscribers("Kishore")

mihirshah.register(s1)
mihirshah.register(s2)
mihirshah.register(s3)

s1.subscribe(mihirshah)
s2.subscribe(mihirshah)
s3.subscribe(mihirshah)


mihirshah.upload("New Video")