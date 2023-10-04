from db_handler import MsSQL
import pandas as pd
from urllib.parse import urlparse
class Parser:

    def __init__(self, rules):
        self.rules = rules
        self._host = None
        self._username = None
        self._type = None
        self._path = None
        self._password = None


        self.url_parse()
        
   # pull important information from a url format      
    def url_parse(self):

        parsed_URL = urlparse(self.rules)

        self._host = parsed_URL.hostname
        self._username = parsed_URL.username
        self._type = parsed_URL.scheme
        self._path = parsed_URL.path
        self._password = parsed_URL.password

    
    #saves host name 

    def get_host(self):
       return self._host
    
    # saves type of handler 
    def get_type(self):
        return self._type
    
    # gets  path 
    def get_path(self):
        return self._path
    
    # returns username for connection 
    def get_username(self):
        return self._username
    
    #returns passwork for connection
    def get_password(self):
        return self._password
    

    # allows to set a host name 
    def set_host(self, hostname):
       self._host = hostname
       return hostname
    
    # set a type of handler 
    def set_type(self, type):
        self._type = type
        return type
    
    
    # set a  path 
    def set_path(self, path):
        self._path = path 
        return path 
    
    # set a username 
    def set_username(self, username):
        self._username = username
        return username
    
    # set a password
    def set_password(self, password):
        self._password = password
        return password
    


def main():
    Driver="Louis"
    Server="LOUIS-PC"
    Database="Sweeper"
    Trusted_Connection="yes"



    mssql = MsSQL(driver=Driver, Server=Server, Database=Database,Trusted_Connection=Trusted_Connection, dbtype="MSSQL")
    #rule = mssql.query('Select * from sweeper_rules')
    rule = "https://user:password@domain.com/"
    
    pare = Parser(rules = rule)

    
    print(pare.get_type())

    


if __name__ == "__main__":
    main()
