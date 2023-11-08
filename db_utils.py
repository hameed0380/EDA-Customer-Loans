import yaml
from sqlalchemy import create_engine
import pandas as pd
import psycopg2


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

    def initialise_engine(self):
        '''initialises a SQLAlchemy engine from the credentials provided from class'''
        # dictionary 
        creds = self.loaded_creds

        DATABASE_TYPE = 'postgresql'
        HOST = creds["RDS_HOST"]
        PASSWORD = ["RDS_PASSWORD"]
        USER = ["RDS_USER"]
        DATABASE = ["RDS_DATABASE"]
        PORT = 5432

        engine = create_engine(f"{DATABASE_TYPE}+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        return engine
    
    def extract_dataframe(self):
        pass



def load_file():
    '''Load  credentials file to access the database'''
    with open('credentials.yaml', 'r') as file:
        credential = yaml.safe_load(file)
    print(credential)
    return credential


if __name__ == '__main__':
    # Load credentials from your YAML file
    credentionals_passed = load_file()
    RDSDatabaseConnector(credentionals_passed).initialise_engine()

