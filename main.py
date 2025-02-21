import asyncio
import uuid
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

# 🔥 Словарь для хранения user_id по username
users_map = {}


async def simulate_user_session(username):
    """
    Симуляция сессии пользователя с несколькими случайными действиями.
    """
    # 🔥 Гарантируем, что у одного username всегда один user_id
    if username not in users_map:
        users_map[username] = randint(9999, 100000)  # Генерируем user_id, если его ещё нет

    user_id = users_map[username]  # Получаем закрепленный user_id

    with structlog.contextvars.bound_contextvars(user_id=user_id, username=username, stream_id=str(uuid.uuid4())):
        logger.info(f"Юзер {username} зашел на сайт", _event="login")

        num_events = randint(2, 6)
        for _ in range(num_events):
            await asyncio.sleep(randint(1, 10))
            _event = choice(["profile", "products", "view_product", "logout", "delete_account"])

            if _event == "profile":
                logger.info(f"Юзер {username} перешел в профиль", _event="profile")
            elif _event == "products":
                logger.info(f"Юзер {username} перешел в товары", _event="products")
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
                logger.info(f"Юзер {username} вышел из аккаунта", _event="logout")
                return
            elif _event == "delete_account":
                logger.info(f"Юзер {username} удалил аккаунт", _event="delete_account")
                return

        await asyncio.sleep(randint(1, 10))
        final_event = choice(["logout", "delete_account"])
        if final_event == "logout":
            logger.info(f"Юзер {username} вышел из аккаунта", _event="logout")
        else:
            logger.info(f"Юзер {username} удалил аккаунт", _event="delete_account")


async def main():
    tasks = []
    while True:
        await asyncio.sleep(randint(0, 3))
        username = choice(usernames)  # Выбираем случайного юзера
        task = asyncio.create_task(simulate_user_session(username))
        tasks.append(task)
        tasks = [t for t in tasks if not t.done()]


if __name__ == '__main__':
    InitLoggers()
    asyncio.run(main())
