from socket import socket
from collections import deque
from bmbuffer import blocksplit
class BMStream:
	def __init__(self, socket):
		self.blockqueue = deque()
		self.socket = socket
	def read(self):
		self.blockqueue = blocksplit(self.socket.recv(500))
	def pop(self):
		return self.blockqueue.pop()
	def isEmpty(self):
		return self.blockqueue
