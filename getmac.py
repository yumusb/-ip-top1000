import re
with open("sewace.tk.log.1","rb") as f:
    log = f.read().decode()
    r = re.compile("mac=(.*?)&")
    macs = r.findall(log)
    macs = set(macs)
    with open("macs.txt","wb")as f1:
        f1.write("\n".join(macs).encode())