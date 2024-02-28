import pyautogui

# Obtenha a posição atual do cursor do mouse
x, y = pyautogui.position()

# Imprima as coordenadas x e y
print(f'Posição do cursor do mouse: x = {x}, y = {y}')
