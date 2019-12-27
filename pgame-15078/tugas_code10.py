import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
done = False
warna_bg = (0,0,0)

pygame.display.set_caption("Hello APP")

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and \
	 event.key == pygame.K_ESCAPE:
			done = True

	screen.fill(warna_bg)
	pygame.draw.line(screen, (255, 255, 255),(0, 20),(599, 20),(3))
	pygame.draw.line(screen, (255, 255, 255),(0, 380),(599, 380),(3))
	pygame.draw.line(screen, (255, 255, 255),(300, 20),(300, 380),(3))
	pygame.draw.line(screen, (255, 255, 255),(30, 180),(30, 240),(4))
	pygame.draw.line(screen, (255, 255, 255),(570, 180),(570, 240),(4))
	
	
	
	
	














	pygame.display.flip()
