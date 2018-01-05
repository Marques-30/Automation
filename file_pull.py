import os
file = os.listdir("C:\\Users\\butilm01\\Desktop\\Jira")
cut = str(file).split("'")
print cut[1]
print cut[3]
print cut[5]