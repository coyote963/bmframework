import re
from collections import deque

infotypes = {1:"Chat", 2:"Match End", 3:"Scoreboard", 4:"Info", 5:"Vote", 6:"Killfeed", \
             7:"Steam ID", 8:"ID"}
gamemodes = {1:"CTF",2:"DM",3:"CLB",4:"ZMB",5:"TDM",6:"WD",7:"SVL",8:"TO"}
voteinfotypes = {0:"Change Map", 1:"Ban Player"}

def chatiter(index):
	return index + 3

def matchiter(index):
	return index + 3
def scoreboarditer(index):
	return index + 6
def infoiter(index):
	return index + 8
def voteiter(index):
	return index + 3
def killiter(index):
	return index + 4
def steamiter(index):
	return index + 3
def iditer(index):
	return index + 3


def infotype(identifier):
	return infotypes[int(identifier)]


def blocksplit(block):
	i = 0
	blockq = deque()
	blocklist = re.split('\n', block)
	while i < len(blocklist)-1:
		if infotype(blocklist[i]) == "Chat":
			blockq.append({
				'option':blocklist[i],
				'content':blocklist[i+1],
				'infotype':int(blocklist[i+2])
			})
			i = chatiter(i)
		
		elif infotype(blocklist[i]) == "Match End":
			blockq.append({
				'option':blocklist[i],
				'winner':blocklist[i+1],
				'next_map':blocklist[i+2]
				 })
			i = matchiter(i)
		
		elif infotype(blocklist[i]) == "Scoreboard":
			blockq.append({'option':blocklist[i],
				'gamemode': gamemode(blocklist[i+1]), 
				'team':blocklist[i+2], 
				'name':blocklist[i+3], 
				'kills':blocklist[i+4], 
				'deaths':blocklist[i+5]
				})
			i = scoreiter(i)
		
		elif infotype(blocklist[i]) == "Info":
			blockq.append({'option':blocklist[i],
				'server_name' : blocklist[i+1], 
				'connected' : int(blocklist[i+2]), 
				'capacity' : int(blocklist[i+3]), 
				'gamemode' : blocklist[i+4], 
				'mapname' :blocklist[i+5], 
				'minutes' : blocklist[i+6], 
				'seconds' : blocklist[i+7]
				})
			i =infoiter(i)
		
		elif infotype(blocklist[i]) == "Vote":
			if voteinfotype(block[i+2]) == "Change Map":
				blockq.append({
					'option': block[i],
					'map' : block[i+1]})
			else:
				blockq.append({
					'option':block[i],
					'player':block[i+1]
					})
			i = voteiter(i)
		
		elif infotype(blocklist[i]) == "Killfeed":
			blockq.append({
				'option' : block[i],
				'killer' : block[i+1],
				'victim' : block[i+2], 
				'cause' : block[i+3]
				})
			i = killiter(i)
		elif infotype(blocklist[i]) == "ID":
			blockq.append({
				'id' : int(block[i+1]), 
				'player' : block[i+2]
				})
			i = iditer(i)


		elif infotype(blocklist[i]) == "Steam ID":
			blockq.append({
				'steamid' : int(block[i+1]), 
				'player' : block[i+2]
				})
			i = steamiter(i)
		
	
		
	return blockq
