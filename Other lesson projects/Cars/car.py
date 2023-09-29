class Car:
    def __init__(self, fabricator, color, storage):
        self.fabricator = fabricator
        self.color = color
        self.storage = storage

    def set_fabricator (self, fabricator):
        self.fabricator = fabricator

    def get_fabricator (self):
        return self.fabricator
    
    def get_storage (self):
        return self.storage
    
    def get_color (self):
        return self.color
    
    def set_storage (self, storage):
        self.storage = storage