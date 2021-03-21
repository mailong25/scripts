#for filename in *.tar.gz
#do
#  tar -xvf $filename
#  rm -rf $filename
#done

#mv */* ../all_wav2lip

def number_to_string(number):
    return f'{number:05}'

import os
from os.path import join as join_path
PATH_TO_FILE_LIST = '/mnt/disks3/wav2lip_data/filelists'
PATH_TO_FILE_VIDEO = '/mnt/disks3/wav2lip_data/videos'

dirs = [join_path(PATH_TO_FILE_VIDEO,p) for p in os.listdir(PATH_TO_FILE_VIDEO)]
all_files = []

for d in dirs:
    os.system('rm -rf ' + d + '/.@__thumb')
    files = [join_path(d,p) for p in os.listdir(d)]
    for i in range(0,len(files)):
        new_file_name = files[i].replace(ntpath.basename(files[i]), number_to_string(i) + '.mp4')
        os.rename(files[i], new_file_name)
        all_files.append(ntpath.basename(d) + '/' + number_to_string(i))
        
        
SPLIT_NUM = int(len(all_files) * (1 - 0.05))

with open(join_path(PATH_TO_FILE_LIST,'train.txt'),'w') as f:
    f.write('\n'.join(all_files[:SPLIT_NUM]))
    
with open(join_path(PATH_TO_FILE_LIST,'val.txt'),'w') as f:
    f.write('\n'.join(all_files[SPLIT_NUM:]))
    
with open(join_path(PATH_TO_FILE_LIST,'test.txt'),'w') as f:
    f.write('\n'.join(all_files[SPLIT_NUM:]))

