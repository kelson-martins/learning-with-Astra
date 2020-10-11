# Learning with Astra #

This repository is a fork of [learning-with-astra](https://github.com/bettinaswynnerton/learning-with-Astra) repository, created so to get hands-on experience with cassandra databases.

## Use case

A simple Pomodoro tracking app written in Python, with data stored in Cassandra via Astra.

The app uses a standard Pomodoro of 25 minutes. Once executed, the app will record the current time as the end of a Pomodoro session, while also recording the start time ( (current time) - 25 minutes).

DB Connection is on .gitignore to preserve credentials. The source can be fetched [here](https://github.com/DataStax-Academy/workshop-crud-with-python-and-node/blob/5b01543a18ba31d6fddc9953dc458c96aadab220/crud-python/Ex02_Connect_to_Cassandra.py).

## Tables

Project Tables

```
CREATE TABLE IF NOT EXISTS pomodoro_by_user (
	user_id uuid,
	start_time timestamp,
	end_time timestamp,	
	task text,
	category text,
	comments text,	
    PRIMARY KEY (user_id, end_time)
);
```

```
use pomodoro;
token@cqlsh:pomodoro> describe tables;
pomodoro_by_user
```

## Excution Sample

```
python insert_pomodoro.py  "Cassandra" "Certifications Studies"
Pomodoro recorded

Start Time: 2020-10-11 10:50:57.986745
End Time: 2020-10-11 11:15:57.986745
Closing connection (up to 10s)
```

## Selecting Data

Here some example data that we used in the workshop:

```
 select * from pomodoro_by_user;

 user_id                              | end_time                        | category               | comments | start_time                      | task
--------------------------------------+---------------------------------+------------------------+----------+---------------------------------+-----------
 230995ee-c697-11ea-b7a1-8c85907c08dd | 2020-10-11 11:14:45.438000+0000 | Certifications Studies |     null | 2020-10-11 10:49:45.438000+0000 | Cassandra

```