import configparser
import os

def device_id():
    device_list_file_path = os.path.join(os.path.dirname(__file__), "device_list.txt")

    if not os.path.exists(device_list_file_path):
        raise FileNotFoundError(f"Config file not found: {device_list_file_path}")

    device_config = configparser.ConfigParser()
    device_config.read(device_list_file_path)

    print("Sections found in config file:", device_config.sections())

    if 'devices' in device_config:
        return device_config['devices']['udid']
    else:
        raise ValueError("[devices] section missing in device_list.txt")
