# README

This is a small toy created for my friend. It makes happy if this script also help you. Feel free to pull any issue!

⚠️: Currently, I do not implement all the feature you may need. Just feel free to pull you issue!

## How to install

1. Install mdbtools (technically, this script is just a wrapper of mdbtools)

    [The true Hero!](https://github.com/mdbtools/mdbtools)

2. Just shut up and take this script

## How to use in your python

1. import it into your main script

```python
from pymdbtools import Mdb
```

2. construct a Mdb Object using the path to you mdb file.

```python
my_mdb = Mdb("./path/to/your/mdb_file.mdb")
```

3. what you can do:

* check schema

```python
my_mdb.schema
```

* check tables in your file

```python
my_mdb.tables
```

* check your mdb version

```python
my_mdb.ver
```

* check count (actually, I do not know what it is.)

```python
my_mdb.count(table=table_name)
```

* translate one table into json (actually, dict in python)

```python
my_mdb.json(table=table_name)
```

* export to csv file.

```python
my_mdb.export(table=table_name)
```

* check properties

col_name is optional.

```python
my_mdb.prop(table_name=table_name, col_name=col_name)
```

* check queries

```python
# list queries
my_mdb.queries(list=True)

# check queries
my_mdb.queries(query_name=table_name)
```

* translate into pandas DataFrame

```python
df = my_mdb.to_df(table=table_name)
```

* export all tables

```python
my_mdb.export_all()
```
