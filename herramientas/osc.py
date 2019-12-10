from pythonosc import udp_client
client = udp_client.SimpleUDPClient("192.168.0.249",55000)
gifs = ["alquim", "walpurgis","dance","queijiro"]

client.send_message("/test", [gifs[-1]])

def otro_gif(nombre):
	return client.send_message("/test", [nombre])