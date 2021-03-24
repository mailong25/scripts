#for filename in *.tar.gz
#do
#  tar -xvf $filename
#  rm -rf $filename
#done

#mv */* ../all_wav2lip

def number_to_string(number):
    return f'{number:05}'

import os, ntpath
from os.path import join as join_path
import multiprocessing
from multiprocessing import Pool
from tqdm import tqdm

PATH_TO_FILE_LIST = '/mnt/disks3/wav2lip_data/filelists'
PATH_TO_FILE_VIDEO = '/mnt/disks3/wav2lip_data/videos'

dirs = [join_path(PATH_TO_FILE_VIDEO,p) for p in os.listdir(PATH_TO_FILE_VIDEO)]
all_files = []

def norm_video(d):
    all_files = []
    os.system('rm -rf ' + d + '/.@__thumb')
    files = [join_path(d,p) for p in os.listdir(d)]
    for i in range(0,len(files)):
        new_file_name = files[i].replace(ntpath.basename(files[i]), number_to_string(i) + '.mp4')
        os.system("ffmpeg -hide_banner -loglevel panic -i " + files[i] + " -filter:v fps=fps=25 " + new_file_name)
        os.remove(files[i])
        all_files.append(ntpath.basename(d) + '/' + number_to_string(i))
    return all_files

pool = Pool(16)    
#pool = Pool(multiprocessing.cpu_count())
all_files = pool.map(norm_video,dirs)
all_files = [j for i in all_files for j in i]

SPLIT_NUM = int(len(all_files) * (1 - 0.05))

with open(join_path(PATH_TO_FILE_LIST,'train.txt'),'w') as f:
    f.write('\n'.join(all_files[:SPLIT_NUM]))
    
with open(join_path(PATH_TO_FILE_LIST,'val.txt'),'w') as f:
    f.write('\n'.join(all_files[SPLIT_NUM:]))
    
with open(join_path(PATH_TO_FILE_LIST,'test.txt'),'w') as f:
    f.write('\n'.join(all_files[SPLIT_NUM:]))

