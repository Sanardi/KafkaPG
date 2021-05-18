
import json
import time
import requests
import dbcon
import marziasproducer
import marziasconsumer


class KafkaPG:
    '''
    This Class lets you make requests to your chosen website and publishes the stauts codes
    as a Kafta Topic which is read by a consumer that puts it into Postgresql. THe default waiting
    time between requests in 300 seconds, or 5 minutes.
    THis can be overriden by passing waiting_time = <WHATEVER> when initializing the class
    '''

    def __init__(self, url = "https://datanalysis.ai", topic = "checking_website_availability", waiting_time = 300, table_name = "kafkadata"):

        self.url = url
        self.waiting_time = waiting_time
        self.topic = topic
        self.tableName = table_name

    def make_request(self):
        status_data = {}
        try:
            #acessing the website:'
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
            headers={'User-Agent':user_agent}
            r = requests.get(self.url, headers = headers)
            status_data["time"] = time.time()
            status_data["code"] = r.status_code
            status_data["response_time"] = r.elapsed.total_seconds()

            return status_data

        except Exception as e:
            print(e)

    def _consume(self):
        while True:
            marziasconsumer.consume_and_send_to_db(self.table_name)

    def _produce(self):
        while True:
            status_data = self.make_request()
            status_json = json.dumps(status_data)
            marziasproducer.produce_message(status_json, self.topic)

            time.sleep(self.waiting_time)

    def run(self):
        print("I will now check the status codes and send them to the kafta topic, then into Postgresql")
        while True:
            self._produce()
            self._consume()


if __name__ == '__main__':
    bla = KafkaPG()
    bla.run()
