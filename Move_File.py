import os 
import shutil

from_dir = '/Downloads/Class111.pdf'
to_dir = 'C:/Users/HP/Desktop/whitehat jr/Document_Files'

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    result = os.path.splitext(from_dir)
    print(result)
