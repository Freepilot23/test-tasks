import paramiko
#host = input("Введите адрес сервера: ")
#username = input ("Введите имя пользователя")
host = '192.168.48.7'
username = 'user'
password = '1234'
dir = 'home/user'#заданная папка
command = 'cd /'+ dir + "\nls -a"
#Соединение с сервером
client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
#Выполнение комманды на сервере
stdin, stdout, stderr = client.exec_command(command)
out1 = stdout.read().decode()
stdin, stdout, stderr = client.exec_command('find . -maxdepth 2')#вывод вложенных файлов
out2 = stdout.read().decode()#подсчет папок и файлов из списка
client.close()
sum = out2.count("\n")
print(out1)#построение списка
print("Общее количество файлов и папок:",sum)

#transport = paramiko.Transport((host, port))
#transport.connect(username='login', password='password')
#sftp = paramiko.SFTPClient.from_transport(transport)

#remotepath = '/path/to/remote/file.py'
#localpath = '/path/to/local/file.py'

#sftp.get(remotepath, localpath)
#sftp.put(localpath, remotepath)

#sftp.close()
#transport.close()
