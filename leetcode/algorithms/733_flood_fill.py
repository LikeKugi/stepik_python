from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    query_color = image[sr][sc]
    if color != query_color:
        FillImage(image, sr, sc, color, query_color)
    return image


def FillImage(image, sr, sc, color, qc):
    if 0 <= sr < len(image) and 0 <= sc < len(image[0]):
        print(f'sr = {sr} sc = {sc}')
        if image[sr][sc] == qc:
            image[sr][sc] = color
            FillImage(image, sr - 1, sc, color, qc)
            FillImage(image, sr, sc - 1, color, qc)
            FillImage(image, sr + 1, sc, color, qc)
            FillImage(image, sr, sc + 1, color, qc)
    return image


def test_1():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    print(floodFill(image, sr, sc, color))


test_1()
