import pygame

WIDTH_START = 400
HEIGHT_START =600
WIN = pygame.display.set_mode((WIDTH_START,HEIGHT_START))

pygame.font.init()
SCORE_FONT=pygame.font.SysFont('calibri',30)
max_score = 1
actual_score = 0
#WINDOW MAIN MENU

#colors
BACKGROUND_COLOR1=(0, 181, 82)
BACKGROUND_COLOR2=(2, 212, 97)
BLACK = (0, 0, 0)
GREEN= (34,139,34)
BLACK = (0, 0, 0)
BACKGROUND_COLOR=BLACK
WHITE= (255,255,255)
GREEN= (34,139,34)
RED = (255,99,71)
SNAKE_COLOR = BLACK
FOOD_COLOR= (0, 22, 189)


def draw_background(cell_size, height, width):
    color1_line=True
    for h in range(0, height, cell_size):
        color1=color1_line
        for w in range(0, width, cell_size):
            border = pygame.Rect(w, h, cell_size, cell_size)
            if color1:
                pygame.draw.rect(WIN, BACKGROUND_COLOR1, border)
                color1 = False
            else:
                pygame.draw.rect(WIN, BACKGROUND_COLOR2, border)
                color1 = True
        if color1_line:
            color1_line=False
        else:
            color1_line=True

def draw_menu(button1_text, button1rect, button2_text, button2rect):
    draw_background(20,HEIGHT_START,WIDTH_START)
    #button1
    pygame.draw.rect(WIN, BLACK, button1rect)
    WIN.blit(button1_text,( WIDTH_START/2 - (button1_text.get_width()//2), HEIGHT_START/2-(button1_text.get_height()//2) ))
    #button2
    pygame.draw.rect(WIN, BLACK, button2rect)
    WIN.blit(button2_text,
             (WIDTH_START / 2 - (button2_text.get_width() // 2) + 5,
                              HEIGHT_START / 2 + (button1_text.get_height() // 2) + 15))
    pygame.display.update()

def menu():
    # button Start new game
    button1_text = SCORE_FONT.render("Start new game", 1, BACKGROUND_COLOR1)
    button1rectPos=(WIDTH_START / 2 - (button1_text.get_width() // 2) - 5,
                              HEIGHT_START / 2 - (button1_text.get_height() // 2) - 5,
                              button1_text.get_width() + 10,
                              button1_text.get_height() + 10)
    button1rect = pygame.Rect(button1rectPos[0],button1rectPos[1],button1rectPos[2],button1rectPos[3])
    # button settings
    button2_text = SCORE_FONT.render("Custom map", 1, BACKGROUND_COLOR2)
    button2rectPos=(WIDTH_START / 2 - (button2_text.get_width() // 2) - 5,
                              HEIGHT_START / 2 + (button1_text.get_height() // 2) + 10,
                              button2_text.get_width() + 20,
                              button2_text.get_height() + 10)
    button2rect = pygame.Rect(button2rectPos[0],button2rectPos[1],button2rectPos[2],button2rectPos[3])
    run_menu=True
    while run_menu:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
                return -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1rectPos[0]<=mouse[0]<=button1rectPos[0]+button1rectPos[2] and button1rectPos[1]<=mouse[1]<=button1rectPos[1]+button1rectPos[3]:
                    return 1
                if button2rectPos[0]<=mouse[0]<=button2rectPos[0]+button2rectPos[2] and button2rectPos[1]<=mouse[1]<=button2rectPos[1]+button2rectPos[3]:
                    return 2

        draw_menu(button1_text, button1rect, button2_text, button2rect)


def main():

    #initialize menu
    run_app=True
    page=0
    while run_app:
        pygame.display.set_caption("Snake Menu")
        if page==-1:
            run_app = False
        if page==0:
            page = menu()
        if page==1: #start new game
            page = game("default")
        if page == 2:
            page = game("costumize")

if __name__ == '__main__':
    main()