import os
from collections import Counter
import string
import socket
import sys

original_stdout = sys.stdout

#folder paths
resFile=r'/home/output/result.txt'
dir_path = r'/home/data/'
ifFilePath=r'/home/data/IF.txt'
result_file=open(resFile, 'w+')
with result_file as f:
    #sys.stdout = f # Change the standard output to the file we created.

    # list to store files
    res = []

    # a. List name of all the text file at location: /home/data
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    result_file.write("Files at location /home/data are:\n")
    
    #total number of words in each text files
    sum=0
    for path in res:
        result_file.write("->"+path+"\n")
        file = open("/home/data/"+path, 'r')
        read_data = file.read()
        per_word = read_data.split()
        abc="Total Words:"+str(len(per_word))   
        #result_file.write(abc+"\n")
        sum=sum+len(per_word)


    result_file.write("total number of words in each text files "+str(sum)+"\n")


    #top 3 words with maximum number of counts in IF.txt
    file = open(ifFilePath, 'r')
    read_data = file.read()
    per_word = read_data.split()
    #result_file.write(str(per_word)+"\n")

    word=[];
    for i in per_word:
        a=i.translate(str.maketrans('', '', string.punctuation))
        a=a.capitalize()
        word.append(a)
    Counter = Counter(word)
    most_occur = Counter.most_common(3)
    result_file.write("top 3 words with maximum number of counts in IF.txt "+str(most_occur)+"\n")




    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    result_file.write("Your Computer IP Address is:"+IPAddr+"\n")
    sys.stdout = original_stdout
result_file.close()

file = open(resFile, 'r',encoding='utf-8')
print(file.read())








