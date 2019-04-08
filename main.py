from threading import *
from time import *
import time

resource_lock_ = Lock()
writers_lock_ = Lock()

resource = time.strftime("%c")

n_readers = 0
n_writers = 0

counter = 0
wcounter = 0

class reader(Thread):
    def run(self):

        global counter
        global resource
        global n_readers
        global resource_lock_



        while counter < 20:

            print ("vill in")
            if n_readers == 0:
                resource_lock_.acquire()
            
            n_readers += 1
            sleep(1)

            print("%s reader in the room" % (self.name), resource)
            sleep(1)
            
            n_readers -= 1
            #sleep(1)
            
            if n_readers == 0:
                resource_lock_.release()

            print("%s reader left the room" % (self.name))
            sleep(1) 


            counter += 1



class control(Thread):
    def run(self):

        global counter
        global resource
        global n_readers
        global resource_lock_

        if n_readers == 0:

            resource_lock_.acquire()

        n_readers -= 1

        resource_lock_.release()



        
















obj1 = reader()
obj2 = reader()
obj3 = reader()

#wobj = writer()
#wobj2 = writer()


#Skapar threads for klassen reader
obj1.start()
obj2.start()
obj3.start()
##wobj.start()
#wobj2.start()






