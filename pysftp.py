import pysftp

host = 'HOSTNAME OR IP Address'
port = 22
username = 'username'
password = 'password'

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

file_name = 'merge_1_20210902.mp4'

local_path = '/home/ubuntu/video/'
remote_path = '/home/ubuntu/video/'

with pysftp.Connection(host, port=port, username=username, password=password, cnopts=cnopts) as sftp:
    
    sftp.put(local_path+file_name, remote_path+file_name)
    
    sftp.close()