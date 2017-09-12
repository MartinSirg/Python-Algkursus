"""Conversion from row, col => cell index and vice versa."""


def get_cell_index(row, col, row_len):
    """
    Return cell index for row, col and table width.

    Given the row and column indices and the number of columns in the table
    return cell index at the given location.

    :param row: row index
    :param col: column index
    :param row_len: number of columns in the table
    :return: cell index at the given location
    """
    return col + row_len * row


def get_row_and_col(cell_index, row_len):
    """
    Return row, col for cell index and table width.

    Given the cell index and the number of columns in the table
    return tuple with row and col indices.

    :param cell_index: cell index
    :param row_len: number of columns in the table
    :return: row index, col index as tuple
    """
    tup = (cell_index // row_len, cell_index % row_len)

    return tup


def get_row_len(row, col, cell_index):
    """
    Return table width for row, col and cell index.

    Given the row and column indices and the cell index
    return the number of columns in the table.

    If the given setup is not possible
    or it is not possible to deduct column count
    return -1

    :param row: row index
    :param col: column index
    :param cell_index: cell index
    :return: number of columns in the table
    """
    if row == 0 and cell_index > col:
        return -1
    elif row == 0 and col == 0:
        return -1
    elif row == 0:
        return col
    elif col > (cell_index - col) / row:
        return - 1
    else:
        return (cell_index - col) / row
