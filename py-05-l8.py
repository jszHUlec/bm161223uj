
def poloczenie_ssh_do_pbrania_log(ip): # to jest funckja globalna!
    print("drukuje logi z ip: ",ip)


class Server:
    def __init__(self, ip):
        self.ip = ip

    def drukuj_log(self):
        poloczenie_ssh_do_pbrania_log(self.ip)


sever1 = Server("10.20.30.4")
sever2 = Server("10.20.30.5")
sever3 = Server("10.20.30.6")
sever4 = Server("10.20.30.7")

sever1.drukuj_log()
sever3.drukuj_log()