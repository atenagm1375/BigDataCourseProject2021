from snakebite.client import Client


client = Client('localhost', 9000)
for p in client.delete(['test'], recurse=True):
	print(p)

