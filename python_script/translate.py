#处理格式

import sys
import os

#read each clip into a 2Darray
def readfile(filepath):
    data = []
    each_clip = []
    for line in open(filepath,'r'):
        if line == ' ' or line == '\n':
            break
        # print(line)
        if 'mp4' in line:
            each_clip = []
        each_clip.append(line.strip('\n').strip())
        # print(each_clip)
        cur_line = line.split()

        if cur_line[-1] =='end':
            data.append(each_clip)

    return data



def process_each_clip(clip):
    res = []
    res.append(clip[0])
    res.append(clip[1])
    i = 2
    while i < len(clip)-1:
        cur1 = clip[i].split()
        cur2 = clip[i+1].split()

        if i == 2:
            key_frame = 0
            start_frame = 0
            end_frame = int(cur2[0])//2


        elif 2 < i < len(clip) - 3:
            key_frame = int(cur1[0])
            start_frame = int(res[-1][2]) + 1
            end_frame = (int(cur2[0]) + int(cur1[0]))//2

        elif i == len(clip) - 3:
            key_frame = int(cur1[0])
            start_frame = int(res[-1][2]) + 1
            end_frame = int(cur2[0])-1


        elif i == len(clip) - 2:
            key_frame = int(cur1[0])
            start_frame = int(cur1[0])
            end_frame = int(cur2[0])

        # print(i)
        # print('key_frame:',key_frame)
        # print('start_frame:', start_frame)
        # print('end_frame:', end_frame)
        i += 1


        res.append([str('%06d' % key_frame),str('%06d' % start_frame),str('%06d' % end_frame),str('%.3f'%(float(key_frame)*0.02)),str('%.3f'%(float(start_frame)*0.02)),str('%.3f'%(float(end_frame)*0.02)),cur1[-1]])

    return res

def process(filepath):
    clips = readfile(filepath)
    res = []
    for clip in clips:
        cur = process_each_clip(clip)
        res.append(cur)
    return res

def write2txt(filepath,clips):

    f = open(filepath,'w')
    f.truncate();

    for clip in clips:
        for each_line in clip:
            if type(each_line) == str:
                f.write(each_line)
            else:
                f.write(' '.join(map(str,each_line)))
            f.write('\n')
    f.close()


def main(filepath):

    write2txt(filepath,process(filepath))

main(sys.argv[1])