class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Свойство для получения названия книги (только для чтения)"""
        return self._name

    @property
    def author(self) -> str:
        """Свойство для получения автора книги (только для чтения)"""
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.name = name
        self.author = author
        self.pages = pages

    @property
    def pages(self):
        """Свойство для получения количества страниц"""
        return self._pages

    @pages.setter
    def pages(self, value):
        """Сеттер с проверкой количества страниц"""
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        # Перегружаем метод для добавления информации о страницах
        return f"{super().__str__()}. Страниц: {self._pages}"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.name = name
        self.author = author
        self.duration = duration

    @property
    def duration(self):
        """Свойство для получения длительности аудиокниги"""
        return self._duration

    @duration.setter
    def duration(self, value):
        """Сеттер с проверкой длительности"""
        if not isinstance(value, (int, float)):
            raise TypeError("Длительность должна быть числом")
        if value <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self._duration = float(value)

    def __str__(self):
        # Перегружаем метод для добавления информации о длительности
        return f"{super().__str__()}. Длительность: {self._duration} часов"
