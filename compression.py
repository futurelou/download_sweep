import tarfile 
from tqdm import tqdm
import os 
import zipfile
class compress: 

    def __init__(self, file, path = None) :
        self.file = file
        self.path = path


class compress_tar(compress):

    def __init__(self, file, path ,tar_file):
        self.tar_file = tar_file
        super().__init__(file, path)

    def compress(self):
        tar = tarfile.open(self.tar_file, mode= 'w:gz')

        progress = tqdm(self.file)

        for member in progress:
            tar.add(member)

            progress.set_description(f"Compressing {member}")
        
        tar.close

    def decompress(self):

        tar = tarfile.open(self.tar_file, mode="r:gz")

        if self.file is None:
            
            self.file = tar.getmembers()

        progress = tqdm(self.file)

        for member in progress:
            tar.extract(member, path= self.path)

            progress.set_description(f"Extracting {member.name}")

        tar.close()
        
        
class Zip(compress):
    def __init__(self, file, filename,pwd = None ,path=None):
        self.filename = filename
        self.pwd = pwd
        super().__init__(file, path)


    def zip_directory(self):

        directory = self.path
        files = os.listdir(directory)

        with zipfile.ZipFile(self.filename, 'w') as zip:
            for file in files:
                file_path = os.path.join(directory,file)
                zip.write(file_path)

    def add_to_zip(self):

        directory = self.path
        file_name = self.file

        with zipfile.ZipFile(self.filename, 'a') as zip:

            file_path = os.path.join(directory,file_name)
            zip.write(filename=file_path, arcname=file_name)


    def unzip_all(self):
        with zipfile.ZipFile(self.path, 'r') as zip:
            zip.extractall(self.filename, pwd=self.pwd)

    

    def unzip_one_file(self):

        with zipfile.ZipFile(self.path, 'r') as zip:
            zip.extract(self.filename, pwd=self.pwd)



            


