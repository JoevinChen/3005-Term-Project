import psycopg2

# Used to connect to database
class DatabaseConnect:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def get_conn(self):
        return self.conn

# Change as needed
db = DatabaseConnect('FitnessClubManagementSystem', 'postgres', 'postgres', 'localhost', '5432')