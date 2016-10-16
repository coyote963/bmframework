from socket import socket
import psycopg2

def gameconnect(ip, port, password):
	bmsocket= socket()
	bmsocket.connect((ip, port))
	bmsocket.send(bytes('/rcon ' + password +'\n'))
	return bmsocket


def dbconnect(credentials):
	conn = psycopg2.connect(credentials)
	return conn
