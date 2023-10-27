# dictionary - словарь / изменяемые несортированные пары ключ:значение. Использует хэширование, поэтому быстро

capitals = {"USA": "Washington DC", "Canada": "Toronto", "GB": "London"}
# print(type(capitals))
# # print(capitals["USA"])
# print(capitals.get("GB"))  # get - позволяет без прерывания кода получить информацию из словаря
#
# if capitals.get("GB") in capitals.values():
#     print("1")
#
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items()) # keys + values
#
# for x,y in capitals.items():
#     print(x,y)

capitals.update({"Germany":"Berlin","New_country":"New_city2"})
capitals.update({"USA":"New_city"})
#capitals.pop("USA") # удаляет указанное значение
#capitals.clear() # полностью очищает словарь
print(capitals.items())