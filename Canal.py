class Canal:
    def __init__(self, lock, low_queue, high_queue):
        self.m_Lock = lock  # The lock
        self.m_lowQueue = low_queue  # The low queue
        self.m_highQueue = high_queue  # The high queue

    def process(self):
        total_time = 0
        #TODO
        return total_time