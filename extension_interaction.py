import time
import pyautogui


def interact_with_extension():
    try:
        chrome_x, chrome_y = 1105, 96
        pyautogui.click(chrome_x, chrome_y)
        time.sleep(2)

        x_extension, y_extension = 815, 250
        pyautogui.click(x_extension, y_extension)

        x_save, y_save = 615, 477
        pyautogui.click(x_save, y_save)
        time.sleep(1002)

    except Exception as e:
        print(f"An error occurred while interacting with the extension: {str(e)}")
