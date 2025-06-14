from pypresence import Presence
import json
import time

# Загружаем конфиг
with open("rests.json", "r") as file:
    config = json.load(file)

client_id = config[1383557334097203332]  # ID приложения Discord
rpc = Presence(client_id)
rpc.connect()

while True:
    rpc.update(**config["data"])  # Обновляем статус
    time.sleep(15)  # Обновление каждые 15 секунд
