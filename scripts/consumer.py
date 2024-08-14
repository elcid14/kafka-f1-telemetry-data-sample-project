from confluent_kafka import Consumer
import json
c = Consumer({
    'bootstrap.servers':'localhost:9092',
    'group.id':'f1-telem-consumer',
    'auto.offset.reset':'earliest'
})


c.subscribe(['f1-telem-data'])


while True:
    
    msg = c.poll(1)
    
    if msg is None:
        continue
    
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    msg_decode = msg.value().decode('utf-8')
    
    test_json = json.loads(msg_decode)
    
    print(test_json)