class BoatQueue:
    def __init__(self, boats=[]):
        self.m_boats = boats  # The boats currently in the queue

    def getMaxBoatsToLock(self, lockSize :int):
        """
        Get and remove the maximum number of boats that can fit in the lock size
        """
        max_boats = []
        if len(self.m_boats) == 0:
            return max_boats
        while lockSize > 0:
            if len(self.m_boats) == 0:
                break
            boat = self.m_boats[0]
            if boat.getLength() <= lockSize:
                max_boats.append(boat)
                lockSize -= boat.getLength()
                self.m_boats.pop(0)
            else:
                break
        return max_boats

    def isEmpty(self):
        return len(self.m_boats) == 0