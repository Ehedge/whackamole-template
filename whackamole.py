import pygame
import random
board_length = 640
board_height = 512
board = []

def board_maker():
    for i in range(0, 20):
        board.append([])
        for j in range(0, 16):
            board[i].append(0)
def main():
    board_maker()
    board[0][0] = 1
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        screen.fill("light green")
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // 32
                    row = event.pos[1] // 32
                    if board[col][row] == 1:
                        board[col][row] = 0
                        new_row = random.randrange(0, 16)
                        new_col = random.randrange(0, 20)
                        screen.fill("light green")
                        screen.blit(mole_image, mole_image.get_rect(topleft=(new_col * 32, new_row * 32)))
                        board[new_col][new_row] = 1


            for i in range(1, 16):
                pygame.draw.line(screen, (0, 0, 0), (0, i * 32), (board_length, i * 32), 1)
            for i in range(1, 20):
                pygame.draw.line(screen, (0, 0, 0), (i * 32, 0), (i * 32, board_height), 1)

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
