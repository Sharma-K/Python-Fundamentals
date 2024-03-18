fp = open('D:\\AI\\Ai\\Note1.txt', 'w+')
fp.write("changes made by file_handling.py")
fp.seek(0) # it is the pointer from which we will read
print(fp.read())
fp.close()