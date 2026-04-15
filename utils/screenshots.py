import os
from datetime import datetime

def save_screenshots(driver, test_name):
    folder = "screenshots"
    os.makedirs(folder, exist_ok = True)
    timeStamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(folder, f"{test_name}_{timeStamp}.png")
    driver.save_screenshot(path)

