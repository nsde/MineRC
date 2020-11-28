from mcrcon import MCRcon

class Connection:
    def __init__(self, ip, pw):
        self.ip = ip
        self.pw = pw

    def execute(self, command):
        with MCRcon(self.ip, self.pw) as mcr:
            self.response = mcr.command(command)

        return self.response