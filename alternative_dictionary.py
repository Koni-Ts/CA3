import os
def file_reader(direct):
    content={}
    for root, dirs, files in os.walk(direct):
        for subdir in dirs:
            content[os.path.join(root, subdir)] = []
        content[root] = files
        # print (content)
    # Print out the content dict    
    for folder, filenames in content.items():
        print ('Folder: {}'.format(folder))
        print ('Filenames:')
        for filename in filenames:
            print ('-> {}'.format(filename))


files_dict=dict(file_reader("/workspace/CA3"))
print(files_dict)


for key, value in files_dict.keys():   # iter on both keys and values
        if key.startswith('Folder: \/workspace\/CA3\/wk[0-9]$'):
                print (key, value)