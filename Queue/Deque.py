import collections

def main():
    dq = collections.deque()
    dq.append(5)
    dq.append(6)
    print(dq)
    dq.appendleft(10)
    print(dq)
    dq.append(20)
    print(dq)

    dq.pop()
    print(dq)
    dq.popleft()
    print(dq)
    dq.appendleft(5)
    dq.appendleft(100)
    dq.append(7)

    print(dq)
    print(dq.index(5,0,3))
    dq.appendleft(5)
    print(dq)
    dq.remove(5)
    print(dq)
    print(dq.count(5))

    dq.extend([1,2,3])
    dq.extendleft([7,8,9])
    print(dq)

    dq.reverse()
    print(dq)
    dq.rotate(-4)
    print(dq)



if __name__ == '__main__':
    main()
