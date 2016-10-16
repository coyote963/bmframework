import psycopg2
import bmbuffer
import BMStream
def parse(funclist,socket, **kwargs):
	bms = BMStream.BMStream(socket)
	try:
		while (True):
			bms.read()
			
			while bms.isEmpty():
				bmdict = bms.pop()
				for bmfunc in funclist:
					bmfunc(bmdict,socket,**kwargs)
	except KeyboardInterrupt:
		print "exiting"
		dbcursor.close()
		socket.close()
		
		
		
