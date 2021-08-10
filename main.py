import os

folder = r"D:\Peer Kasten\python\rename_pictures\input"
prefix = 'clock'
data = os.listdir(folder)

num = 1
for i in data:
    filename, file_extension = os.path.splitext(folder + i)
    oldname = folder + '/' + i
    newname = folder + '/' + prefix + '.' + str(num) + file_extension
    while os.path.isfile(newname) and newname != oldname:
        num += 1
        newname = folder + '/' + prefix + '.' + str(num) + file_extension
    os.rename(oldname, newname)
    num += 1
