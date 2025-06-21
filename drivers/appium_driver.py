import json,os
from appium import webdriver
from appium.options.android import UiAutomator2Options

# This commented was for one deivce .. loading config.json
def load_config():
    with open("config/config.json") as f:
        return json.load(f)

def create_driver():
    config=load_config()
    options=UiAutomator2Options().load_capabilities(config)

    os.system(f"adb -s {config['udid']} shell am force-stop {config['appPackage']}")
    return webdriver.Remote("http://127.0.0.1:4723",options=options)

# running on two devices now
#
# def load_config(config_path):
#     with open(config_path) as f:
#         return json.load(f)
#
# def create_driver(configPath):
#     config=load_config(configPath)
#     options=UiAutomator2Options().load_capabilities(config)
#
#     os.system(f"adb -s {config['udid']} shell am force-stop {config['appPackage']}")
#     return webdriver.Remote("http://127.0.0.1:4723",options=options)