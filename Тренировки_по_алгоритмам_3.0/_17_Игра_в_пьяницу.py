cards1=list(map(int,input().split(' ')))
cards2=list(map(int,input().split(' ')))
queue1=cards1.copy()+[None]*5
head1=0
tail1=4
queue2=cards2.copy()+[None]*5
head2=0
tail2=4
move=0
size1=size2=5
k=True
while True:
    front1=queue1[head1]
    queue1[head1]=None
    head1=(head1+1)%len(queue1)
    front2 = queue2[head2]
    queue2[head2] = None
    head2 = (head2 + 1) % len(queue2)
    if front1>front2 and not((front1==9 and front2==0)) or (front1==0 and front2==9):
        tail1 = (tail1 + 1) % len(queue1)
        queue1[tail1]=front1
        tail1=(tail1+1)%len(queue1)
        queue1[tail1]=front2
        size1+=1
        size2-=1
    else:
        tail2 = (tail2 + 1) % len(queue2)
        queue2[tail2] = front1
        tail2 = (tail2 + 1) % len(queue2)
        queue2[tail2] = front2
        size2+=1
        size1-=1
    move+=1
    if move==10**6:
        print('botva')
        break
    if size1==0 or size2==0:
        print((size1 > 0) * 'first' + int(size2 > 0) * 'second' + ' ' + str(move))
        break

# from collections import deque
# cards1=deque(list(map(int,input().split(' '))))
# cards2=deque(list(map(int,input().split(' '))))
# move=0
# while len(cards1)*len(cards2)>0:
#     card1=cards1.popleft()
#     card2=cards2.popleft()
#     if card1>card2 and not(card1==9 and card2==0) or card1==0 and card2==9:
#         cards1.append(card1)
#         cards1.append(card2)
#     else:
#         cards2.append(card1)
#         cards2.append(card2)
#     move+=1
#     if move==10**6:
#         print('botva')
#         break
# else:
#     print(int(len(cards1)>0)*'first'+int(len(cards2)>0)*'second'+' '+str(move))

# def play_game(cards1, cards2):
#     moves = 0
#     while moves < 10**6:
#         moves += 1
#         if len(cards1) == 0 or len(cards2) == 0:
#             break
#         card1 = cards1.pop(0)
#         card2 = cards2.pop(0)
#         if card1 == 0 and card2 == 9:
#             cards1.append(card1)
#             cards1.append(card2)
#         elif card2 == 0 and card1 == 9:
#             cards2.append(card1)
#             cards2.append(card2)
#         elif card1 > card2:
#             cards1.append(card1)
#             cards1.append(card2)
#         else:
#             cards2.append(card1)
#             cards2.append(card2)
#
#     if len(cards1) == 0:
#         return "second", moves
#     elif len(cards2) == 0:
#         return "first", moves
#     else:
#         return "botva"
# cards1 = list(map(int, input().split()))
# cards2 = list(map(int, input().split()))
# result, moves = play_game(cards1, cards2)
# print(result, moves - 1)
