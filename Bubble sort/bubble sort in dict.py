elements = [
        { 'name': 'kartikey',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'mukesh', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'ajay',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

def bubble_sort(elements, key):
    size = len(elements)
    for i in range(size-1):
        swaped = False
        for j in range(size-1-i):
            a = elements[j][key]
            b = elements[j+1][key]
            if a>b:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swaped = True

        if not swaped:
            break


bubble_sort(elements, 'name')
print(elements)