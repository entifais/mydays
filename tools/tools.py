def readFile(name):
	with open(name, 'r') as file:
		content = []
		for i in file.readlines():
			content.append(str(i).replace("\n",""))
		return content