import pyautogui
import time
# import keyboard
from pynput import keyboard
# print(pyautogui.size())
temp = True

# pyautogui.FailSafeException: PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED
pyautogui.FAILSAFE = False


# while True:
#     if keyboard.read_key() == "p":
#         print("You pressed p")
#         temp = False
#         break
# while True:
#     if keyboard.is_pressed("q"):
#         print("You pressed q")
#         temp = False
#         break

# keyboard.on_press_key("r", lambda _: print("You pressed r"))


# def on_press(key):
#     try:
#         print("Alphanumeric key pressed: {0} ".format(key.char))
#     except AttributeError:
#         print("special key pressed: {0}".format(key))


# def on_release(key):
#     print("Key released: {0}".format(key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False


# # Collect events until released
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()


while(temp):
    time.sleep(2)
    print(pyautogui.position())

    # mac = 손쉬운 사용 vscode 사용 권한 설정
    # pyautogui.moveTo(100, 200) # x 100, y 200 위치로 바로 이동
    pyautogui.moveTo(1910, 500, 2) # x 100, y 200 위치로 2초동안 이동

    # pyautogui.click()
    pyautogui.click(button='right')
    # pyautogui.doubleClick()
    # pyautogui.click(clicks=3, interval=1) # 3번 클릭할건데 1초마다

    # 816,81 -> 539,80
    pyautogui.moveTo(900,500, 2)
    # pyautogui.dragTo(539,80, 2)

    pyautogui.moveTo(100, 500, 2) # x 100, y 200 위치로 2초동안 이동
    print('end')