import yaml
from sqlalchemy import create_engine


class RDSDatabaseConnector:

    def __init__(self, credential) -> None:
        self.loaded_creds = credential

    # def show_creds(self):
    #     print(self.loaded_creds)






def load_file():
    with open('credentials.yaml', 'r') as file:
        credential = yaml.safe_load(file)
#    print(credential)
    return credential


#load_file()
credentionals_passed = load_file()
# RDSDatabaseConnector(credentionals_passed).show_creds()