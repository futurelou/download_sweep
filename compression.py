import tarfile 
from tqdm import tqdm
import os 
import tempfile
import zipfile
class compress: 

    
    def __init__(self, file, source_dir = None) :
        self.file = file
        self.source_dir = source_dir
        


class compress_tar(compress):

    def __init__(self, source_dir = None , compression_type = None):
        self.compression_type = compression_type
        self.source_dir = source_dir

    def compression_types():
        return ['gz', 'bz2', 'xz']
        

    def make_tarfile(self,output_filename ):
        with tarfile.open(output_filename, f"w:{self.compression_type}") as tar:
            tar.add(self.source_dir, arcname=os.path.basename(self.source_dir))


    def extract_tarfile(self, tar_file, dest_dir):
        file = tarfile.open(tar_file)
        file.extractall(dest_dir)

    def add_to_tar(self,file):
        if not os.path.exists(self.source_dir):
            t1 = tarfile.open(self.source_dir, f'r:{self.compression_type}')
            t1.close()


        t1 = tarfile.open(self.source_dir, f'r:{self.compression_type}')
        tmp = "-" + self.source_dir
        t2 = tarfile.open(tmp, f'w:{self.compression_type}')
        t1.extractall()
        for m in t1.members():
            t2.add(m)
            os.remove(m.path)

        t2.add(file)
        t2.close()
        t1.close()
        os.remove(file)
        os.rename(tmp, self.source_dir)


        


class zip_compress(compress):

    def __init__(self, src = None, dst = None  ):
        self.src = src
        self.dst = dst


    def compress_single_file(self):
        with zipfile.ZipFile(self.dst , mode = 'w') as zf:
            zf.write(self.src)

    def compress_dir(self):
        with zipfile.ZipFile(self.dst) as zf:
            for f in self.src:
                zf.write(f)


    def extract_single_file(self, file):
        with zipfile.ZipFile(self.src, mode='r') as zf:
            zf.extract(file, path=self.dst)

    def extract_all(self):
        with zipfile.ZipFile(self.src, mode='r') as zf:
            zf.extractall(self.dst)

    def append_to_zip(self, file):
        with zipfile.ZipFile(self.src, mode='a') as zf:
            zf.write('file')


    
           

        


        






            

def main():

  comp = zip_compress(src=r"Z:\trading\data\FactSet\datafeeds\estimates\fe_basic_ap\fe_basic_ap_full_677.zip",dst=r'\Users\louie\download_sweep\estimates')
  comp.extract_all()
     
if __name__ == "__main__":
    main()


