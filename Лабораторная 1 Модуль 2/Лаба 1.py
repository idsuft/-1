# TODO Написать 3 класса с документацией и аннотацией типов
import doctest



class Chair:
    """Класс, описывающий стул."""

    def __init__(self, material: str, max_weight: float, height: float):
        """
        Создание и подготовка к работе объекта "Стул".

        :param material: Материал стула
        :param max_weight: Максимальный поддерживаемый вес (кг)
        :param height: Высота стула (см)

        Примеры:
        >>> chair = Chair("wood", 120.5, 45.0)  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        if not material:
            raise ValueError("Материал не может быть пустой строкой")
        self.material = material

        if not isinstance(max_weight, (int, float)):
            raise TypeError("Максимальный вес должен быть типа int или float")
        if max_weight <= 0:
            raise ValueError("Максимальный вес должен быть положительным числом")
        self.max_weight = max_weight

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

    def can_support_person(self, person_weight: float) -> bool:
        """
        Проверяет, может ли стул выдержать вес человека.

        :param person_weight: Вес человека (кг)
        :return: True если стул выдержит, иначе False

        Примеры:
        >>> chair = Chair("wood", 120.5, 45.0)
        >>> chair.can_support_person(80.0)
        """
        if not isinstance(person_weight, (int, float)):
            raise TypeError("Вес человека должен быть типа int или float")
        if person_weight <= 0:
            raise ValueError("Вес человека должен быть положительным числом")
        ...

    def adjust_height(self, new_height: float) -> None:
        """
        Регулировка высоты стула (если стул регулируемый).

        :param new_height: Новая высота стула (см)
        :raise ValueError: Если новая высота выходит за допустимые пределы

        Примеры:
        >>> chair = Chair("wood", 120.5, 45.0)
        >>> chair.adjust_height(50.0)
        """
        if not isinstance(new_height, (int, float)):
            raise TypeError("Новая высота должна быть типа int или float")
        if new_height <= 0:
            raise ValueError("Новая высота должна быть положительным числом")
        ...


class Tree:
    """Класс, описывающий дерево."""

    def __init__(self, species: str, age: int, height: float):
        """
        Создание и подготовка к работе объекта "Дерево".

        :param species: Вид дерева
        :param age: Возраст дерева (лет)
        :param height: Высота дерева (метры)

        Примеры:
        >>> tree = Tree("oak", 50, 25.5)  # инициализация экземпляра класса
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть типа str")
        if not species:
            raise ValueError("Вид дерева не может быть пустой строкой")
        self.species = species

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

    def get_annual_growth(self) -> float:
        """
        Рассчитывает среднегодовой прирост дерева.

        :return: Среднегодовой прирост в метрах

        Примеры:
        >>> tree = Tree("oak", 50, 25.5)
        >>> tree.get_annual_growth()
        """
        ...

    def is_mature(self) -> bool:
        """
        Проверяет, является ли дерево зрелым (возраст > 30 лет).

        :return: True если дерево зрелое, иначе False

        Примеры:
        >>> tree = Tree("oak", 50, 25.5)
        >>> tree.is_mature()
        """
        ...


class SocialNetwork:
    """Класс, описывающий социальную сеть."""

    def __init__(self, name: str, active_users: int, founded_year: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть".

        :param name: Название социальной сети
        :param active_users: Количество активных пользователей
        :param founded_year: Год основания

        Примеры:
        >>> network = SocialNetwork("TestNetwork", 1000000, 2010)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        if not name:
            raise ValueError("Название не может быть пустой строкой")
        self.name = name

        if not isinstance(active_users, int):
            raise TypeError("Количество пользователей должно быть типа int")
        if active_users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        self.active_users = active_users

        if not isinstance(founded_year, int):
            raise TypeError("Год основания должен быть типа int")
        if founded_year <= 0:
            raise ValueError("Год основания должен быть положительным числом")
        self.founded_year = founded_year

    def calculate_user_growth_rate(self, previous_year_users: int) -> float:
        """
        Рассчитывает темп роста пользователей по сравнению с предыдущим годом.

        :param previous_year_users: Количество пользователей в предыдущем году
        :return: Темп роста в процентах

        Примеры:
        >>> network = SocialNetwork("TestNetwork", 1000000, 2010)
        >>> network.calculate_user_growth_rate(800000)
        """
        if not isinstance(previous_year_users, int):
            raise TypeError("Количество пользователей должно быть типа int")
        if previous_year_users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        ...

    def add_users(self, new_users: int) -> None:
        """
        Добавляет новых пользователей в социальную сеть.

        :param new_users: Количество новых пользователей
        :raise ValueError: Если количество новых пользователей отрицательное

        Примеры:
        >>> network = SocialNetwork("TestNetwork", 1000000, 2010)
        >>> network.add_users(50000)
        """
        if not isinstance(new_users, int):
            raise TypeError("Количество новых пользователей должно быть типа int")
        if new_users < 0:
            raise ValueError("Количество новых пользователей не может быть отрицательным")
        ...




if __name__ == "__main__":
    # Пример использования классов
    my_chair = Chair("plastic", 100, 40)
    print(f"Стул из материала: {my_chair.material}")

    my_tree = Tree("birch", 20, 15.5)
    print(f"Дерево вида: {my_tree.species}")

    my_network = SocialNetwork("MySocial", 5000, 2020)
    print(f"Социальная сеть: {my_network.name}")

    # Тестирование с помощью doctest
    doctest.testmod(verbose=True)
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
