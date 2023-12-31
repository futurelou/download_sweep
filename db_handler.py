import sqlalchemy
import pandas as pd
from sqlalchemy import text
import psycopg2
import MySQLdb

class DB_conn:

    def __init__(self, dbtype, driver  , Server , Database , Trusted_Connection , Username =None , Password =None):

            self.driver = driver
            self.Server = Server
            self.database = Database
            self.Trusted_Connection = Trusted_Connection
            self.username = Username
            self.Password = Password 
            self.dbtype = dbtype

        # query and return a pandas df from a db       
    def sql_to_df_(self,query):
            result  = pd.read_sql(query, con= self.conn)
            return result
    # go from pandas df to a db table 
    def df_to_sql(self, data, table_name):
          data.to_sql(name = table_name, con = self.conn, if_exists = 'append', index = False)



# connect to a Mssql server 
class MsSQL(DB_conn):


    def __init__(self,dbtype , driver, Server , Database , Trusted_Connection , Username = None, Password =None ):
        super().__init__(dbtype , driver, Server, Database , Trusted_Connection, Username , Password )

    
        self.conn = sqlalchemy.create_engine('mssql+pyodbc://@' + f'{self.Server}' + '/' + f'{self.database}' + '?trusted_connection=yes&driver=ODBC Driver 17 for SQL Server', max_overflow=0, pool_size=1000)


    def close(self):
            pass
    
    def insert_file_into_table(self, file, dbtable):
          qry = text("BULK INSERT " + dbtable + " FROM '" + file + "' WITH (DATAFILETYPE = 'char', FIRSTROW = 2, ROWTERMINATOR = '0x0a' )")
          con = self.conn.connect()
          con.execute(qry)
          con.commit()
          con.close

    def table_to_file(self, filename, query):
         
         self.conn.cursor()
         data = self.query(query=query)
         file = open(filename, 'w')
         file.write(data)
         file.close

    def query(self, query):
          qry = text(query)
          con= self.con.connect()
          res = con.execute(qry).fetchall()
          con.commit()
          con.close
          return res
    
class PostGres(DB_conn):
      
    def __init__(self, database, user, password):
      
        self.database = database 
        self.user = user
        self.password = password 

      
        self.conn = psycopg2.connect(database = self.database,user = self.user,password= self.password)

    def query(self, query):
        try:
           cursor =  self.conn.cursor()
           cursor.execute(query)
           
           try:
                result = cursor.fetchall()
                return result
           except(Exception, psycopg2.Error) as error:
                print('this aint working')            
           cursor.commit()

        except(Exception, psycopg2.Error) as error:
             print(f'error connecting to the database: {error}')


    def insert_file_into_table(self, file, table):
         qry = f'copy {table} from {file}'
         try:
              cursor = self.conn.cursor()
              cursor.ececute(qry)

         except(Exception, psycopg2.Error) as error:
             print(f'error performing this action: {error}')


    def copy_table_into_file(self, file, table):
         
         qry = f'copy {table} to {file}'
         try:
              cursor = self.conn.cursor()
              cursor.ececute(qry)

         except(Exception, psycopg2.Error) as error:
             print(f'error performing this action: {error}')


class MySql(DB_conn):
     
     def __init__(self, database, user, password):
      
        self.database = database 
        self.user = user
        self.password = password 
        
        self.conn = MySQLdb.connect(database = self.database,user = self.user,password= self.password)

     def query(self, qry):
          try:
           cursor =  self.conn.cursor()
           cursor.execute(qry)
           
           try:
                result = cursor.fetchall()
                return result
           except(Exception) as error:
                print('this aint working')            
           cursor.commit()

          except(Exception, psycopg2.Error) as error:
             print(f'error connecting to the database: {error}')
          
          

     
     
         


       

        
    
   
        

def main():
    Driver="Louis"
    Server="LOUIS-PC"
    Database="Sweeper"
    Trusted_Connection="yes"
    
    mssql = MsSQL(driver=Driver, Server=Server, Database=Database,Trusted_Connection=Trusted_Connection, dbtype="MSSQL")

    
    #psg = PostGres( database='PSG_TEST',user='postgres', password='Zoezeus16701')

    print(mssql.query('select * from seeper_rules'))

    

     
if __name__ == "__main__":
    main()
