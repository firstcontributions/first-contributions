from random import random
from random import randint


def create_grid(n):
    #n designe la taille de la grille
    game_grid= []
    for i in range(0,n):
        L=[]
        for j in range(0,n):
            L.append(' ')
        game_grid.append(L)
    return game_grid

def grid_add_new_tile_at_position(game_grid,x,y):
    game_grid[x][y]=2
    return(game_grid)

def get_value_new_tile():
    if random()<= 0.90:
        return(2)
    else:
        return(4)

def get_all_tiles(game_grid):
    n= len(game_grid)
    L=[]
    for i in range(n):
        for j in range(n):
            if game_grid[i][j]== ' ':
                L.append(0)
            else:
                L.append(game_grid[i][j])
    return (L)

def get_empty_tiles_positions(game_grid):
    L=[]
    n=len(game_grid)
    for i in  range(n):
        for j in range(n):
            if game_grid[i][j]==' ' or game_grid[i][j]== 0:
                L.append((i,j))
    return(L)

def grid_get_value(game_grid,x,y):
    #x et y désignent abscisses et ordonnées
    if game_grid[x][y]== ' ':
        return(0)
    else:
        return (game_grid[x][y])
def get_new_position(game_grid):
    L=get_empty_tiles_positions(game_grid)
    n=randint(0,len(L)-1)
    return(L[n])

def grid_add_new_tiles(game_grid):
    L=get_empty_tiles_positions(game_grid)
    for elem in L:
        x,y=elem
        value_new_tile=get_value_new_tile()
        game_grid[x][y]=value_new_tile
    return(game_grid)

def grid_to_string(grid,n):
    list=['']
    for i in  range(n):
        a=''
        for j in range (n):
            a+='=== '
        list.append(a)
        b= ''
        for j in range(n):
            b+= '| '
            b+= str((grid_get_value(grid,i,j)))
            b+= ' |'
        list.append(b)
    c=''
    for i in range(n):
        c+='=== '
    grid_string = "\n".join(list)
    return(grid_string)

def grid_to_string_with_size(grid,n):
    size=len(grid)
    list=['']
    for i in range(size):
        a= ' '
        for j in range(size):
            for k in range(n+2):
                a+= '='
            a+= ' '
        list.append(a)
        b=''
        for j in range(size):
            value=str((grid_get_value(grid,i,j)))
            size_v=len(value)
            b+='|'
            b+= value
            for k in range(n+2-size_v):
                b+=' '
        b+='|'
        list.append(b)
    c=''
    for j in range(size):
            for k in range(n+2):
                c+= '='
            c+= ' '
    list.append(c)
    grid_string="\n".join(list)
    return(grid_string)

def grid_long_value(grid):
    long_value=0
    n=len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j]!= ' ':
                length=len(str(grid[i][j]))
                if length>long_value:
                    long_value= length
    return(long_value)


def grid_to_string_with_size_2(grid):
    return(grid_to_string_with_size(grid,grid_long_value(grid)))

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

def long_value_with_theme(grid,theme):
    long_value=0
    size=len(grid)
    for i in range(size):
        for j in range(size):
            x=grid[i][j]
            if len(theme[x])>long_value:
                long_value=len(theme[x])
    return(long_value)

def grid_to_string_with_size_and_theme(grid,theme,size):
    list=[]
    n=long_value_with_theme(grid,theme)
    for i in range(size):
        a= ''
        for j in range(size):
            for k in range(n+1):
                a+= '='
        a+= '='
        list.append(a)
        b=''
        for j in range(size):
            value=theme[grid[i][j]]
            b+='|'
            b+= value
            for k in range(n-len(value)):
                b+=' '
        b+='|'
        list.append(b)
    c=''
    for j in range(size):
            for k in range(n+1):
                c+= '='
    c+= '='
    list.append(c)
    list.append('')
    grid_string="\n".join(list)
    return(grid_string)
grid=[[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 64], [1024, 2048, 512, 2]]
print(grid_to_string_with_size_and_theme(grid,THEMES["1"],4))



