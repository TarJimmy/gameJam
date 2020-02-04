pygame.init()
screen = pygame.display.set_mode((640, 640))
screen_buf = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()
angus = Hero()

formosa = TiledRenderer(filename)
run = True
while run:
    key=pygame.key.get_pressed()
        try:
            event = pygame.event.wait()
            if event.type == KEYDOWN:
                if (event.key == K_LEFT):
                    if angus.direction != DIRECTIONS['left']:
                        angus.direction = DIRECTIONS['left']
                        angus.update_now()
                    else:
                        angus.update()
                    testrect = pygame.Rect(angus.collision.x-2, angus.collision.y, 26, 16 )
                    if testrect.collidelist(formosa.boxcollider) == -1:
                        angus.position.x -= 2
                        angus.collision.x -= 2
# .. Le même type de condition pour les 3 autres mouvements
                elif (event.key == K_ESCAPE):
                    menu = Menu(screen, team)
                    menu.open_menu()

            if event.type == QUIT: run = False<br><br>        except KeyboardInterrupt:
            run = False
        formosa.terrain_render(screen_buf)
        formosa.over_terrain_render(screen_buf)
        formosa.under_char_render(screen_buf)
        screen_buf.blit(angus.image,angus.position)
        formosa.over_char_render(screen_buf)
        pygame.transform.scale(screen_buf, screen.get_size(), screen)
        pygame.display.flip()
        clock.tick(60)
