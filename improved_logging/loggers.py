from improved_logging.main import LoggerReg, SetupLogger, JSONFORMAT_HANDLER


class InitLoggers:

    main = LoggerReg(name="MAIN", level=LoggerReg.Level.DEBUG)

    def __init__(self) -> None:
        SetupLogger(
            name_registration=[
                self.main,
            ],
            select_format=JSONFORMAT_HANDLER,
            ensure_ascii=False
        )


if __name__ == "__main__":
    test_logger = InitLoggers.main

    print(type(test_logger))    # <class 'src.infrastructure.logging.main.LoggerReg'>
    print(test_logger)          # LoggerReg(name='MAIN', level=<Level.DEBUG: 'DEBUG'>, propagate=False, write_file=False)

    test_logger_name = InitLoggers.main.name

    print(type(test_logger_name))   # <class 'str'>
    print(test_logger_name)         # MAIN
