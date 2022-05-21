# Given a positive sorted array
# Define a function f(a, x) that returns x, the next smallest number, or -1 for errors.
a = [ 3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21 ]

def next_smallest_number(items, x):
    state = -1
    if not items or not isinstance(items, list): 
        return state

    for item in items:
        if item <= x:
            state = item
        else:
            break
    return state

assert next_smallest_number(a, 13) == 12
assert next_smallest_number(a, 12) == 12
assert next_smallest_number(a, 2) == -1
assert next_smallest_number(a, 22) == 21
assert next_smallest_number(a, 3) == 3
assert next_smallest_number(a, 21) == 21
assert next_smallest_number([], 21) == -1
assert next_smallest_number(None, 21) == -1
assert next_smallest_number(None, 'a') == -1
assert next_smallest_number([], 'a') == -1
assert next_smallest_number([], None) == -1
assert next_smallest_number([], 0) == -1
assert next_smallest_number(a, -1) == -1
assert next_smallest_number(a, 11) == 10
assert next_smallest_number(a, 8) == 6
assert next_smallest_number(9, 8) == -1
assert next_smallest_number(-1, 8) == -1
assert next_smallest_number(-1, -1) == -1
