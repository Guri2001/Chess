class Chessboard:

    def __init__(self):

        files = [i for i in range(1, 9)]
        ranks = [chr(i) for i in range(ord('a'), ord('h')+1)]

        self.board = [[None for _ in range(8)] for _ in range(8)]

        self.setup_board()
    
    """
    Fill in the starting position of the board (Defalt starting position) 
    for both White and Black.
    """
    def setup_board(self):
        #TO DO: Create objects of each pieces e.g. Pawn, Rook, etc ...
        pass

    






c1 = Chessboard()


    