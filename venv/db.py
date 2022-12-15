import sqlite3

class DB:
    def __init__(self, name, ex_script, clearDB=False):
        self.name = name
        self.ex_script = ex_script
        self.connection = sqlite3.connect(name)
        self.cur = None
        self.createDB(clearDB)

    def createDB(self, clearDB):
        if clearDB:
            with open(self.ex_script) as f:
                self.connection.executescript(f.read())

        self.cur = self.connection.cursor()

    def Add(self, message: str):
        self.cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                         ("Log:", message)
                         )
        self.connection.commit()

    def __del__(self):
        self.connection.close()