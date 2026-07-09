class Task:
    def __init__(self,name,priority,deadline,done = False):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.done = done

    def to_dict(self):
        return{
            "task":self.name,
            "done":self.done,
            "priority":self.priority,
            "deadline":self.deadline
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["task"],
            data["priority"],
            data["deadline"],
            data["done"]
        )