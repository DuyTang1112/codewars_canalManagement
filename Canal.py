class Canal:
    def __init__(self, lock, low_queue, high_queue):
        self.m_Lock = lock  # The lock
        self.m_lowQueue = low_queue  # The low queue
        self.m_highQueue = high_queue  # The high queue

    def process(self):
        total_time = 0
        while not self.m_lowQueue.isEmpty() or not self.m_highQueue.isEmpty():
            # print("---------------")
            if not self.m_Lock.m_isfull:
                queue_to_process = self.m_lowQueue
                # print("Low Queue")
            else:
                queue_to_process = self.m_highQueue
                # print("High Queue")

            max_boats = queue_to_process.getMaxBoatsToLock(self.m_Lock.m_length)
            # print([boat.getLength() for boat in max_boats])
            total_time += self.m_Lock.processBoats(max_boats)
            # print("total_time ", total_time)

        if self.m_Lock.m_isfull:
            total_time += self.m_Lock.empty()

        return total_time