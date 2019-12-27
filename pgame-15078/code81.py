#pemrograman game praktikum 8
#latihan kode 8.1 : Pygame 
import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
done = False

warna_font = (255, 0, 0)
warna_bg_font = (0, 255, 0)
warna_bg = (55, 255, 255)

font = pygame.font.SysFont("Comicsanasms", 72)

text = font.render("Hello World", True, warna_font, warna_bg_font)
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			done = True

	screen.fill(warna_bg)
	screen.blit(text, (220 - text.get_width() //2, 250)) #posisi text
	
	pygame.display.flip()
	
