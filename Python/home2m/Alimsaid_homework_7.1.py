def __init__(self, array):
    self.array = array
    swapped = False
    for i in range(len(self.array) - 1, 0, -1):
        for j in range(i):
            if self.array[j] > self.array[j + 1]:
                self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break


arr_1 = [76, 98, 122, 34, 5, 90, 14, 8]
print(f'Sorted list: {sorted(arr_1)}')
