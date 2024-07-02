import sqlite3

class DatabaseManager:
    def __init__(self, db_name='data.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS api_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                primaryImage TEXT,
                objectDate TEXT,
                creditLine TEXT,
                country TEXT
            )
        ''')
        self.conn.commit()

    def insert_data(self, data):
        self.cursor.execute('''
            INSERT INTO api_data (title, primaryImage, objectDate, creditLine, country)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['title'], data['primaryImage'], data['objectDate'], data['creditLine'], data['country']))
        self.conn.commit()
        
    def print_table(self):
        self.cursor.execute('SELECT * FROM api_data')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def close_connection(self):
        self.conn.close()