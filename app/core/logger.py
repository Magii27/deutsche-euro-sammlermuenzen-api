from app.core.config import Settings


class LoggingConfig:
    def __init__(self):
        self._settings: Settings = Settings()

    def setup_logging(self):
        log_level = self._settings.LOGLEVEL.upper()

        logging_config = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                },
            },
            "root": {
                "level": log_level,
                "handlers": ["console"],
            }
        }

