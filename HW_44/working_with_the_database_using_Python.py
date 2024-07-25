import sqlite3
from abc import ABC


class Record:
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Record(id={self.id}, name='{self.name}', age={self.age}, salary={self.salary})"


class BaseRepository(ABC):
    def __init__(self, db_path):
        self._connection = sqlite3.connect(db_path)
        self._cursor = self._connection.cursor()

    def close(self):
        if self._connection:
            self._cursor.close()
            self._connection.close()

    @staticmethod
    def _row2obj(row):
        return Record(*row)

    @staticmethod
    def _rows2obj(rows):
        return [DataRepository._row2obj(row) for row in rows]


class DataRepository(BaseRepository):
    table_name = 'records'

    def __init__(self, db_path):
        super().__init__(db_path)
        self._cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, salary REAL);')

    def add_record(self, record):
        self._cursor.execute("INSERT INTO records (id, name, age, salary) VALUES (?, ?, ?, ?)",
                             (record.id, record.name, record.age, record.salary))
        self._connection.commit()

    def add_records(self, records):
        self._cursor.executemany("INSERT INTO records (id, name, age, salary) VALUES (?, ?, ?, ?)",
                                 [(record.id, record.name, record.age, record.salary) for record in records])
        self._connection.commit()

    def get_all(self):
        self._cursor.execute(f'SELECT * FROM {self.table_name};')
        return DataRepository._rows2obj(self._cursor.fetchall())

    def update_records(self, set_clause, condition, params=None):
        self._cursor.execute(f"UPDATE records SET {set_clause} WHERE {condition}", params or [])
        self._connection.commit()

    def get_records_by_condition(self, condition, params=None):
        self._cursor.execute(f"SELECT * FROM records WHERE {condition}", params or [])
        return DataRepository._rows2obj(self._cursor.fetchall())

    def delete_records_by_condition(self, condition, params=None):
        self._cursor.execute(f"DELETE FROM records WHERE {condition}", params or [])
        self._connection.commit()


record_repo = DataRepository('data.db')

record_repo.delete_records_by_condition("TRUE")
print(record_repo.get_all())

record1 = Record(1, 'Vasya', 25, 5000)
record2 = Record(2, 'Petya', 30, 6000)
record3 = Record(3, 'Andrey', 35, 7000)
record4 = Record(4, 'Genadiy', 40, 8000)
record_repo.add_record(record1)
record_repo.add_records([record2, record3, record4])
print(record_repo.get_all())

record_repo.update_records(set_clause="salary = ?", condition="name = ?", params=[3000, 'Vasya'])
print(record_repo.get_all())

filtered_records = record_repo.get_records_by_condition(condition="salary > ?", params=[6000])
print(filtered_records)

record_repo.delete_records_by_condition(condition="name = ?", params=['Vasya'])
print(record_repo.get_all())