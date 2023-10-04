from db_handler import MsSQL
import pandas as pd
import glob
from sqlalchemy import text



def main():

  
    Driver="Louie"
    Server="LOUIS-PC"
    Database =  "Research"
    Trusted_Connection="yes"
    
    mssql = MsSQL(driver=Driver, Server=Server, Database=Database,Trusted_Connection=Trusted_Connection, dbtype="MSSQL")

    finaldf = []
    data  =glob.glob(r"Z:\researchDB\closeQuotes\SSE\2010*")
    file1 = glob.glob(r'Z:\researchDB\closeQuotes\SSE\20101014')
    count = 0 
    for file in data:
        
        #data = mssql.query(f"""BULK INSERT closeQuotes
        #                   FROM '{file}'
        #                    WITH (                         
        ##                FIRSTROW = 2,
        #               FIELDTERMINATOR = ',', 

        #               ROWTERMINATOR = '\n', 
        #            TABLOCK);
        #                    """)
        
        res = mssql.con.connect()
        res.execute(text(f"""BULK INSERT closeQuotes
                           FROM '{file}'
                            WITH (                         
                        FIRSTROW = 2,
                       FIELDTERMINATOR = ',', 
                       
                       ROWTERMINATOR = '\n', 
                    TABLOCK);
                           """))
      
        
        

        
    

    
   


        



    

   

  
   


     
if __name__ == "__main__":
    main()
