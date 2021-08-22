import pygame


SIZE_BLOCK = 20
COUNT_BLOCKS = 20
MARGIN = 1
HEADER_MARGIN = 70
SIZE = [SIZE_BLOCK*(COUNT_BLOCKS+2) + MARGIN*COUNT_BLOCKS, SIZE_BLOCK*(COUNT_BLOCKS+2) + MARGIN*COUNT_BLOCKS + HEADER_MARGIN]

SNAKE_COLOR = (0, 102, 0)
FRAME_COLOR = (0, 255, 204)
HEADER_COLOR = (0, 204, 153)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)


def draw_block(color: tuple, row: int, column: int) -> None:
    pygame.draw.rect(screen, color, [SIZE_BLOCK+column*SIZE_BLOCK+MARGIN*(column+1),HEADER_MARGIN+SIZE_BLOCK+row*SIZE_BLOCK+MARGIN*(row+1), SIZE_BLOCK,SIZE_BLOCK])


class SnakeBlock:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


if __name__ == "__main__":
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Snake")
    timer = pygame.time.Clock()

    snake_block = [SnakeBlock(9,9)]
    drow = 0
    dcol = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and drow != 1:
                    drow = -1
                    dcol = 0
                elif event.key == pygame.K_DOWN and drow != -1:
                    drow = 1
                    dcol = 0
                elif event.key == pygame.K_LEFT and dcol != 1:
                    drow = 0
                    dcol = -1
                elif event.key == pygame.K_RIGHT and dcol != -1:
                    drow = 0
                    dcol = 1
        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0,0, SIZE[0],HEADER_MARGIN])

        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):
                if (row + column) % 2 == 0:
                    color = BLUE
                else:
                    color = WHITE
                draw_block(color, row, column)

        for block in snake_block:
            draw_block(SNAKE_COLOR, block.x, block.y)
            block.x += drow
            block.y += dcol

        pygame.display.flip()
        timer.tick(3)