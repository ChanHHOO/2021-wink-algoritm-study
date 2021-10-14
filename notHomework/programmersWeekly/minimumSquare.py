def solution(sizes):
    answer = 0
    
    sizes = [sorted(size, reverse=True) for size in sizes]
    width = [size[0] for size in sizes]
    height = [size[1] for size in sizes]


    return max(width) * max(height)

solution([[60, 50], [30, 70], [60, 30], [80, 40]])