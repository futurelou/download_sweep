import sqlalchemy
import pandas as pd
from sqlalchemy import text

class DB_conn:

    def __init__(self, dbtype, driver  , Server , Database , Trusted_Connection , Username =None , Password =None):

            self.driver = driver
            self.Server = Server
            self.database = Database
            self.Trusted_Connection = Trusted_Connection
            self.username = Username
            self.Password = Password 
            self.dbtype = dbtype

# connect to a Mssql server 
class MsSQL(DB_conn):


    def __init__(self,dbtype , driver, Server , Database , Trusted_Connection , Username = None, Password =None ):
        super().__init__(dbtype , driver, Server, Database , Trusted_Connection, Username , Password )

        self.con = sqlalchemy.create_engine('mssql+pyodbc://@' + f'{self.Server}' + '/' + f'{self.database}' + '?trusted_connection=yes&driver=ODBC Driver 17 for SQL Server', max_overflow=0, pool_size=1000)

  # query and return a pandas df from a db       
    def sql_to_df_(self,query):
            result  = pd.read_sql(query, con= self.con)
            return result
    # go from pandas df to a db table 
    def df_to_sql(self, data, table_name):
          data.to_sql(name = table_name, con = self.con, if_exists = 'append', index = False)

    def close(self):
            pass
    
    def insert_data(self, incsv, dbtable):
          qry = text("BULK INSERT " + dbtable + " FROM '" + incsv + "' WITH (DATAFILETYPE = 'char', FIRSTROW = 2, ROWTERMINATOR = '0x0a' )")
          con = self.con.connect()
          con.execute(qry)
          con.commit()
          con.close

    def query(self, query):
          qry = text(query)
          con= self.con.connect()
          res = con.execute(qry).fetchall()
          con.commit()
          con.close
          return res
          

      


   
        

def main():
    Driver="Louis"
    Server="LOUIS-PC"
    Database="Research"
    Trusted_Connection="yes"
    
    mssql = MsSQL(driver=Driver, Server=Server, Database=Database,Trusted_Connection=Trusted_Connection, dbtype="MSSQL")

    
    df = mssql.query('Select * from closeQuotes')
    


     
if __name__ == "__main__":
    main()
