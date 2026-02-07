import pygame

def main():
    # Setup
    pygame.init()
    width = 1280
    height = 720
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    # Variables
    x_block = 50
    y_block = 50
    block_width = 50
    block_height = 50
    platform_width = width
    platform_height = 50

    while running:
        # Checa se o usuário saiu do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_block -= 100

        platform = pygame.Rect(0, height - 50, platform_width, platform_height)
        block = pygame.Rect(x_block, y_block, block_width, block_height)

        # A variável keys armazena o status de cada tecla do teclado.
        keys = pygame.key.get_pressed()

        # Movimentação do bloco (FALTA DESCREVER ISSO)
        if keys[pygame.K_UP]:
            y_block -= 15
        if keys[pygame.K_DOWN]:
            y_block += 15
        if keys[pygame.K_LEFT]:
            x_block -= 15
        if keys[pygame.K_RIGHT]:
            x_block += 15

        # Colisões com a tela
        if block.left < 0:
            block.left = 0
        if block.top <= 0:
            block.top = 0
        if block.right > width:
            block.right = width

        # Colisão com a plataforma
        if block.bottom > platform.top:
            block.bottom = platform.top
        
        # Configura a cor da tela
        screen.fill("orange")

        # Draw 
        pygame.draw.rect(screen, "brown", platform)
        pygame.draw.rect(screen, "black", block)


        # Atualiza as coisas na tela.
        pygame.display.flip()

        # Limita para 60 FPS
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()