class StateManager:
    """Centralized state management for agent workflow."""
    def __init__(self):
        self.state = {}
    def update_state(self, agent, data):
        self.state[agent] = data
        print(f"StateManager: Updated state for {agent}.")
        return self.state
