import os
from datetime import datetime

def save_screenshots(driver, test_name):
    folder = "screenshots"
    os.makedirs(folder, exist_ok = True)
    timeStamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{folder}/{test_name}_{timeStamp}.png"
    driver.save_screenshot(file_name)

