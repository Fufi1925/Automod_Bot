import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, **columns):
        columns_with_types = [f'{col} {col_type}' for col, col_type in columns.items()]
        sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({", ".join(columns_with_types)})'
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, table_name, **values):
        columns = ', '.join(values.keys())
        placeholders = ', '.join('?' for _ in values)
        sql = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
        self.cursor.execute(sql, tuple(values.values()))
        self.connection.commit()

    def query(self, sql, params=None):
        if params is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
