from sqlalchemy import create_engine

class PostgresConnection:
    def __init__(self):
        self.engine = create_engine("postgresql+psycopg2://admin:root@localhost:5455/postgres")



