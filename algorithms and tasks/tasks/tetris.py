import numpy as np

example_input = np.array([
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
])

TILES = {
    'I': [np.array([[1], [1], [1], [1]])],
    'O': [np.array([[[1, 1], [1, 1]]])],
    's': [np.array([[0, 1, 1], [1, 1, 0]])],
}


def rotate(matrix):
    return np.rot90(matrix)


def compare_tiles(matrix, tile):
    # We can simply compare with build in method of comparing in numpy and specify all method.
    # we compare tuple of matricies element-wise. All returns true when all is true.

    return np.any((matrix == tile, np.all((matrix == 1, tile == 0))))
    # return np.any((matrix == tile, np.and((matrix == 1, tile == 0)))) # В задачи было написано так и ее приняли


def search_in_matrix(matrix, tile, letter):
    # We will search for the possible matrix in tiles
    x, y = tile.shape
    results = []
    for i in range(6 - x):
        for j in range(6 - y):
            sub_matrix = matrix[i: i + x, j: j + y]  # we take each possible sub matrix here
            # will use compare_tiles() here to compare our tile in each sub_matrix that we are iterating
            if compare_tiles(sub_matrix, tile):
                matrix_copy = matrix.copy()
                pattern = sub_matrix == tile
                # Pattern - matrix of Boolean variable were we have matches matrix and tile
                # We could replace in matrix by that pattern. If true variable is replaced if false not
                # It will not replace if value is false

                matrix_copy[pattern] = letter  # here we colour our matrix with found patter
                results.append(matrix_copy)  # and append in result

    return results


def search_places(matrix, tile_letter_list):
    grids = [matrix]  # to list cast because we need a list of results
    for tile_letter in tile_letter_list:  # iterate over previous result with coloured matrix
        tiles = TILES[tile_letter]  # get mapping with all possible rotations
        new_grids = []  # list with all possible locations for the next iteration

        for grid in grids:  # we are searching for it in any grids return by previous step
            for tile in tiles:  # we are searching in any possible tile rotations
                found_grids = search_in_matrix(grid, tile, tile_letter)  # we found new grids
                new_grids.extend(found_grids)  # and extend list of the
            grids = new_grids  # we replace old grids with new ones

    return len(grids) > 0  # if length of grids in last iteration we’ll get true


def init_rotations():
    for key, value in TILES.items():
        tile = value[0]
        rotated = tile

        for i in range(3):
            rotated = rotate(rotated)
            if np.any(tile != rotated):
                TILES[key].append(rotated)


if __name__ == '__main__':
    """
    !!! Algorithm's complexity is: n ^ 3 * m ^ 2 !!!
    where: 
        n - is number of figures and also all rotations for them
        m - size of matrix
    
    We’ve got a grid with colored zone. We initialize all possible rotations of all tiles.
    Search through all possible grids, and tile's rotations.
    It’s kind of breadth-first search. 
    For each tile we’re search all possible places according to previous tile positions.
    And we replace previous result with new iteration result

    """
    # get input data
    grid = [], tile_letter_list = []
    init_rotations()
    search_places(grid, tile_letter_list)


