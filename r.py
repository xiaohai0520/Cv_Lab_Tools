import os
import sys

fix_path = './frames/'

def rename(folder):

    # get the path
    path = fix_path + folder + '/'

    # get all the files
    f = os.listdir(path)

    # sort the files
    f.sort()

    # new index
    count = 0

    # loop
    for i in f:
        if i[0] == '.':
            continue
        # oldname get
        oldname = path + i

        # new name with new index
        newname = path + str('%06d' % count) + '.jpg'

        # print(oldname,newname)

        # change name
        # print(oldname,newname)
        os.rename(oldname, newname)


        count += 1


rename(sys.argv[1])
