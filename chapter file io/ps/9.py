with open("this.txt","r") as f:
    content1 = f.read()

# with open("this_copy.txt","r") as f: # this_copy.txt is a copy of this.txt that's why both files are identical
#     content2 = f.read()

with open("log.txt","r") as f: # log.txt is a different file that's why both files are not identical 
    content2 = f.read()

if(content1 == content2):
    print("Both files are Identical")
else:
    print("Both files are not Identical")