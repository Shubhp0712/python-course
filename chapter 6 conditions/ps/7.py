post = input("Enter a post :")

if "Harry".lower() in post.lower():  # using lower() to make the comparison case-insensitive
    print("The post is talking about harry.")

else:
    print("The post is not talking about harry.")