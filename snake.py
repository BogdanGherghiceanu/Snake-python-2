import pygame

WIDTH_START = 400
HEIGHT_START =600
WIN = pygame.display.set_mode((WIDTH_START,HEIGHT_START))

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