# 1. Fonction newBoard(n)
def newBoard(n):
    board = [[0] * n for _ in range(n)]
    # Place initiale des pions : joueur 1 en bas, joueur 2 à gauche
    for j in range(1, n):
        board[n - 1][j] = 1  # Pions du joueur 1
    for i in range(n - 1):
        board[i][0] = 2      # Pions du joueur 2
    return board

# 2. Procédure displayBoard(board, n)
def displayBoard(board, n):
    for i in range(n):
        row_display = str(i + 1) + " | "  # Numéro de ligne
        for j in range(n):
            if board[i][j] == 0:
                row_display += ". "  # Case vide
            elif board[i][j] == 1:
                row_display += "x "  # Pion du joueur 1
            elif board[i][j] == 2:
                row_display += "o "  # Pion du joueur 2
        print(row_display)

    # Ligne de séparation et numérotation des colonnes
    print("    " + "‾" * (2 * n - 1))
    print("    " + " ".join(str(j + 1) for j in range(n)))

# 3. Fonction possiblePawn
def possiblePawn(board, n, player, i, j):
    # Vérifie que la case contient un pion du joueur et qu'il peut se déplacer
    if board[i][j] != player:
        return False

    # Directions possibles pour chaque joueur
    if player == 1:  # Joueur 1 (peut aller haut, droite, gauche)
        moves = [(-1, 0), (0, 1), (0, -1)]
    else:  # Joueur 2 (peut aller droite, haut, bas)
        moves = [(0, 1), (-1, 0), (1, 0)]

    for di, dj in moves:
        ni, nj = i + di, j + dj
        
        # Vérifie si le mouvement est vers l'extérieur du plateau
        if player == 1 and ni < 0:  # Joueur 1 peut sortir par le haut
            return True
        if player == 2 and nj >= n:  # Joueur 2 peut sortir par la droite
            return True

        # Vérifie si le pion peut se déplacer vers une case vide dans le plateau
        if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 0:
            return True

    return False

# 4. Fonction selectPawn
def selectPawn(board, n, player):
    while True:
        i = int(input("Entrez la ligne de votre pion: ")) - 1
        j = int(input("Entrez la colonne de votre pion: ")) - 1
        if possiblePawn(board, n, player, i, j):
            return i, j
        print("Coordonnées invalides, réessayez.")
# 5. Fonction possibleMove
def possibleMove(board, n, player, i, j, m):
    # Directions spécifiques selon le joueur
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    di, dj = directions[m - 1]
    ni, nj = i + di, j + dj

    # Autoriser le mouvement vers (0, 0) même si c'est vide
    if ni == 0 and nj == 0:
        return True
    
    # Vérifier si le mouvement est hors plateau selon les règles
    if player == 1 and ni < 0:  # Joueur 1 sort par le haut
        return True
    if player == 2 and nj == n:  # Joueur 2 sort par la droite
        return True
    
    # Vérification des limites du plateau pour éviter les indices hors limites
    if ni < 0 or ni >= n or nj < 0 or nj >= n:
        return False

    return board[ni][nj] == 0

# 6. Fonction selectMove
def selectMove(board, n, player, i, j):
    while True:
        m = int(input("Choisissez une direction (1=haut, 2=droite, 3=bas, 4=gauche): "))
        if 1 <= m <= 4 and possibleMove(board, n, player, i, j, m):
            return m
        print("Direction invalide, réessayez.")

# 7. Fonction move
def move(board, n, player, i, j, m):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    di, dj = directions[m - 1]
    ni, nj = i + di, j + dj
    board[i][j] = 0  # Enlève le pion de l'ancienne position

    # Si le pion sort du plateau
    if (player == 1 and ni < 0) or (player == 2 and nj == n):
        print(f"Le pion du joueur {player} est sorti du plateau.")
    else:
        board[ni][nj] = player  # Place le pion dans la nouvelle position

# 8. Fonction win
def win(board, n, player):
    for i in range(n):
        for j in range(n):
            if board[i][j] == player and possiblePawn(board, n, player, i, j):
                return False
    return True

# 9. Programme principal dodgem
def dodgem(n):
    board = newBoard(n)
    player = 1

    while True:
        displayBoard(board, n)
        print(f"Joueur {player}, c'est votre tour.")
        
        # Sélectionner et déplacer un pion
        i, j = selectPawn(board, n, player)
        m = selectMove(board, n, player, i, j)
        move(board, n, player, i, j, m)
        
        # Vérifie si le joueur a gagné
        if win(board, n, player):
            displayBoard(board, n)
            print(f"Félicitations, joueur {player}, vous avez gagné!")
            break
        
        # Changer de joueur
        player = 1 if player == 2 else 2

# Démarrage du jeu
n = int(input("Entrez la taille du plateau (n x n): "))
dodgem(n)
