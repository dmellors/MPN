import paramiko, getpass, time

devices = {'R1': {'ip': '10.1.1.254'},
           'R2': {'ip': '10.1.1.253'}}

# note use of \n for newline, this is needed in order for the command to be sent, by default paramiko does not issue a carrage return.
commands = ['show version\n', 'show run\n']

username = input('Username: ')
password = getpass.getpass('Password: ')

max_buffer = 65535

# This function clears the buffer and can be used for commands such as 'term len 0' where we do not need to see the output.
def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)


# Starts the loop for devices
for device in devices.keys():
    outputFileName = device + '_output.txt'
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'], username=username, password=password, look_for_keys=False, allow_agent=False)
    new_connection = connection.invoke_shell()
    output = clear_buffer(new_connection)
    time.sleep(2)
    new_connection.send("terminal length 0\n")
    output = clear_buffer(new_connection)
    with open(outputFileName, 'wb') as f:
        for command in commands:
            new_connection.send(command)
            time.sleep(2)
            output = new_connection.recv(max_buffer)
            print(output)
            f.write(output)

    new_connection.close()