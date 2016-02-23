import shutil
from os.path import isfile, join, getmtime
from os import listdir

# Locations of the PDF expert directory and the full PDF repository
pdfExpertPath = "/Users/bcjenkin/Dropbox/PDF Expert/"
citationPath = "/Users/bcjenkin/Google Drive/Work/Research/Citations/"

# Files in each directory
pdfFiles = [ f for f in listdir(pdfExpertPath) if isfile(join(pdfExpertPath,f)) ]
citationFiles = [ f for f in listdir(citationPath) if isfile(join(citationPath,f)) ]

# Identify files that have been modified in the PDF experct directory and copy
for file in pdfFiles:
    if file in citationFiles:
        if getmtime(pdfExpertPath+file) > getmtime(citationPath+file):
            shutil.copyfile(pdfExpertPath+file,citationPath+file)