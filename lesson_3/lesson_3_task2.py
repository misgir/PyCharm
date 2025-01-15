from Smartphone import Smartphone

catalog = [
    Smartphone("brand1", "model1", "+78005553535"),
    Smartphone("brand2", "model2", "+78887567576"),
    Smartphone("brand3", "model3", "+79090909092"),
    Smartphone("brand4", "model4", "+79090909093"),
    Smartphone("brand5", "model5", "+79090909094"),
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")
