class Call(object):
    def __init__(self, uniqueId, callerName, number, time, reason):
        self.uniqueId = uniqueId
        self.callerName = callerName
        self.number = number
        self.time = time
        self.reason = reason
        
    def display(self):
        print ''
        print self.uniqueId
        print self.callerName
        print self.number 
        print self.time
        print self.reason

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queueSize = 0
    

    def add(self, newCall):
        self.calls.append(newCall)
        self.queueSize += 1
        return self
    
    def remove(self):
        if self.queueSize > 0:
            del self.calls[0]
            self.queueSize -= 1
        return self

    def info(self):
        for i in self.calls:
            i.display()
        print "Queue Size: {}".format(self.queueSize)

call1 = Call(1234, "Brian", 9114206969, 420, "mac n cheese")
call2 = Call(2345, "Ricardo", 48923452432, 330, "headphones")
call3 = Call(3456, "Burt", 53353215433, 1200, "where's Ernie")

cc = CallCenter()
cc.add(call1)
cc.add(call2)
cc.add(call3)
cc.info()
cc.remove()
cc.info()