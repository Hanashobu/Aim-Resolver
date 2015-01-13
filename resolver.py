#!/usr/bin/env python
# AIM username->IP by Matthew Blankenship
# In order for this to work, you must be logged into the aim application
# Only have a chat open with the username you are trying to resolve
# This same concept works for any P2P chat application including Skype and ICQ

import socket, random

def getUsername(username):
	l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	l.bind(("127.0.0.1", 4000)) # AIM uses port 4000
	print ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])

def main():
	while True:
		username = raw_input("AIM username: ")
		if username:
			break;

	getUsername(username)

if __name__=='__main__':
	main()
