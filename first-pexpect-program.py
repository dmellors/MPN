import pexpect

# create dictionary containing two routers, note each entry is itself an embedded dictionary

devices = {'R1': {'prompt': 'R1#', 'ip': '10.1.1.254'},
           'R2': {'prompt': 'R2#', 'ip': '10.1.1.253'}
           }

# store username and password

username = 'dan'
password = 'danny1'

# Loop through each device in above nested dictionary and login via telnet then run a show version
# command finally printing output of the command to the console.

for device in devices.keys():
    device_prompt = devices[device]['prompt']
    child = pexpect.spawn('telnet ' + devices[device]['ip'])
    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt)
    child.sendline('show version | include V')
    child.expect(device_prompt)
    print (child.before)
    child.sendline('exit')


