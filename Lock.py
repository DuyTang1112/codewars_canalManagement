class Lock:
    def __init__(self, length, water_fill_time, water_empty_time):
        self.m_isfull = False  # Whether the lock is full
        self.m_length = length  # The length of the lock
        self.m_currentBoats = []  # The boats that are currently in the lock
        self.s_waterfillTime = water_fill_time  # The time for the lock to fill the water
        self.s_waterEmptyTime = water_empty_time  # The time for the lock to empty the water

    def setCurrentBoats(self, boats):
        """
        Set the current boats in the lock
        """
        self.m_currentBoats = boats
        # Assuming processing time is proportional to the number of boats
        
        processing_time = -1  # Example processing time calculation. TODO implement this
        return processing_time

    def fill(self):
        """
        Fill the lock with water
		"""
        #TODO implement this
        self.m_isfull = True
        return self.s_waterfillTime

    def empty(self):
        """
        Empty the lock of water
        """
        #TODO implement this
        self.m_isfull = False
        return self.s_waterEmptyTime