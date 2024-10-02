from custom_logger import logger

class Enemy:
    difficulty_multiplier: int = 1

    @classmethod
    def increase_difficulty(cls):
        cls.difficulty_multiplier += 1
        logger.info("Difficulty increased")

    @classmethod
    def decrease_difficulty(cls):
        cls.difficulty_multiplier = max(1, cls.difficulty_multiplier - 1)
        logger.warning("Difficulty decreased")

    def __init__(self, hp: int, attack: int, name: str, personal_multiplier: int = 1):
        self.HP: int = hp
        self.attack: int = attack
        self.name: str = name
        self.personal_multiplier: int = personal_multiplier

    def get_HP(self) -> int:
        return self.HP * type(self).get_difficulty() * self.personal_multiplier

    def get_attack(self) -> int:
        return self.attack * type(self).get_difficulty() * self.personal_multiplier

    def __repr__(self):
        return f"Name: {self.name}, HP: {self.get_HP()}, attack: {self.get_attack()}"

    @classmethod
    def get_difficulty(cls):
        return cls.difficulty_multiplier


class Troll(Enemy):

    @classmethod
    def get_difficulty(cls):
        return cls.difficulty_multiplier * 2 if cls.difficulty_multiplier > 1 else cls.difficulty_multiplier


class Wolf(Enemy):
    pass


if __name__ == '__main__':


    Zbysiu = Enemy(
        hp=100,
        attack=50,
        name="Zbysiu"
    )

    Shrek = Troll(
        hp=500,
        name="Shrek",
        attack=320
    )

    Robert = Wolf(
        hp=321,
        attack=123,
        name="Robert"
    )

    SnowTroll = Troll(
        hp=342,
        attack=83,
        name="snowTroll",
        personal_multiplier=3
    )

    print(Zbysiu)
    print(Shrek)
    print(Robert)
    print(SnowTroll)
    Enemy.increase_difficulty()

    print(Zbysiu)
    print(Shrek)
    print(Robert)
    print(SnowTroll)

    Enemy.decrease_difficulty()