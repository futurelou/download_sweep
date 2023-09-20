import hashlib
from db_handler import MsSQL
import pysftp
import wget
class Handler:

    def __init__(self, srcpath = None , dstpath =None, host= None, username= None, password= None):

        self.srcPath = srcpath
        self.dstPath = dstpath
        self.hostname = host
        self.username = username
        self.password = password
        
    def get_md5(self,data):
        with open(data, 'rb') as data_to_check:
            data = data_to_check.read()
            return hashlib.md5(data).hexdigest()
        
    def md5_check(self , new_data):
        Server="LOUIS-PC"
        Database="Sweeper"
        db = MsSQL(Server=Server,Database=Database)
        history = db.query('select * from sweeper_rules')

        if new_data in history['md5_check']:
            return True
        else:
            return False


class SFTP_Handler(Handler):
    
    def __init__(self,srcpath , dstpath, host, username, password ):
        super().__init__(srcpath , dstpath, host, username, password)

        self.con = pysftp.Connection(host=self.hostname, username=self.hostname,password=self.password)

    def get_file_from_sftp(self):
        tmp_storage = []
        self.con.get(remotepath=self.srcPath, localpath=tmp_storage)
        return tmp_storage
        
    
    #local dir "C:\Users\louie\sweeper_tmp_data"
    def get_directory_from_sftp(self,tmp_path):
        self.con.get_d(remotedir=self.srcPath, localdir=tmp_path)



#dst path would be a dir or file with data already in it
    def put_file(self):
        self.con.put(localpath=self.dstPath, remotepath=self.srcPath)

    def put_dir(self):
        self.con.put_d(localpath=self.dstPath, remotepath=self.srcPath)

    def get_pwd(self):
        return self.con.cwd()

    def close_sftp_connection(self):
        self.con.close()


class w_get(Handler):

    def __init__(self, srcpath=None, dstpath=None, host=None, username=None, password=None):
        super().__init__(srcpath, dstpath, host, username, password)


    def get(self):

        wget.download(url = self.srcPath, out=self.dstPath )


        





def main():
    
    h = Handler()
    md5 = h.get_md5(data=r"C:\Users\louie\Crypto_Data\1_hour_interval_crypto_data")
    print(md5)

    


if __name__ == "__main__":
    main()


            




    