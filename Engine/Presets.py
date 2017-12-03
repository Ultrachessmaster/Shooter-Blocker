class TimerPreset():
    def __init__(self):
        self.timers = []
    def get_timers(self):
        return self.timers
    def reset_timers(self):
        self.timers = []
class EntitySpawnerPreset():
    def __init__(self):
        self.entities = []
    def get_entities(self):
        return self.entities
    def reset_entities(self):
        self.entities = []
    def update(self):
        return