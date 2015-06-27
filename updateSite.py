import os

try:
    os.chdir("/Users/brianjenkins/dropbox/github/teaching")
    os.system("git add -A")
    os.system("git commit -m \"automatic update\"")
    os.system("git push")

    os.chdir("/Users/brianjenkins/dropbox/github/data")
    os.system("git add -A")
    os.system("git commit -m \"automatic update\"")
    os.system("git push")

except:
    os.chdir("/Users/bcjenkin/dropbox/github/teaching")
    os.system("git add -A")
    os.system("git commit -m \"automatic update\"")
    os.system("git push")
    
    os.chdir("/Users/bcjenkin/dropbox/github/data")
    os.system("git add -A")
    os.system("git commit -m \"automatic update\"")
    os.system("git push")