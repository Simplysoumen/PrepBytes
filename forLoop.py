# var = range(0,5)
# print(var)
# print(type(var))
#
# for i in range(20,0,-3):
#     print(i)

# st = "PrepBytes"
# for ch in st:
#     print(ch)

# for i in range(len(st)):
#     print(st[i])


# for i in range(20):
#     if(i>10):
#         break
#     print(i,end="")
# print()
# print("Loop ended")


# for i in range(1,6):
#     for j in range(i,6):
#         print("*",end="")
#     print()

#Angle Problems
# T = int(input())
# for i in range(T):
#     h, m = map(int, input().split())
#     h_pos = int (h*(360/12)+(m*360)/(12*60))
#     m_pos = int (m*(360/60))
#     if(h_pos - m_pos <= 180):
#         angle = int(h_pos - m_pos)
#     else:
#         angle = int(m_pos - h_pos)
#     if(angle < 0):
#         angle *= -1
#     print(angle)

# Socks Problems
# T= int(input())
# for i in range(T):
#     N = int(input())
#     N = N+1
#     print(N)
