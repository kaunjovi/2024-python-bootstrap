import os

if __name__ == "__main__" : 
    print(f"Traverse a folder.")


# 3-tuple (dirpath, dirnames, filenames).
# root : Prints out directories only from what you specified.
# dirs : Prints out sub-directories from root.
# files : Prints out all files from root and directories.
# for (root,dirs,files) in os.walk('.', topdown=True):


    for dirname, _, filenames in os.walk('./src'):
        for filename in filenames:
            print(os.path.join(dirname,filename))
            # print(dirname)
            # print(filename)
            # print( _)