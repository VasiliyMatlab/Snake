import pygame
import sys
import random


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
RED = (224, 0, 0)


def draw_block(color: tuple, row: int, column: int) -> None:
    pygame.draw.rect(screen, color, [SIZE_BLOCK+column*SIZE_BLOCK+MARGIN*(column+1),HEADER_MARGIN+SIZE_BLOCK+row*SIZE_BLOCK+MARGIN*(row+1), SIZE_BLOCK,SIZE_BLOCK])

def get_random_empty_block():
    x = random.randint(0, COUNT_BLOCKS-1)
    y = random.randint(0, COUNT_BLOCKS-1)
    empty_block = SnakeBlock(x, y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, COUNT_BLOCKS-1)
        empty_block.y = random.randint(0, COUNT_BLOCKS-1)
    return empty_block


class SnakeBlock:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def is_inside(self):
        return 0<=self.x<COUNT_BLOCKS and 0<=self.y<COUNT_BLOCKS
    
    def __eq__(self, other) -> bool:
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


if __name__ == "__main__":
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Snake")
    timer = pygame.time.Clock()

    snake_blocks = [SnakeBlock(9,9)]
    apple = get_random_empty_block()
    drow = 0
    dcol = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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

        head = snake_blocks[-1]
        if not head.is_inside():
            pygame.quit()
            sys.exit()
        
        draw_block(RED, apple.x, apple.y)
        if apple == head:
            apple = get_random_empty_block()

        for block in snake_blocks:
            draw_block(SNAKE_COLOR, block.x, block.y)

        new_head = SnakeBlock(head.x+drow, head.y+dcol)
        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        pygame.display.flip()
        timer.tick(3)