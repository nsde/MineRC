# MineRC
Easier remonte connection to Minecraft Servers via Python! API avaiable.

# Disclaimer
This API is not 100% secure, so please use it only for small servers and make backups.

# Installation
In your Minecraft server folder, open the file `server.properties`.
Update the following line:

```properties
enable-rcon=true
```
Now, set up the port (default: 25575) and choose a strong password. Remember the password, you'll need it later.

```properties
rcon.port=25575
rcon.password=password
```

# Usage
## Connect with server
```py
myConnection = main.Connection(
    ip="localhost", # IP adress for the server to connect to
    pw="PASSWORD" # Remote connect password
    )
```

## Execute command

```py
response = server.execute(
    "say hi" # a Minecraft command
    )
```
The output of the command will be saved in the variable "response".

# Examples
## Simple program
```py
import main
server = main.Connection(ip="localhost", pw="PASSWORD")
output = server.execute("say hi")
print(output)
```
## Input loop
```py
import main
server = main.Connection(ip="localhost", pw="PASSWORD")

while 1:
    userInput = input("Type a command:\n") # User input
    output = server.execute(userInput) # Excute the input
    print(output) # Show the response
```