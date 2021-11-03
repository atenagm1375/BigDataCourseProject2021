from snakebite.client import Client


client = Client('localhost', 9000)
for p in client.mkdir(['test/input', 'test/output'], create_parent=True):
	print(p)

