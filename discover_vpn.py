import json
	
def parse_openvpn(file_name):
    file_read = open(file_name,'r').read()
    file_split_n=file_read.split('\n')
    clients = []
    for client in file_split_n:
        split_t = client.split('\t')
        if split_t[0] == 'CLIENT_LIST':
            clients.append(split_t[1])
    return clients

file = '/path_to/file.log'


comma = ""

users = parse_openvpn(file)
count=0
data={}
for i in users:
    count += 1
    key = "{#VPNUSER}"
    data.setdefault("data", []).append({key:i})

print(json.dumps(data, sort_keys=True, indent=2))
