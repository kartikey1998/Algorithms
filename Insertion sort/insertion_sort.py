def insertion_sort(elements):
    for i in range(1, len(elements)):
        j = i-1
        anchor = elements[i]
        while j>=0 and anchor<elements[j]:
            elements[j+1] = elements[j]
            j = j-1
            elements[j+1] = anchor




if __name__ == '__main__':
    elements = [11,9,28,7,9,46,8,24]
    insertion_sort(elements)
    print(elements)
