st = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

f = open("filewrite.txt", "a") # open file in append mode. If file not found, it will create file.
f.write(st)

# Append mode will add the content at the end of the file. If we use write mode, it will overwrite the content of file.

f.close()