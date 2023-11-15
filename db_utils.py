import yaml
from sqlalchemy import create_engine
import pandas as pd
import psycopg2


class RDSDatabaseConnector:

    def __init__(self, credential) -> None:
        self.loaded_creds = self.load_file(credential)
        self.engine = self.initialise_engine()

    # def show_creds(self):
    #     print(self.loaded_creds)

    def load_file(self, credential):
        '''Load credentials file to access the database
        
        Args:
            credential: path of the credentials file to connect to the database

        Returns:
            credential: returns a dict containing the credentials to
            connect to the database.
        '''
        with open(credential, 'r') as file:
            credential = yaml.safe_load(file)
        print(credential)
        return credential


    def initialise_engine(self):
        '''initialises a SQLAlchemy engine from the credentials provided from class'''
        # dictionary 
        creds = self.loaded_creds

        DATABASE_TYPE = 'postgresql'
        HOST = creds["RDS_HOST"]
        PASSWORD = creds["RDS_PASSWORD"]
        USER = creds["RDS_USER"]
        DATABASE = creds["RDS_DATABASE"]
        PORT = 5432

        engine = create_engine(f"{DATABASE_TYPE}+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        return engine
    
    def extract_data(self, table_name):
        '''Extracts the data from RDS database and returns it as a DataFrame.
        
        Args:
            table_name: name of the table we want to extract from
        Returns:
            data: returns the data we queried
        '''
        data = pd.read_sql_query(f"SELECT * FROM {table_name}", self.engine)
        return data
    
    def save_to_csv(self, data, credential):
        '''Save the data to a csv file'''
        data.to_csv(credential, index=False)

    def load_csv(self, data_csv):
        '''Load the data csv as a pandas dataframe'''
        df = pd.read_csv(data_csv)
        return df







if __name__ == '__main__':
    RDS_CONNECTOR = RDSDatabaseConnector('credentials.yaml')
    RDS_CONNECTOR.initialise_engine()
    data = RDS_CONNECTOR.extract_data('loan_payments')
    print(data.head())
    RDS_CONNECTOR.save_to_csv(data, 'data.csv')
    dataframe = RDS_CONNECTOR.load_csv('data.csv')
    print(dataframe)
    print(dataframe.shape)

