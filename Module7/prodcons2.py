''' prodcons2.py

    Different threads fill orders for pizza, spaghetti, or salads.
    The orders are placed first-come-first-served, so a queue is used.
    The prepared items are placed in another queue, from which they are 
    retrieved by the wait staff, and placed in a log file.

    See the logfiles for sample output:
    pclog2.txt, takelog2.txt,preplog2.txt, servlog2.txt

    Output:
    ======
    Elapsed time: 15.026023209
'''

import threading as th
import queue, random, os, time

def take_order(q,fname):
    '''
        Generates random orders and places them in queue q1
    '''
    take_fname = 'takelog2.txt'
    if os.path.exists(take_fname):
        os.remove(take_fname)        # Truncate previous take log file

    items = ['pizza','spaghetti','salad']
    for i in range(10):
        item = random.choice(items)
        q.put(item)
        with open(fname,'a') as f:
            print(item,"ordered",file=f)
        with open(take_fname,'a') as t:
            print(item,"ordered",file=t)
    with open(fname,'a') as f:
        print('All orders taken',file=f)
    q.put('')   # Signal end of orders

def prepare_order(q1,q2,fname):
    '''
        Removes orders from q1 and places them in q2
    '''
    prep_fname = 'preplog2.txt'
    if os.path.exists(prep_fname):
        os.remove(prep_fname)        # Truncate previous prep log file

    # Get order from q1 (order_queue)
    while True:
        item = q1.get()
        if not item:
            break
        q2.put(item)
        with open(fname,'a') as f:
            print(item,'prepared',file=f)
        with open(prep_fname,'a') as p:
            print(item,'prepared',file=p)
    with open(fname,'a') as f:
        print('All orders prepared',file=f)
    q2.put('')

def serve_order(q2,fname):
    '''
        Removes items from q2 and logs them
    '''
    serv_fname = 'servlog2.txt'
    if os.path.exists(serv_fname):
        os.remove(serv_fname)        # Truncate previous serve log file

    while True:
        item = q2.get()
        if not item:
            break
        with open(fname,'a') as f:
            print(item,'served',file=f)
        with open(serv_fname,'a') as s:
            print(item,'served',file=s)
    with open(fname,'a') as f:
        print('All orders served',file=f)

if __name__ == '__main__':
    fname = 'pclog2.txt'
    if os.path.exists(fname):
        os.remove(fname)        # Truncate previous log file

    # Keep time
    start = time.perf_counter()

    # Create queues and processes
    q1 = queue.Queue()
    q2 = queue.Queue()
    take = th.Thread(target=take_order,args=(q1,fname))
    prepare = th.Thread(target=prepare_order,args=(q1,q2,fname))
    serve = th.Thread(target=serve_order,args=(q2,fname))

    # Start the processes (in reverse order)
    serve.start()
    prepare.start()
    take.start()

    # Wait for the processes to complete (in forward order)
    take.join()
    prepare.join()
    serve.join()

    print("Elapsed time:",time.perf_counter()-start)
