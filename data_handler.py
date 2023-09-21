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
        
    def md5_check(self , new_data, hist):

        if new_data in hist:
            return True
        else:
            return False


class SFTP_Handler(Handler):
    
    def __init__(self,srcpath , dstpath, host, username, password ):
        super().__init__(srcpath , dstpath, host, username, password)

        self.con = pysftp.Connection(host=self.hostname, username=self.username,password=self.password)

    def get_file_from_sftp(self):
        
        self.con.get(remotepath=self.srcPath, localpath=self.dstPath)
       
        
    
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
    md1 = h.get_md5(data=r"C:\Users\louie\Crypto_Data\1_min_interval_crypto_data")

    print(h.md5_check(new_data=md5, hist=md1))
    print(md1)

    s = SFTP_Handler(host='louis-pc', username='louie', password='Zoezeus16701!',srcpath=r"C:\Users\louie\Crypto_Data\1_hour_interval_crypto_data", dstpath=r"C:\Users\louie\sweeper_tmp_data\test.data")
    s.get_file_from_sftp()



    


if __name__ == "__main__":
    main()


            




    