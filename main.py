import asyncio
from random import randint, choice
import structlog

from improved_logging.loggers import InitLoggers

logger: structlog.BoundLogger = structlog.getLogger(InitLoggers.main.name)

usernames = [
    "CyberNinja", "ShadowHunter", "QuantumLeap", "NeonBlaze", "PhantomRider", "SilverFox", "MysticWolf", "IronClad",
    "GoldenEagle", "CrimsonTide", "NightOwl", "StormChaser", "FrostByte", "DarkKnight", "SolarFlare", "OceanMaster",
    "ThunderBolt", "BlazeRunner", "SkyPirate", "LunarGhost", "SteelTitan", "VenomStrike", "ArcticWolf", "InfernoDragon",
    "CosmicDrift", "EchoFox", "RogueAgent", "PhoenixRise", "ShadowStalker", "IronWolf", "CrimsonBlade", "NightHawk",
    "StormRider", "FrostWolf", "DarkPhoenix", "SolarWind", "OceanRider", "ThunderWolf", "BlazeStorm", "SkyHunter",
    "LunarWolf", "SteelWolf", "VenomWolf", "ArcticFox", "InfernoWolf", "CosmicWolf", "EchoWolf", "RogueWolf"
]

product_names = [
    "Косметика", "Электроника", "Книги", "Одежда", "Игрушки", "Продукты", "Спорттовары", "Домашняя техника",
    "Садовая техника"
]


async def simulate_user_session(username, user_id):
    """
    Симуляция сессии пользователя с несколькими случайными действиями.
    """
    logger.info(f"Юзер {username} зашел на сайт", user_id=user_id, username=username, _event="login")

    num_events = randint(2, 6)
    for _ in range(num_events):
        await asyncio.sleep(randint(1, 10))
        _event = choice(["profile", "products", "view_product", "logout", "delete_account"])

        if _event == "profile":
            logger.info(f"Юзер {username} перешел в профиль", user_id=user_id, username=username, _event="profile")
        elif _event == "products":
            logger.info(f"Юзер {username} перешел в товары", user_id=user_id, username=username, _event="products")
        elif _event == "view_product":
            product = choice(product_names)
            logger.info(
                f"Юзер {username} смотрит товар {product}",
                user_id=user_id,
                username=username,
                _event="view_product",
                product=product
            )
        elif _event == "logout":
            logger.info(f"Юзер {username} вышел из аккаунта", user_id=user_id, username=username, _event="logout")
            return
        elif _event == "delete_account":
            logger.info(f"Юзер {username} удалил аккаунт", user_id=user_id, username=username, _event="delete_account")
            return

    await asyncio.sleep(randint(1, 10))
    final_event = choice(["logout", "delete_account"])
    if final_event == "logout":
        logger.info(f"Юзер {username} вышел из аккаунта", user_id=user_id, username=username, _event="logout")
    else:
        logger.info(f"Юзер {username} удалил аккаунт", user_id=user_id, username=username, _event="delete_account")


async def main():
    tasks = []
    while True:
        await asyncio.sleep(randint(1, 5))
        username = choice(usernames)
        user_id = randint(9999, 100000)
        task = asyncio.create_task(simulate_user_session(username, user_id))
        tasks.append(task)
        tasks = [t for t in tasks if not t.done()]


if __name__ == '__main__':
    InitLoggers()
    asyncio.run(main())
