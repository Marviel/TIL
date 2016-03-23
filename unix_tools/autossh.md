#Autossh
##Installation:
    sudo apt-get install autossh

##Description
Autossh allows you to maintain an ssh connection for long periods of time.
I primarily use it for SSH Reverse Tunneling. (google that if you don't know what it is)

##Usage
To connect a private computer to a middleman host, and leave it open for ssh on port 12345, use this:
    autossh -M 12399 -oPasswordAuthentication=no -oLogLevel=error  -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no -i ~/.ssh/keyfile.pem -R 12345:localhost:22 middle_usr@middleman.com -p 22
Where:
"keyfile.pem" is the .pem file that allows middleman access,
"middle_usr" is the user on the middleman server
"middleman.com" is the domain/ip for the middleman server


##Further Information:
1. http://www.harding.motd.ca/autossh/
2. bash$ man autossh
