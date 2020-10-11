#!/usr/bin/env python3
from db_connection import Connection
import uuid
import sys
from datetime import datetime, timedelta

def unix_time(dt):
    epoch = datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()

def unix_time_millis(dt):
    return int(unix_time(dt) * 1000.0)

def insert_pomodoro(user_id, start_time, end_time, task, category):

    formatted_start_time = unix_time_millis(start_time)
    formatted_end_time = unix_time_millis(end_time)

    try:
        connection = Connection()
        output = connection.session.execute(
            "INSERT INTO pomodoro_by_user (user_id, start_time, end_time, task, category) VALUES (%s,%s,%s,%s,%s)",
            [user_id, formatted_start_time , formatted_end_time, task, category]
        )
    except Exception as e: 
        print(e)
        print('Failure')
    else:
        print('Pomodoro recorded')
        print('Start Time: {}'.format(start_time))
        print('End Time: {}'.format(end_time))
        print('Closing connection (up to 10s)')
    finally:
        connection.close()
    print('========================================')


if __name__ == "__main__":
    
    user_id = uuid.UUID('230995ee-c697-11ea-b7a1-8c85907c08dd')

    # Cassadra timestamp is milliseconds since epoch 
    # https://stackoverflow.com/questions/16532566/how-to-insert-a-datetime-into-a-cassandra-1-2-timestamp-column
    end_time = datetime.now()
    start_time = end_time - timedelta(minutes=25)

    task = sys.argv[1]
    category = sys.argv[2]

    insert_pomodoro(user_id, start_time, end_time, task, category)

