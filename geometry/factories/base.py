from abc import ABC, abstractmethod


class FigureCreator(ABC):
    @abstractmethod
    def create_figure(self):
        pass
