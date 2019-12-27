#pemrograman game praktikum 8
#latihan kode 8.2 : Pygame 
import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
# clock = pygame.time.clock()
done = False

warna_font = (255, 255, 255)
warna_bg_font = (0, 255, 0)
warna_bg = (255, 255, 25)

font = pygame.font.SysFont("Comicsanasms", 72)
pygame.display.set_caption("Hallo App")
text = font.render("Hello World", True, warna_font, warna_bg_font)
text1 = font.render("Informatika UMMU", True, warna_font, warna_bg_font)
text2 = font.render("Praktikum 8", True, warna_font, warna_bg_font)
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			done = True

	screen.fill(warna_font)
	screen.fill(warna_bg_font)
	screen.fill(warna_bg)
	screen.blit(text, (220 - text.get_width() //4, 250)) #posisi text
	screen.blit(text1, (220 - text1.get_width() //4, 150)) #posisi text
	screen.blit(text2, (220 - text2.get_width() //4, 50)) #posisi text

	pygame.display.flip()
	# clock.tick(60)
