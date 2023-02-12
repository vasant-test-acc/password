class UseMySQL:
    # Importing MySQLdb and as a smaller name for reusing it.
    # To install MySQL Python connection use below command:
    # pip install mysqlclient
    import MySQLdb as _mysql

    def __init__(self, host, user, password, db):
        """
        Initializing MySQL details in init method.

        Args:
            self
            host: Host name of the machine.
            user: Username of mySQL DB.
            password: Password of mySQL DB.
            db: Database name of mySQL DB.
        """
        self._host = host
        self._user = user
        self._password = password
        self._db = db

    def __enter__(self):
        """
        This data model/dunder method is used
        to employ auto open of my sql connection
        and cursor inside 'with' and in turn
        close them inside the same with the help
        of exit method in order to avoid not so
        closed database connections.

        Args:
            self

        Returns:
            self.cursor
        """
        self._conn = self._mysql.connect(
            host=self._host, user=self._user, passwd=self._password, db=self._db)
        self.cursor = self._conn.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, traceback):
        """
        This data model/dunder method is used to employ
        auto close of connection and cursor as with block ends.

        Args:
            self
            exception_type: Type of Exception.
            exception_value: Exception Value.
            traceback: Traceback value.
        """
        self.cursor.close()
        self._conn.close()


with UseMySQL(host="localhost", user="admin", password="test", db="sakila") as mySqlObj:
    cursor = mySqlObj
    cursor.execute("SELECT * FROM ACTOR")
    for tup1 in cursor.fetchall():
        print(tup1)
