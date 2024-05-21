from typing import List


def custom_zip(*args, full=False, default=None) -> List[List]:
    zipped_lists = []
    if full:
        max_length = max(len(lst) for lst in args)
        for i in range(max_length):
            elements_in_tuple = [lst[i] if i < len(lst) else default for lst in args]
            zipped_lists.append(tuple(elements_in_tuple))
    else:
        min_length = min(len(lst) for lst in args)
        for i in range(min_length):
            elements_in_tuple = [lst[i] for lst in args]
            zipped_lists.append(tuple(elements_in_tuple))
    return zipped_lists


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
print(custom_zip(seq1, seq2))  # [(1, 9), (2, 8), (3, 7)]
print(custom_zip(seq1, seq2, full=True, default="Q"))  # [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
