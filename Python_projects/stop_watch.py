import time

class Stop_watch:
    k = True
    count = False
    def __init__(self,initial_):
        self.initial = initial_
        while self.initial > 0:
            print(self.initial, end = '\r')
            if Stop_watch.k == False:
                # self.stop_value = initial
                # print(initial, end = '\r') 
                break
            else :
                if Stop_watch.count == True: 
                    self.stop_value = self.initial
                    self.initial -= 1
            self.stop_value = self.initial
            self.initial += 1
            time.sleep(1)
        # print("0", end = '\r')

    def start(self):
        while self.initial > 0:
            print(self.initial, end = '\r')
            if Stop_watch.k == False:
                # self.stop_value = initial
                # print(initial, end = '\r') 
                break
            else :
                if Stop_watch.count == True: 
                    self.stop_value = self.initial
                    self.initial -= 1
                self.stop_value = self.initial
                self.initial += 1
            time.sleep(1)
            
        

    def stop(self):
        Stop_watch.k = False
        print(self.stop_value, end = '/r')

    def resume(self):
        Stop_watch.k = True
        Stop_watch.start(self.stop_value)

    def count_down(self,count_value):
        Stop_watch.count = True
        Stop_watch.start(count_value)

harish = Stop_watch(1)
# harish.start()
harish.stop()