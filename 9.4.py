#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#input the file name if we press enter we'll immediately assume that the file is mbox-short
filename=input('Please Enter File Name: ')
if len(filename)<1:filename='mbox-short.txt'
try:
    handle=open(filename)
except:
    print ('please enter correct file name')
    quit()
count=None
email=None
dct=dict()
for line in handle: #a loop to go line by line vertically
    line=line.rstrip()
    #print(line)
    if not line.startswith('From '): #we'll only choose lines starting by 'From '
        continue
    else:
        words=line.split() #split each line into words
        for word in words: #loop to look each word in a line horizontally
            if "@" in word: #search for emails
                if word not in dct: #add emails into the dictionary
                    dct[word]=1
                else:
                    dct[word]=dct[word]+1
for k,v in dct.items(): # check the most recurring email and count it
    if count is None or v>count:
        email=k
        count=v
print(email,count)






    
