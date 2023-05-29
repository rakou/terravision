from . import _OnPrem


class _Database(_OnPrem):
    _type = "database"
    _icon_dir = "resource_images/onprem/database"


class Cassandra(_Database):
    _icon = "cassandra.png"


class Clickhouse(_Database):
    _icon = "clickhouse.png"


class Cockroachdb(_Database):
    _icon = "cockroachdb.png"


class Couchbase(_Database):
    _icon = "couchbase.png"


class Couchdb(_Database):
    _icon = "couchdb.png"


class Dgraph(_Database):
    _icon = "dgraph.png"


class Druid(_Database):
    _icon = "druid.png"


class Hbase(_Database):
    _icon = "hbase.png"


class Influxdb(_Database):
    _icon = "influxdb.png"


class Janusgraph(_Database):
    _icon = "janusgraph.png"


class Mariadb(_Database):
    _icon = "mariadb.png"


class Mongodb(_Database):
    _icon = "mongodb.png"


class Mssql(_Database):
    _icon = "mssql.png"


class Mysql(_Database):
    _icon = "mysql.png"


class Neo4J(_Database):
    _icon = "neo4j.png"


class Oracle(_Database):
    _icon = "oracle.png"


class Postgresql(_Database):
    _icon = "postgresql.png"


class Scylla(_Database):
    _icon = "scylla.png"


# Aliases

ClickHouse = Clickhouse
CockroachDB = Cockroachdb
CouchDB = Couchdb
HBase = Hbase
InfluxDB = Influxdb
JanusGraph = Janusgraph
MariaDB = Mariadb
MongoDB = Mongodb
MSSQL = Mssql
MySQL = Mysql
PostgreSQL = Postgresql
