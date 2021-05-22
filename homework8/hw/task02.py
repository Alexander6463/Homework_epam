"""Write a wrapper class TableData for database table,
that when initialized with database name and table acts as
collection object (implements Collection protocol).
Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite',
table_name='presidents') then len(presidents) will give current
amount of rows in presidents table in database presidents['Yeltsin']
should return single data row for president with name Yeltsin
'Yeltsin' in presidents should return if president with same name exists in
table object implements iteration protocol. i.e. you could use it in for
loops:: for president in presidents: print(president['name'])
all above mentioned calls should reflect most recent data.
If data in table changed after you created collection instance,
your calls should return updated data.
Avoid reading entire table into memory. When iterating through records,
start reading the first record, then go to the next one, until
records are exhausted. When writing tests, it's not always neccessary
to mock database calls completely.
Use supplied example.sqlite file as database fixture file."""
import sqlite3


class TableData:
    def __init__(self, path, table_name):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.table_name = table_name

    def __getitem__(self, item):
        self.cursor.execute(f'SELECT * from {self.table_name} where name=?',
                            (item,))
        return tuple(self.cursor.fetchone())

    def __len__(self):
        self.cursor.execute(f'SELECT count(*) from {self.table_name}')
        return self.cursor.fetchone()[0]

    def __contains__(self, item):
        self.cursor.execute(f'SELECT * from {self.table_name} where name=?',
                            (item,))
        if self.cursor.fetchone() is not None:
            return True
        return False

    def __iter__(self):
        self.cursor.execute(f'SELECT * from {self.table_name}')
        return self

    def __next__(self):
        self.res = self.cursor.fetchone()
        if self.res is not None:
            return self.res
        else:
            raise StopIteration


if __name__ == '__main__':
    presidents = TableData('example.sqlite', 'presidents')
    print(presidents['Trump'])
    print(len(presidents))
    print('Trump' in presidents)
    print('Medvedev' in presidents)
    for president in presidents:
        print(president['name'])
