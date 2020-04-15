''' prodcons.py

    Orders for pizza, spaghetti, or salads are filled sequentially.
    The orders are placed first-come-first-served, so a queue is used.
    The prepared items are placed in another queue, from which they are 
    retrieved by the wait staff, and placed in a log file.

    See the logfiles for sample output:
    pclog.txt, takelog.txt,preplog.txt, servlog.txt

    Output:
    ======
    Elapsed time: 18.746922062
'''

import random, os, time

def take_order(q,fname):
    '''
        Generates random orders and places them in queue q1
    '''
    take_fname = 'takelog.txt'
    if os.path.exists(take_fname):
        os.remove(take_fname)        # Truncate previous take log file

    items = ['pizza','spaghetti','salad']
    for i in range(10):
        item = random.choice(items)
        q.append(item)
        with open(fname,'a') as f:
            print(item,"ordered",file=f)
        with open(take_fname,'a') as t:
            print(item,"ordered",file=t)
    with open(fname,'a') as f:
        print('All orders taken',file=f)
    q.append('')   # Signal end of orders

def prep_order(q1,q2,fname):
    '''
        Removes orders from q1 and places them in q2
    '''
    prep_fname = 'preplog.txt'
    if os.path.exists(prep_fname):
        os.remove(prep_fname)        # Truncate previous prep log file

    # Get order from q1 (order_queue)
    f = open(fname,'a')
    while True:
        item = q1.pop(0)
        if not item:
            break
        q2.append(item)
        with open(fname,'a') as f:
            print(item,'prepared',file=f)
        with open(prep_fname,'a') as p:
            print(item,'prepared',file=p)
    with open(fname,'a') as f:
        print('All orders prepared',file=f)
    q2.append('')

def serv_order(q2,fname):
    '''
        Removes items from q2 and logs them
    '''
    serv_fname = 'servlog.txt'
    if os.path.exists(serv_fname):
        os.remove(serv_fname)        # Truncate previous serve log file

    f = open(fname,'a')
    while True:
        item = q2.pop(0)
        if not item:
            break
        with open(fname,'a') as f:
            print(item,'served',file=f)
        with open(serv_fname,'a') as s:
            print(item,'served',file=s)
    with open(fname,'a') as f:
        print('All orders served',file=f)
    f.close()

if __name__ == '__main__':
    fname = 'pclog.txt'
    if os.path.exists(fname):
        os.remove(fname)        # Truncate previous log file

    # Keep time
    start = time.perf_counter()

    # Create "queues" and processes
    q1 = []
    q2 = []
    take_order(q1,fname)
    prep_order(q1,q2,fname)
    serv_order(q2,fname)

    print("Elapsed time:",time.perf_counter() - start)
