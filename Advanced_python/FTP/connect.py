from ftplib import FTP
ftp = FTP('ftp.cse.buffalo.edu')
ftp.login()

print(ftp.retrlines('LIST'))
print(ftp.cwd('mirror'))
