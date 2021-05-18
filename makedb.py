from psycopg2.extras import RealDictCursor
import psycopg2

uri = "postgres://user:password@db.aivencloud.com:28386/defaultdb?sslmode=require"
db_conn = psycopg2.connect(uri)
c = db_conn.cursor(cursor_factory=RealDictCursor)

sql = """CREATE DATABASE MarziasKafkaThing;

USE MarziasKafkaThing;

CREATE TABLE kafkadata (
    id UUID PRIMARY KEY,
    time TIMESTAMP with time zone;),
    response_time SMALLINT,
    status_code SMALLINT,
);"""

c.execute("SELECT 1 = 1")
result = c.fetchone()
