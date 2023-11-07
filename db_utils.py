import yaml
from sqlalchemy import create_engine


class RDSDatabaseConnector:

    def __init__(self, credential) -> None:
        self.loaded_creds = credential

    # def show_creds(self):
    #     print(self.loaded_creds)

# template ideas

# DATABASE_TYPE = 'postgresql'
# DBAPI = 'psycopg2'
# HOST = 'localhost'
# USER = 'postgres'
# PASSWORD = #'password'
# DATABASE = 'pagila'
# PORT = 5432
# engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

    # initialises a SQLAlchemy engine from the credentials provided from class
    def initialise_engine(self):
        
        # dictionary 
        creds = self.credential

        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = creds["RDS_HOST"]
        PASSWORD = ["RDS_PASSWORD"]
        USER = ["RDS_USER"]
        DATABASE = ["RDS_DATABASE"]
        PORT = ["RDS_PORT"]

        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        return engine





def load_file():
    with open('credentials.yaml', 'r') as file:
        credential = yaml.safe_load(file)
    print(credential)
    return credential


#load_file()
credentionals_passed = load_file()
# RDSDatabaseConnector(credentionals_passed).show_creds()