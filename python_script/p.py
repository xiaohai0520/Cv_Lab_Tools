
#处理各种

import os
import sys
start_index = 15
total = 2
frames = 25


# time file foramt :

# 00:05:30 2
# 00:05:40 5


# write the time file path here
filepath = './input/test.txt'

def readfile():
    res = []
    for line in open(filepath,'r'):
        line = line.split()
        res.append(line)
    return res

def get_clips_command_lines(times):


    command_lines = []
    for i,time in enumerate(times):
        command = 'ffmpeg -ss {} -t {}s -accurate_seek -i input/1.mp4 -codec copy -avoid_negative_ts 1 ./output/{}.mp4'.format(time[0],time[1],start_index+i)
        command_lines.append(command)
    return command_lines



def get_splits_command_lines():
    res = []
    for i in range(total):
        res.append('ffmpeg -i ./output/{}.mp4 -qscale:v 2 frames/{}/%6d.jpg'.format(start_index+i,start_index+i))
    return res

def get_renames_lines():
    res = []
    for i in range(total):
        # change the name of the rename python file name
        res.append('python r.py {}'.format(start_index+i))
    return res

def get_f2v_command_lines():
    res = []
    for i in range(total):
        res.append('ffmpeg -framerate {} -i ./frames/{}/%6d.jpg ./mp4/{}.mp4'.format(frames,start_index+i,start_index+i))
    return res

def run_code(lines):
    for l in lines:
        os.system(l)



def main(op):
    if op == "1":
        lines = get_clips_command_lines(readfile())

    elif op == '2':
        lines = get_splits_command_lines()
        for i in range(total):
            path = './frames/{}'.format(start_index+i)
            os.makedirs(path)
    elif op == '3':
        lines = get_renames_lines()
    elif op == '4':
        lines = get_f2v_command_lines()

    run_code(lines)




# 1 提取clips
# 2 将视频切成frames
# 3 转换frame名字
# 4 frams to video

main(sys.argv[1])