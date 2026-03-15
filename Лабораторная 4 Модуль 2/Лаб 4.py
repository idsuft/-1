if __name__ == "__main__":
    # Write your solution here
    pass
from abc import ABC, abstractmethod
from typing import Optional


class Vehicle(ABC):
    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
        _brand (str): Марка транспортного средства (непубличный)
        _model (str): Модель транспортного средства (непубличный)
        _year (int): Год выпуска
        _speed (float): Текущая скорость
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация базового транспортного средства.

        Args:
            brand: Марка автомобиля
            model: Модель автомобиля
            year: Год выпуска
        """
        self._brand = brand
        self._model = model
        self._year = year
        self._speed = 0.0

    @abstractmethod
    def start(self) -> str:
        """Запуск двигателя (абстрактный метод)."""
        pass

    def accelerate(self, increment: float) -> float:
        """
        Увеличение скорости.

        Args:
            increment: Значение увеличения скорости

        Returns:
            Текущая скорость после ускорения
        """
        self._speed += increment
        return self._speed

    def get_info(self) -> str:
        """
        Получение базовой информации о транспортном средстве.

        Returns:
            Строка с информацией
        """
        return f"{self._brand} {self._model} ({self._year})"

    def __str__(self) -> str:
        """Строковое представление для пользователей."""
        return f"Транспортное средство: {self.get_info()}"

    def __repr__(self) -> str:
        """Официальное строковое представление для разработчиков."""
        return f"Vehicle(brand='{self._brand}', model='{self._model}', year={self._year})"


class Car(Vehicle):
    """
    Класс легкового автомобиля (наследуется от Vehicle).

    Дополнительные атрибуты:
        _doors (int): Количество дверей
        _fuel_type (str): Тип топлива
    """

    def __init__(self, brand: str, model: str, year: int,
                 doors: int, fuel_type: str) -> None:
        """
        Инициализация легкового автомобиля.

        Args:
            brand: Марка
            model: Модель
            year: Год выпуска
            doors: Количество дверей
            fuel_type: Тип топлива
        """
        # Расширение конструктора базового класса
        super().__init__(brand, model, year)
        self._doors = doors
        self._fuel_type = fuel_type

    def start(self) -> str:
        """
        Запуск двигателя легкового автомобиля.

        Returns:
            Сообщение о запуске
        """
        return f"Легковой автомобиль {self._brand} {self._model} заведён. " \
               f"Тип топлива: {self._fuel_type}"

    def get_info(self) -> str:
        """
        Перегруженный метод получения информации.

        Причина перегрузки: для легкового автомобиля важно указать
        количество дверей и тип топлива, чтобы пользователь имел
        полное представление об автомобиле.

        Returns:
            Расширенная информация об автомобиле
        """
        base_info = super().get_info()
        return f"{base_info}, Дверей: {self._doors}, Топливо: {self._fuel_type}"

    def __str__(self) -> str:
        """Перегруженный строковый метод для легкового автомобиля."""
        return f"Легковой автомобиль: {self.get_info()}"

    def __repr__(self) -> str:
        """Перегруженный repr для легкового автомобиля."""
        return (f"Car(brand='{self._brand}', model='{self._model}', "
                f"year={self._year}, doors={self._doors}, "
                f"fuel_type='{self._fuel_type}')")


class Truck(Vehicle):
    """
    Класс грузового автомобиля (наследуется от Vehicle).

    Дополнительные атрибуты:
        _capacity (float): Грузоподъёмность в тоннах
        _current_load (float): Текущая загрузка в тоннах
    """

    def __init__(self, brand: str, model: str, year: int,
                 capacity: float) -> None:
        """
        Инициализация грузового автомобиля.

        Args:
            brand: Марка
            model: Модель
            year: Год выпуска
            capacity: Грузоподъёмность в тоннах
        """
        super().__init__(brand, model, year)
        self._capacity = capacity
        self._current_load = 0.0

    def start(self) -> str:
        """
        Запуск двигателя грузового автомобиля.

        Returns:
            Сообщение о запуске
        """
        return f"Грузовой автомобиль {self._brand} {self._model} готов к работе. " \
               f"Грузоподъёмность: {self._capacity} т"

    def load(self, weight: float) -> Optional[str]:
        """
        Загрузка груза.

        Args:
            weight: Вес груза в тоннах

        Returns:
            Сообщение об успешной загрузке или None при перегрузе
        """
        if self._current_load + weight <= self._capacity:
            self._current_load += weight
            return f"Груз загружен. Текущая загрузка: {self._current_load} т"
        else:
            return None  # Перегруз

    def get_info(self) -> str:
        """
        Перегруженный метод получения информации.

        Причина перегрузки: для грузовика критически важна информация
        о грузоподъёмности и текущей загрузке, чтобы избежать перегруза.

        Returns:
            Информация о грузовике с данными о грузе
        """
        base_info = super().get_info()
        return (f"{base_info}, Грузоподъёмность: {self._capacity} т, "
                f"Загружено: {self._current_load} т")

    def __str__(self) -> str:
        """Перегруженный строковый метод для грузовика."""
        return f"Грузовой автомобиль: {self.get_info()}"

    def __repr__(self) -> str:
        """Перегруженный repr для грузовика."""
        return (f"Truck(brand='{self._brand}', model='{self._model}', "
                f"year={self._year}, capacity={self._capacity})")


if __name__ == "__main__":
    # Пример использования
    car = Car("Toyota", "Camry", 2020, 4, "бензин")
    truck = Truck("Volvo", "FH16", 2019, 20.5)

    print(car)  # Легковой автомобиль: Toyota Camry (2020), Дверей: 4, Топливо: бензин
    print(repr(car))  # Car(brand='Toyota', model='Camry', year=2020, doors=4, fuel_type='бензин')
    print(car.start())  # Легковой автомобиль Toyota Camry заведён. Тип топлива: бензин

    print(truck)  # Грузовой автомобиль: Volvo FH16 (2019), Грузоподъёмность: 20.5 т, Загружено: 0.0 т
    print(truck.load(5))  # Груз загружен. Текущая загрузка: 5.0 т
    print(truck.start())  # Грузовой автомобиль Volvo FH16 готов к работе. Грузоподъёмность: 20.5 т
