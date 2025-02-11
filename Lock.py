class Lock:
    def __init__(self, length, water_fill_time, water_empty_time):
        self.m_isfull = False  # Whether the lock is full
        self.m_length = length  # The length of the lock
        self.s_waterfillTime = water_fill_time  # The time for the lock to fill the water
        self.s_waterEmptyTime = water_empty_time  # The time for the lock to empty the water

    def processBoats(self, boats):
        """
        Process the boats in the lock
        """
        processing_time = 0
        #enter the lock
        for boat in boats:
            processing_time += boat.getLength()
        if self.m_isfull:
            processing_time += self.empty()
        else:
            processing_time += self.fill()

        # exit the lock
        for boat in boats:
            processing_time += boat.getLength()
        return processing_time

    def fill(self):
        """
        Fill the lock with water
		"""
        if self.m_isfull:
            return 0
        self.m_isfull = True
        return self.s_waterfillTime

    def empty(self):
        """
        Empty the lock of water
        """
        if not self.m_isfull:
            return 0
        self.m_isfull = False
        return self.s_waterEmptyTime