import json

print("""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
"""
)
f=open("sample-data.json", "r")
y = json.loads(f.read())
for x in y["imdata"]:
        print(x["l1PhysIf"]["attributes"]["dn"], "                              ", x["l1PhysIf"]["attributes"]["speed"], x["l1PhysIf"]["attributes"]["mtu"] )
 