from confluent_kafka import Producer # type: ignore
import json


p = Producer({'bootstrap.servers':'localhost:9092'})


# define callback function to handle serializing the data, running transformation


def deliver_telem_data(err, msg):
    if err is not None:
        print('message failed to deliver: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
        

test_data = json.dumps([{"driver_number":1}, {"driver_number":2}])

p.poll(0)
p.produce('f1-telem-data', test_data, callback=deliver_telem_data)
    
p.flush()