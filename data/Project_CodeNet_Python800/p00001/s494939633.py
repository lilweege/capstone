heap = []
while True:
    try:
        n = int(raw_input())
        if len(heap) == 0:
            heap.append(n)
        elif len(heap) == 1:
            if n <= heap[0]:
                heap.append(n)
            else:
                heap.insert(0, n)
        elif len(heap) == 2:
            if n > heap[0]:
                heap.insert(0, n)
            elif n <= heap[1]:
                heap.append(n)
            else:
                heap.insert(1, n)
        elif n > heap[2]:
            if n >= heap[0]:
                heap.insert(0, n)
            elif n >= heap[1]:
                heap.insert(1, n)
            else:
                heap.insert(2, n)
            heap.pop()
    except (EOFError):
        break
for num in heap:
    print num