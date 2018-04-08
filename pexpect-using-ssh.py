import getpass
from pexpect import pxssh

# create dictionary containing two routers, note each entry is itself an embedded dictionary

devices = {'R1': {'prompt': 'R1#', 'ip': '10.1.1.254'},
           'R2': {'prompt': 'R2#', 'ip': '10.1.1.253'}
           }

commands = ['term length 0', 'show version', 'show run']

username = input('Username: ')
password = getpass.getpass('Password: ')

for device in devices.keys():
    outputFilename = device + '_output.txt'
    device_prompt = devices[device]['prompt']
    child=pxssh.pxssh()
    child.login(devices[device]['ip'], username.strip(), password.strip(), auto_prompt_reset=False)
    with open(outputFilename, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(device_prompt)
            f.write(child.before)
    child.logout()

    

