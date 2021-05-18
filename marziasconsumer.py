import json
from kafka import KafkaConsumer
import dbcon


consumer = KafkaConsumer(
    "kafka-marzia",
    auto_offset_reset="earliest",
    bootstrap_servers="kafka-marzia-azam-9f68.aivencloud.com:28388",
    client_id="demo-client-1",
    group_id="demo-group",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

def consume_and_send_to_db(table_name):
    """
    This script receives messages from a Kafka topic
    I have plagiarized how to make the consumer from the AIVEN docs
    """

    for _ in range(2):
        raw_msgs = consumer.poll(timeout_ms=1000)
        for tp, msgs in raw_msgs.items():
            for msg in msgs:
                dictpg = json.loads(msg.value)
                columns = ', '.join("`" + str(x).replace('*', '_') + "`" for x in dictpg.keys())
                values = ', '.join("'" + str(x).replace('*', '_') + "'" for x in dictpg.values())
                sql = "INSERT INTO `%s` ( %s ) VALUES ( %s );" % (table_name, columns, values)
                print(sql)
                #conn = dbcon.make_con(sql) # this method uses jsut dbcon, no seperate config file and is suitable for small prjects like this
                dbcon.connect(sql) # this uses database.ini config file, attached for completeness
                # Commit offsets so we won't get the same messages again
                consumer.commit()
