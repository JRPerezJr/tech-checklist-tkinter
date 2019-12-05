import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts_list (id INTEGER PRIMARY KEY, repair_order text, vin_number text, part_desc text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts_list")
        rows = self.cur.fetchall()
        return rows

    def insert(self, repair_order, vin_number, part_desc, price):
        self.cur.execute("INSERT INTO parts_list VALUES (NULL, ?, ?, ?, ?)",
                         (repair_order, vin_number, part_desc, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts_list WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, repair_order, vin_number, part_desc, price):
        self.cur.execute("UPDATE parts_list SET repair_order = ?, vin_number = ?, part_desc = ?, price = ? WHERE id = ?",
                         (repair_order, vin_number, part_desc, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
