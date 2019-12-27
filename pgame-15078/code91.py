import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
done = False
warna_bg = (55,255, 255)

pygame.display.set_caption("Hello APP")

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and \
	 event.key == pygame.K_ESCAPE:
			done = True

	screen.fill(warna_bg)
	pygame.draw.line(screen, (0, 0, 255),(0, 0),(300, 300))
	pygame.draw.line(screen, (255, 255, 0),(300, 300),(600, 450))



	pygame.display.flip()
