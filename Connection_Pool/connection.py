# To try creating the connection pool of mysql connections and using them
import mysql.connector as mysql
MAX_POOL_SIZE = 10

class ConnectionPool:
    def __init__(self, poolSize):
        self.poolSize = poolSize
        self.connection_pool = []

        for i in range(poolSize):
            mysqlobj = mysql.connect(host='localhost', user='root',password='Vani@0306')
            self.connection_pool.append(mysqlobj)
        
        print("Connection Pool created successfully")
    
    def getConnection(self):
        if len(self.connection_pool) == 0:
            print("Connection Pool is empty")
            return None
        
        return self.connection_pool.pop()
    
    def closeConnection(self, connection):
        connection.close()
        self.connection_pool.append(connection)
        print("Connection closed successfully")

def main():
    connectionPool = ConnectionPool(MAX_POOL_SIZE)
    
    connection = connectionPool.getConnection()

    cursorobj = connection.cursor()
    cursorobj.execute('SELECT SLEEP(10);')

    print("Connection obtained successfully")
    connectionPool.closeConnection(connection)

main()