# The below code was in the main auto generated from the cisco devnet NX-API sandbox tool by typing in the command to run then pressing the python code button to show the code.
# Only the logon creds have been changed and the url, note for this to work /ins was added to the sandbox NX-API url.


import requests
import json

"""
Modify these please
"""
url='http://sbx-nxos-mgmt.cisco.com/ins'
switchuser='admin'
switchpassword='Admin_1234!'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show version",
      "version": 1
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()


# From the JSON data structure returned in the response variable specific details can be printed out, for example:

# Print the system code version
print ("\n")
print("Current system version: ",response['result']['body']['kickstart_ver_str'])

# Print the chassis id
print("Current system version: ",response['result']['body']['chassis_id'],"\n")


### As well as show commands, configuration commands can also be run, for example to set the hostname: ###

# first show current hostanme:

payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show hostname",
      "version": 1
    },
    "id": 1
  }
]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

print ("Hostname is: ",response['result']['body']['hostname'])


# Next set new hostname
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "hostname nx-new-hostA",
      "version": 1
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()


# Then re-display new hostname

payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show hostname",
      "version": 1
    },
    "id": 1
  }
]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

print ("Hostname is: ",response['result']['body']['hostname'],"\n")


### Note that multi line configuration commands they can be sent at the same time in one payload, note that the id field determines the order the commands are executed: ###

payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "interface loopback99",
      "version": 1
    },
    "id": 1
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "description Test",
      "version": 1
    },
    "id": 2
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "ip address 99.99.99.99 255.255.255.255",
      "version": 1
    },
    "id": 3
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "end",
      "version": 1
    },
    "id": 4
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "copy run start",
      "version": 1
    },
    "id": 5
  },
]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show interface loopback99",
      "version": 1
    },
    "id": 1
  },
  ]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

# Print out the new interface details from the returned JSON data in response[]
print ("Interface: ",response['result']['body']['TABLE_interface']['ROW_interface']['interface'])
print ("Description: ",response['result']['body']['TABLE_interface']['ROW_interface']['desc'])
print ("IP address: ",response['result']['body']['TABLE_interface']['ROW_interface']['eth_ip_addr'])
print ("Subnet Mask Bits: ",response['result']['body']['TABLE_interface']['ROW_interface']['eth_ip_mask'],"\n")

