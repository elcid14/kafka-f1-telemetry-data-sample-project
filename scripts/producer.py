from confluent_kafka import Producer


p = Producer({'bootstrap.servers':'localhost:9092'})


# define callback function to handle serializing the data, running transformation


def deliver_telem_data(err, msg):
    if err is not None:
        print('message failed to deliver: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
        


