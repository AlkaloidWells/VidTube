import os
from .misc import yaml_coerce


def get_settings_from_environment(prefix):
    """
    Django settings specific to the environment (eg. production) will be stored as environment variables
    prefixed with "PREFIX_", eg. prefix="VIDTUBESETTINGS_"
    E.G. environment variables like VIDTUBESETTINGS_SECRET_KEY=123, VIDTUBESETTINGS_DATABASE="{'DB': {'NAME': 'db'}}"
    will be converted to pure Python dictionary with the prefix "VIDTUBESETTINGS_" removed from the keys
    {
       "SECRET_KEY": 123,
       "DB": {'NAME': 'db'}
    }
    """
    prefix_len = len(prefix)
    return {key[prefix_len:]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}
