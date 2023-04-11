import sqlite3


class Database:
    def __init__(self, path_to_db='data/main.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
            CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER,
    name varchar(255) ,
    phone integer,
    email varchar(255) ,
    type_visit varchar(255),
    is_payed INTEGER DEFAULT 0
);
        """
        self.execute(sql=sql, commit=True)

    def add_user(self, telegram_id: int, name: str, phone: int = None, email: str = None):
        sql = "INSERT INTO Users(telegram_id,name,phone,email) VALUES (?,?,?,?)"
        parameters = (telegram_id, name, phone, email)
        self.execute(sql, parameters=parameters, commit=True)

    def update_phone(self, phone, telegram_id):
        sql = 'UPDATE Users SET phone=? WHERE telegram_id=?'
        return self.execute(sql, parameters=(phone, telegram_id), commit=True)

    def update_email(self, email, telegram_id):
        sql = 'UPDATE Users SET email=? WHERE telegram_id=?'
        return self.execute(sql, parameters=(email, telegram_id), commit=True)

    def select_all_users(self):
        sql = "SELECT name,phone, email FROM Users WHERE is_payed ='1'"
        return self.execute(sql, fetchall=True)

    def exist_user(self, telegram_id):
        sql = "SELECT * FROM Users WHERE telegram_id=?"
        return self.execute(sql, parameters=(telegram_id,), fetchone=True)

    def update_is_pay(self, telegram_id):
        sql = "UPDATE Users SET is_payed=1 WHERE telegram_id=?"
        return self.execute(sql, parameters=(telegram_id,), commit=True)

    def update_type_visit(self, type_visit, telegram_id):
        sql = "UPDATE Users SET type_visit=? WHERE telegram_id=?"
        return self.execute(sql, parameters=(type_visit, telegram_id), commit=True)

    def select_ticket(self, telegram_id):
        sql = "SELECT * FROM Users WHERE telegram_id=? AND is_payed=1"
        return self.execute(sql, parameters=(telegram_id,), fetchone=True)

    def select_all_payed_user(self):
        sql = "SELECT * FROM Users WHERE is_payed=1 AND type_visit='offline'"
        return self.execute(sql, fetchall=True)


