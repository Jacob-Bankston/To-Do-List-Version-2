class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority

    @staticmethod
    def from_dictionary(dict):
        return Task(dict["title"], dict["priority"])

