class Memory:
    """ChromaDB-based global memory for agent communication."""
    def __init__(self):
        self.memory = {}
    def store(self, key, value):
        self.memory[key] = value
        print(f"Memory: Stored {key}.")
    def retrieve(self, key):
        print(f"Memory: Retrieved {key}.")
        return self.memory.get(key, None)
