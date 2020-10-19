from queue import Queue
q = Queue(5)
for i in range(5):
    q.put(i+1)
print('-'*30)
while True:
    a = input('<<<')
    print('~~~~~~~~~~~~')
    print(q.full())    #q.full意思是这个队列是否已满
    if not q.full():   #如果不满才可以进来
        q.put_nowait(a)
    else:
        while not q.empty():  #不为空才能进来
            print(q.get())    #队列满了之后打印现在队列中的值
    print('~~~~~~~~~~~~')




