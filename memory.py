class Memory:
    __memory_storage = list()
    
    def __init__(self) -> None:
        self.memory_storage = []
        pass

    def reset_memory(self): #MC
        self.memory_storage.clear()  

    def recover_last_memory(self): #MR 
        return self.memory_storage[0] if len(self.memory_storage) > 0 else None

    def add_to_last_memory(self, num): #M+
        self.memory_storage[0] += num

    def subtract_to_last_memory(self, num): #M-
        self.memory_storage[0] -= num

    def insert_to_memory(self, num): #MS
        self.memory_storage.insert(0, num) 

    def get_memory(self):
        return self.memory_storage
    
    def get_memory_by_index(self, index):
        return self.memory_storage[index]

    def delete_memory(self, index):
        self.memory_storage.pop(index) if index != None else self.memory_storage.pop()        