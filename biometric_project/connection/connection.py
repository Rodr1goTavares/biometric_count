from abc import ABC, abstractmethod

class Cv2Connection(ABC):
    
    @abstractmethod
    def open_and_get_cv2():
        pass
    
    @abstractmethod
    def is_opened():
        pass
    
    @abstractmethod
    def close_cv2():
        pass
    