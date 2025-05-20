from abc import ABC, abstractmethod

class Kandidaat(ABC):
    def __init__(self, naam_kandidaat):
        self.__naam_kandidaat = naam_kandidaat
        self.__stemmen = []

    def geef_stem(self, stem):
        if isinstance(stem, Stem):
            self.get_stemmen.append(stem)
        else:
            raise ValueError('Ongeldige stem')

    @property
    def get_stemmen(self):
        return self.__stemmen
    
    @property
    def get_naam_kandidaat(self):
        return self.__naam_kandidaat

    @abstractmethod
    def __str__(self):
        return f'{self.get_naam_kandidaat} '
    
class Stem(ABC):
    def __init__(self, kandidaat):
        if not isinstance(kandidaat, Kandidaat):
            raise ValueError('Ongeldige kandidaat')
        self.__kandidaat = kandidaat
    
    @property
    def get_kandidaat(self):
        return self.__kandidaat

    @abstractmethod
    def __str__(self):
        return f'Stem op {self.get_kandidaat} '
    
class Kiezer(ABC):
    def __init__(self, naam_kiezer):
        self.__naam_kiezer = naam_kiezer

    @property
    def get_naam_kiezer(self):
        return self.__naam_kiezer

    @abstractmethod
    def stem(self, kandidaat):
        pass
    
    @abstractmethod
    def __str__(self):
        return f'Kiezer: {self.get_naam_kiezer}'