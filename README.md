# kafkaPG


#Quick start:

Clone repo and run getset.sh


#Dependencies

KafkaPG requires at least Python 3.6

#Supported Operating Systems

KafkaPG is developed and tested on Linux and Windows 10.

#Database

The tool inserts into a PostgreSQL Database which is expected to run elsewhere. You can make the requried table like this:


CREATE DATABASE MarziasKafka;

USE MarziasKafka;

CREATE TABLE kafkadata (
    id UUID PRIMARY KEY,
    time TIMESTAMP with time zone;),
    response_time SMALLINT,
    status_code SMALLINT,
);

The instruction is also in postgresql.txt so this step can be automated in the future.

#Installation

On Linux you can simply install the requirements and run KafkaPG.py directly from the repository. On Ubuntu you may need to first install libpq-dev:


sudo apt install libpq-dev

I have also made a script called getset.sh which can be run to install this and other dependencies which may be required on differernt Systems.
After pulling the repo:

cd KafkaPG

bash getset.sh

pip install -r requirements.txt

python3 makedb.py

python3 KafkaPG.py


#License

kafkaPG is licensed under MIT
