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
    return np.any((matrix == tile, np.all((matrix == 1, tile == 0))))
    # return np.any((matrix == tile, np.and((matrix == 1, tile == 0)))) # В задачи было написано так и ее приняли


def search_in_matrix(matrix, tile, letter):
    x, y = tile.shape
    results = []
    for i in range(6 - x):
        for j in range(6 - y):
            sub_matrix = matrix[i: i + x, j: j + y]
            if compare_tiles(sub_matrix, tile):
                matrix_copy = matrix.copy()
                pattern = sub_matrix == tile
                matrix_copy[pattern] = letter
                results.append(matrix_copy)

    return results


def search_places(matrix, tile_letter_list):
    grids = [matrix]
    for tile_letter in tile_letter_list:
        tiles = TILES[tile_letter]
        new_grids = []

        for grid in grids:
            for tile in tiles:
                found_grids = search_in_matrix(grid, tile, tile_letter)
                new_grids.extend(found_grids)
            grids = new_grids

    return len(grids) > 0


def init_rotations():
    for key, value in TILES.items():
        tile = value[0]
        rotated = tile

        for i in range(3):
            rotated = rotate(rotated)
            if np.any(tile != rotated):
                TILES[key].append(rotated)


if __name__ == '__main__':
    # inputs
    grid = [], tile_letter_list = []
    init_rotations()
    print(search_places(grid, tile_letter_list))

# Сложность n ^ 3 * m ^ 2
