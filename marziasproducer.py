# This script connects to Kafka and sends response messages dictionary as topic
import json
import traceback
from kafka import KafkaProducer



producer = KafkaProducer(
bootstrap_servers="kafka-marzia-azam-9f68.aivencloud.com:28388",
security_protocol="SSL",
ssl_cafile="ca.pem",
ssl_certfile="service.cert",
ssl_keyfile="service.key",
)



def produce_message(status_json, topic):
    try:
        message =  str(json.dumps(status_json))
        producer.send(topic,message.encode("utf-8"))
        # Force sending of all messages
        producer.flush()
    except:
        print(traceback.print_exc())
