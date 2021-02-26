import os , sys
from pydub import AudioSegment
from shutil import copy2
from multiprocessing import Pool
import multiprocessing
from pathlib import Path
import ntpath
from random import randint

SELECT_DIR = '/mnt/disks3/non-native/all'
min_sec = 8
max_sec = 30

def split_audio(path):
    file_name   = ntpath.basename(path).replace('.wav','')
    parent_dir  = str(Path(path).parent)
    audio = AudioSegment.from_wav(path)
    audio_len = int(len(audio) / 1000.0) - 1
    
    if audio_len <= max_sec:
        return
    
    if audio_len > 7200:
        os.remove(path)
        return
    
    if audio_len >= 300:
        audio_len = 270
        audio = audio[20000:-10000]
    
    cur_idx = 0
    file_idx = 0
    while True:
        chunk_len = randint(min_sec,max_sec) * 1000
        chunk_audio = audio[cur_idx : min(cur_idx + chunk_len,audio_len * 1000)]
        if len(chunk_audio) < min_sec*1000:
            break
        chunk_file_name = file_name + '-_-' + str(file_idx) + '.wav'
        chunk_file_name = os.path.join(parent_dir,chunk_file_name)
        chunk_audio.export(chunk_file_name,format='wav')
        file_idx += 1
        cur_idx  += chunk_len
        
    os.remove(path)

files = [SELECT_DIR + '/' + p for p in os.listdir(SELECT_DIR)]
pool = multiprocessing.Pool(multiprocessing.cpu_count())
pool.map(split_audio,files)
