
# import os

# print(os.listdir())

# os.listdir(path='/workspace/CA3')

# def getListOfFiles(dirName):
#     # create a list of file and sub directories 
#     # names in the given directory 
#     listOfFile = sorted(os.listdir(dirName))
#     allFiles = list()
#     # Iterate over all the entries
#     for entry in listOfFile:
#         allFiles.append(entry)      
#     return allFiles



# dirName = '/workspace/CA3/wk1'
# listOfFiles = getListOfFiles(dirName)
# print (listOfFiles)





































# import os

# def html_files(direct):
#             x = [i[2] for i in sorted(os.walk(direct))]
#             y=list()
#             for t in x:
#                 for f in t:
#                     if f.endswith(".html"):
#                         y.append(f)
            
#             print(y)

# def md_files(direct):
#     x = [i[2] for i in sorted(os.walk(direct))]
#     y=list()
#     for t in x:
#         for f in t:
#             if f.endswith(".md"):
#                 y.append(f)
#     print(y)

# def pdf_files(direct):
#     x = [i[2] for i in sorted(os.walk(direct))]
#     y=list()
#     for t in x:
#         for f in t:
#             if f.endswith(".pdf"):
#                 y.append(f)
#     print(y)







# import os
# p=sorted(os.listdir(r'/workspace/CA3'))
# folders=list()
# for i in p:
#     if os.path.isdir(i):
#         folders.append(i)
#         files.app
# print (folders)

# i=html_files('/workspace/CA3')
# # j=md_files('/workspace/CA3')
# # k=pdf_files('/workspace/CA3')


# L = i
# s = "a"
# print (map(lambda x: str(x)+s, L))














# # import re

# for line in open('filename', 'r'):

#     firstPattern = re.search(r'email=(.*?)"', line)
#     secondPattern = re.search(r'"emailTo":"(.*?)"', line)
#     thirdPattern = re.search(r'pseId="(.*?)"', line)

#     if firstPattern:
#         print(firstPattern.group(1))
#     elif secondPattern:
#         print(secondPattern.group(1))
#     elif thirdPattern:
#         print(thirdPattern.group(1))












# import os
# from functools import reduce

# def get_directory_structure(rootdir):
#     """
#     Creates a nested dictionary that represents the folder structure of rootdir
#     """
#     dir = {}
#     rootdir = rootdir.rstrip(os.sep)
#     start = rootdir.rfind(os.sep) + 1
#     for path, dirs, files in os.walk(rootdir):
#         folders = path[start:].split(os.sep)
#         subdir = dict.fromkeys(files)
#         parent = reduce(dict.get, folders[:-1], dir)
#         parent[folders[-1]] = subdir
#     return dir


# folder_dict=get_directory_structure("/workspace/CA3/")
# # print(folder_dict)


        
# class RegexDict(dict):
#     import re
#     def __init__(self, *args, **kwds):
#         self.update(*args, **kwds)

#     def __getitem__(self, required):
#         for key in dict.__iter__(self):
#             if self.re.match(key, required):
#                 return dict.__getitem__(self, key)
#         return dict.__getitem__(self, key) # redundancy but it can handle exceptions.

# regex_dict = RegexDict(folder_dict)

# print (regex_dict[]) # blabla



import os


content={}
for root, dirs, files in os.walk("/workspace/CA3/"):
    for subdir in dirs:
        content[os.path.join(root, subdir)] = []
    content[root] = files

# Print out the content dict    
for folder, filenames in content.items():
    print ('Folder: {}'.format(folder))
    print ('Filenames:')
    for filename in filenames:
        print ('-> {}'.format(filename))

print(content ["/workspace/CA3/wk7"])

import re


for key, value in content.items():   # iter on both keys and values
        if key.startswith('Folder: \/workspace\/CA3\/wk[0-9]$'):
                print (key, value)