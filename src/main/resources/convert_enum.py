import os

content=open("/home/odysseus/ME/Java/plugins/PySoup/src/main/resources/enum.txt","r").readlines()

values=[]

id=0
for line in content:
    parts=line.split("(")
    name=parts[0]
    if name.startswith("//"):
        continue
    values.append(f"{name}={id}")
    id+=1

open("/home/odysseus/ME/Java/plugins/PySoup/src/main/resources/result.txt","w").write("\n".join(values))