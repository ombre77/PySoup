import os

content=open("/home/odysseus/ME/Java/plugins/PySoup/src/main/resources/enum.txt","r").readlines()

values=[]

id=0
for line in content:
    line=line.replace("\n","")
    parts=line.split("=")
    name=parts[0].strip()
    if name.startswith("//") or name.startswith("#"):
        values.append(line)
        continue
    if name!=name.upper() or len(parts)==1 or len(name.split(" "))>1:
        values.append(line)
        continue
    values.append(f'    {name.upper().replace("\n","")}="{name.lower().strip().strip("\n")}"')
    id+=1

open("/home/odysseus/ME/Java/plugins/PySoup/src/main/resources/result.txt","w").write("\n".join(values))