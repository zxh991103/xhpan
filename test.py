import os
data_dir='/var/www/html'

def list_dir(data_dir):
    list1=os.listdir(data_dir)
    list2=[]
    for i in list1:
        if len(i.split('.')) == 2:
            list2.append(i)

    print(list2)
    return list2

list_dir(data_dir)

