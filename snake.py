import pygame

def main():

    #initialize menu
    run_app=True
    page=0
    while run_app:

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