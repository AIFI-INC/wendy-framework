from os import environ as env
import logging
from logging import config
from opencensus.ext.azure.log_exporter import AzureLogHandler
config_path = env.get('LOGGING_CONFIG', 'logging.conf')
try:
    config.fileConfig(config_path,
                      disable_existing_loggers=False)
except Exception as e:
    print(e)
    print("Cannot open logging config file. Use default configuration now.")


class OpenCensusDimensionsFilter(logging.Filter):
    """
    Add application-wide properties to AzureLogHandler records
    """

    def __init__(self, custom_dimensions=None):
        self.custom_dimensions = custom_dimensions or {}

    def filter(self, record):
        """
        Adds the default custom_dimensions into the current log record
        """
        cdim = self.custom_dimensions.copy()
        cdim.update(getattr(record, 'custom_dimensions', {}))
        record.custom_dimensions = cdim

        return True


def getLogger(name: str, custom_dimensions: dict = dict()) -> logging.Logger:
    log = logging.getLogger(name)
    try:
        handler = AzureLogHandler(connection_string=env.get(
            'OPENCENSUS_CONN', 'InstrumentationKey=00000000-0000-0000-0000-000000000000'))
    except Exception as e:
        print(e)
        print("Cannot use AzureLogHandler. Fallback to default logger.")
        return log
    default_properties = {
        "app_name": env.get('APP_NAME', 'wendy')
    }
    default_properties.update(custom_dimensions)
    filter = OpenCensusDimensionsFilter(custom_dimensions=default_properties)
    handler.addFilter(filter=filter)
    formatter = logging.Formatter(
        fmt="%(asctime)s loglevel=%(levelname)-6s logger=%(name)s %(funcName)s() L%(lineno)-4d %(message)s   call_trace=%(pathname)s L%(lineno)-4d")
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    log.addHandler(handler)
    return log
