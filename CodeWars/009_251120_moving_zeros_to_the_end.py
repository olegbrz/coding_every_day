"""Write an algorithm that takes an array and moves all of the zeros to the
end, preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]

"""


def move_zeros(array):
    filtered = []
    zero_counter = 0

    for element in array:
        if element != 0 or isinstance(element, bool):
            filtered.append(element)
        else:
            zero_counter += 1

    return filtered + [0] * zero_counter
