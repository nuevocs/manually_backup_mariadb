# Manually create a backup csv file from a mariadb database

Since my paid remote database server does not allow me to create a backup via mysqldump, I decided to make a backup
manually retrieving data from the database and save it as a csv file.

### Prerequisites:

- Python 3.11.0+
- pandas==1.5.2
- SQLAlchemy==1.4.41

### Note:

- I would not suggest to retrieve a huge amount of data as it may be inefficient.
- A TOML file is used as en environment file.
- You may check available table names in a database before actually getting data from the database.
- It might work for MySQL databases, but did not try myself.

### TOML file format used:

```
[db]
    [db.mariadb]
        user=""
        pw=""
        host=""
        port=""
        db_name=""
```