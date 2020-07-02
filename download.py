## Want to download file from => ftp://ftp.example.com/directory/directory1/directory2/myfile.bin

import os
from ftplib import FTP

ftp = FTP("ftp.example.com") #If no authen
#ftp = FTP("ftp.example.com","username","password")  ## authen
ftp.login()

## Change directory
ftp.cwd("directory")
ftp.cwd("directory1")
ftp.cwd("directory2")

filename = "myfile.bin"

### Download file
local_filename = os.path.join("./", filename)
lf = open(local_filename, "wb")
print ("Downloading...")
ftp.retrbinary("RETR " + filename, lf.write, 8*1024)
lf.close()
print ("Finished to download " + filename)
