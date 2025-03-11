"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

    сторона_а (довжина сторони a).
    кут_а (кут між сторонами a і b).
    кут_б (суміжний з кутом кут_а).

Необхідно реалізувати наступні вимоги:

    Значення сторони сторона_а повинно бути більше 0.
    Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
    Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення
    кут_б обчислюється автоматично.
    Для встановлення значень атрибутів використовуйте метод __setattr__.
"""

# 1 варіант классу, створенний на умовах таску
class Rhombus:
    validation_rules = {
        "side_a": lambda value: isinstance(value, (int, float)) and value > 0,
        "angle_ab": lambda value: isinstance(value, (int, float)) and 0 < value < 180,
        "angle_bc": lambda value: isinstance(value, (int, float)) and 0 < value < 180,
        "angle_cd": lambda value: isinstance(value, (int, float)) and 0 < value < 180,
        "angle_da": lambda value: isinstance(value, (int, float)) and 0 < value < 180,
    }

    def __init__(self, side_a, angle_ab, angle_bc):
        self.side_a = side_a
        self.angle_ab = angle_ab
        self.angle_bc = angle_bc
        self.angle_cd = angle_ab
        self.angle_da = angle_bc
        self.check_angles()

    def __setattr__(self, name, value):
        if name in self.validation_rules:
            if not isinstance(value, (int, float)):
                raise TypeError(f"Значення {name} повинно бути числом більше 0")
            if not self.validation_rules[name](value):
                raise ValueError(f"Значення {name} повинно бути більше 0 та менше 180")
        super().__setattr__(name, value)

    def check_angles(self):
        if self.angle_ab + self.angle_bc != 180:
            raise ValueError("Сума суміжних кутів ромба повинна бути 180 градусів")
        if self.angle_ab == 90 and self.angle_bc == 90:
            raise ValueError("Кути ромба не можуть бути 90 градусів, бо тоді він переходе у прямокутник")

    def __str__(self):
        return f"Ромб має сторони довжиною {self.side_a}см та кути А та С {self.angle_ab} градусів, " \
               f"а кути В та D мають {self.angle_bc} градусів"

    '''Подумав, що так як написані мною умови не дадуть змінити один з кутів, бо почнеться перевірка та дасть помилку.
    Тож додав сеттер, який може змінити обидва кути.'''
    def set_angles(self, angle_ab, angle_bc):
        super().__setattr__("angle_ab", angle_ab)
        super().__setattr__("angle_bc", angle_bc)
        self.check_angles()



'''2 варіант классу. Спираючись на геометричні властивості ромбу, нам не потрібен ддрцгий кут у атрибутах,
бо ми одразу можемо його обчислити выднявши заданий від 180. Що потім сильно спростить код та перевірки в ньому.
Також спростить функціонал зміни його властивостей'''

class Rhombus_2:
    def __init__(self, side_a, angle_ab):
        self.side_a = side_a
        self.set_angles(angle_ab)

    def __setattr__(self, name, value):
        if name == "side_a":
            if not isinstance(value, (int, float)):
                raise TypeError("Довжина сторони повинна бути числом більше 0")
            if value <= 0 or not value:
                raise ValueError("Довжина сторони повинна бути числом більше 0")
        elif name == "angle_ab":
            if not isinstance(value, (int, float)):
                raise TypeError("Значення angle_ab повинно бути більше 0 та менше 180")
            if not (0 < value < 180) or not value:
                raise ValueError("Значення angle_ab повинно бути більше 0 та менше 180")
            if value == 90:
                raise ValueError("Кути ромба не можуть бути 90 градусів, бо тоді він переходе у прямокутник")
            super().__setattr__("angle_bc", 180 - value)
            super().__setattr__("angle_cd", value)
            super().__setattr__("angle_da", 180 - value)
        super().__setattr__(name, value)

    def set_angles(self, angle_ab):
        self.angle_ab = angle_ab  # Здесь автоматически обновятся все углы через __setattr__

    def __str__(self):
        return f"Ромб має сторони довжиною {self.side_a}см та кути А та С {self.angle_ab} градусів, " \
               f"а кути В та D мають {self.angle_bc} градусів"



# А як на мене, найкращій та компактніший варіант всеж таки з ініт.

class Rhombus_3:
    def __init__(self, side_a, angle_ab):
        if not isinstance(side_a, (int, float)) or side_a <= 0:
            raise ValueError("Довжина сторони повинна бути числом більше 0")
        self.side_a = side_a
        self.set_angles(angle_ab)

    def set_angles(self, angle_ab):
        if not (0 < angle_ab < 180):
            raise ValueError("Значення angle_ab повинно бути більше 0 та менше 180)")
        if not isinstance(angle_ab, (int, float)):
            raise TypeError("Значення angle_ab повинно бути більше 0 та менше 180)")
        if angle_ab == 90:
            raise ValueError("Кути ромба не можуть бути 90 градусів, бо тоді він переходе у прямокутник")
        self.angle_ab = angle_ab
        self.angle_bc = 180 - angle_ab
        self.angle_cd = angle_ab
        self.angle_da = self.angle_bc

    def __str__(self):
        return f"Ромб має сторони довжиною {self.side_a}см та кути А та С {self.angle_ab} градусів, " \
               f"а кути В та D мають {self.angle_bc} градусів"