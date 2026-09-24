def parse_board(board):
    if not isinstance(board, str):
        return None

    rows = board.splitlines()
    if not rows:
        return None

    size = len(rows)
    for row in rows:
        if len(row) != size:
            return None

    king_positions = []

    for row_index, row in enumerate(rows):
        for col_index, cell in enumerate(row):
            if cell == "K":
                king_positions.append((row_index, col_index))

    if len(king_positions) != 1:
        return None

    return rows, king_positions[0]


def get_first_piece_in_direction(board, start_row, start_col, row_step, col_step):
    size = len(board)
    row = start_row + row_step
    col = start_col + col_step

    while row >= 0 and row < size and col >= 0 and col < size:
        cell = board[row][col]

        if cell in "KQBRP":
            return cell

        row += row_step
        col += col_step

    return None


def pawn_checks_king(board, king_row, king_col):
    size = len(board)
    pawn_row = king_row + 1

    if pawn_row >= size:
        return False

    for pawn_col in (king_col - 1, king_col + 1):
        if pawn_col >= 0 and pawn_col < size and board[pawn_row][pawn_col] == "P":
            return True

    return False


def sliding_checks_king(board, king_row, king_col):
    straight_directions = (
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    )
    diagonal_directions = (
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    )

    for row_step, col_step in straight_directions:
        piece = get_first_piece_in_direction(
            board, king_row, king_col, row_step, col_step
        )
        if piece in ("R", "Q"):
            return True

    for row_step, col_step in diagonal_directions:
        piece = get_first_piece_in_direction(
            board, king_row, king_col, row_step, col_step
        )
        if piece in ("B", "Q"):
            return True

    return False


def checkmate(board):
    parsed = parse_board(board)

    if parsed is None:
        print("Error")
        return

    rows, (king_row, king_col) = parsed

    if pawn_checks_king(rows, king_row, king_col):
        print("Success")
        return

    if sliding_checks_king(rows, king_row, king_col):
        print("Success")
        return

    print("Fail")
