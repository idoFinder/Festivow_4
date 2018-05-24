import pymysql


class SQLdb:
    def __init__(self):
        self.dataBase = pymysql.connect(host="localhost", port=3306, user="root", password="150492", db="test")
        self.cursor = self.dataBase.cursor()


    def insert(self, table, id, name, cost):
        query = "INSERT INTO %s(id,name,cost) VALUES(%d,\"%s\",\"%s\")" % (table, id, name, cost)
        try:
            self.cursor.execute(query)
            self.dataBase.commit()

        except Exception:
            print(Exception)
            self.dataBase.rollback()

        finally:
            self.dataBase.close()

    def update(self, table, id, column, newValue):
        query = "UPDATE %s SET %s = %s WHERE id = %d" % (table, column, newValue, id)
        try:
            self.cursor.execute(query)
            self.dataBase.commit()

        except Exception:
            print(Exception)
            self.dataBase.rollback()

        finally:
            self.dataBase.close()

    def delete(self, table, column, key):
        query = "DELETE FROM %s WHERE %s = \"%s\"" % (table, column, key)
        try:
            self.cursor.execute(query)
            self.dataBase.commit()

        except Exception:
            print(Exception)
            self.dataBase.rollback()

        finally:
            self.dataBase.close()

db = SQLdb()
db.delete('items', 'id', '7777')


