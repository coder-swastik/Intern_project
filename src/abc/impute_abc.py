from abc import ABC, abstractmethod

class Imputation(ABC):    
    @abstractmethod
    def apply(self, df, column):
        raise NotImplementedError('Subclasses should implement this method')
