from db_handler import MsSQL
import pandas as pd
import glob
from sqlalchemy import text
import time
import os




def main():

  
    Driver="Louie"
    Server="LOUIS-PC"
    Database =  "Research"
    Trusted_Connection="yes"
    
    mssql = MsSQL(driver=Driver, Server=Server, Database=Database,Trusted_Connection=Trusted_Connection, dbtype="MSSQL")

   
    data  =glob.glob(r"Z:\researchDB\closeQuotes\SSE\201*")
    file1 = glob.glob(r'Z:\researchDB\closeQuotes\SSE\20101014')
   
    
    for file in data:
        print(file)
        
        #mssql.insert_data(incsv=file, dbtable='closeQuotes')

        #df = pd.read_csv(file)
        #mssql.df_to_sql(df, 'closeQuotes')
    
        
        
        

        
    

    
   


        



    

   

  
   


     
if __name__ == "__main__":
    main()
