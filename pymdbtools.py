import os
from pandas import DataFrame
import json
import re
from subprocess import check_output


class Mdb:
    def __init__(self, filepath: str) -> None:
        self.filepath = os.path.abspath(filepath)
        assert os.path.exists(self.filepath)
        self._queries = check_output(
            ["mdb-queries", self.filepath], encoding="utf8").strip().split(" ")

    def __repr__(self) -> str:
        return f"<MDB file containing tables: {self.tables}>"

    @property
    def schema(self):
        schema = check_output(["mdb-schema", self.filepath], encoding="utf8")
        return re.search(r"(CREATE [\s\S]*)", schema)[1].strip().split("\n\n")

    @property
    def tables(self):
        return(check_output(["mdb-tables", self.filepath], encoding="utf8").strip().split(" "))

    @property
    def ver(self):
        return(check_output(["mdb-ver", self.filepath], encoding="utf8"))

    def count(self, table: str):
        if table not in self.tables:
            raise Exception("table not exists.")
        return check_output(["mdb-count", self.filepath], encoding="utf8")

    def json(self, table, *, date_format=None, datetime_format=None, no_unprintable=None):
        if table not in self.tables:
            raise Exception("table not exists.")
        content = check_output(
            ["mdb-json", self.filepath, table], encoding="utf8").strip()
        content = "[" + ",".join(content.splitlines()) + "]"
        return json.loads(content)

    def export(self, table, *, header=None, delimiter=None, row_delimiter=None, no_qoute=None,
               escape=None, escape_invisible=None, namespace=None, batch_size=None, date_format=None,
               datetime_format=None, null=None, bin=None, boolean_words=None, export_path=None, encoding="utf8"):
        # 后面再考虑完善
        if table not in self.tables:
            raise Exception("table not exists.")
        content = check_output(
            ["mdb-export", self.filepath, table], encoding="utf8")
        export_path = f"{table}.csv" if not export_path else export_path
        with open(export_path, mode="wt", encoding=encoding) as f:
            f.write(content)

    def sql(self):
        raise Exception("It seems that you are an advanced player, you got wrong place bro.")

    def prop(self, table_name, col_name):
        # 后面会考虑结构化
        cmds = ["mdb-prop", table_name]
        if col_name:
            cmds.append(col_name)
        return check_output(cmds, encoding="utf8")

    def queries(self, query_name, *, list=False, newline=None, delimiter=None):
        if list:
            return self._queries
        if query_name not in self._queries:
            raise Exception("queries not exists.")
        return check_output(["mdb-queries", query_name], encoding="utf8").strip()

    def to_df(self, table):
        return DataFrame(self.json(table=table))
    
    def export_all(self, **kwargs):
        for table in self.tables:
            self.export(table=table, **kwargs)

if __name__ == "__main__":
    pass
