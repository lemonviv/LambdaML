from abc import ABC, abstractmethod

class Storage(ABC):

    @abstractmethod
    def __init__(self, endpoint):
        pass

    # TODO(milos) not sure if this one is needed
    @abstractmethod
    def list_objects(self, name):
        pass

    @abstractmethod
    def get_object(self, name):
        pass

    @abstractmethod
    def set_object(self, name, data):
        pass

    @abstractmethod
    def delete_object(self, name):
        pass

    @abstractmethod
    def delete_all_objects(self):
        pass
