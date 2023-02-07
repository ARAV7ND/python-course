from ftplib import FTP
ftp = FTP()
HOST = 'ftp.cse.buffalo.edu'
PORT = 12345
ftp.connect(HOST, PORT)

# This code will fail as the FTP server in this example doesn’t have port 12345 open for us. However, the idea is to convey how to connect to a port that differs from the default.
