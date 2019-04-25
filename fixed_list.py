class FixedList:
    sampleRate = 44100  # audio sample rate
    trackingTime = 30   # frame of time in secs that we want to track in this list

    def __init__(self, dataChunk):
        self.maxSize = int((self.sampleRate * self.trackingTime)/dataChunk)    # set max list size as amount of values that should be in 30 seconds
        self.size = 0
        self.front = 0
        self.back = -1
        self.data = []  # init data list
    
    # append data values
    def append(self, x):
        # if haven't yet maxed out array
        if self.size < self.maxSize:
            self.data.append(x)
            self.size += 1
            self.back += 1
            return

        # already maxed out, need to keep track of front/back
        else:
            # increment back/front with wrap
            self.back = (self.back + 1) % self.maxSize
            self.front = (self.front + 1) % self.maxSize

            # add data value at appropriate spot [the back]
            self.data[self.back] = x
            return

    # convert to regular list where front is at front, and return list
    def toList(self):
        realList = []               # init empty list
        iterator = self.front     # set iterator to front

        # run through data in correct order from beginning of data, appending to list
        for i in range (self.size):
            realList.append(self.data[iterator])
            iterator = (iterator + 1) % self.maxSize
            i += 1
        
        return realList