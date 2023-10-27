# set - набор значений без индексов и сортировки, без повторов - из-за этого более быстрый чем лист

stoloviye_pribori={"fork","spoon","knife","knife","knife"} # повтор есть, но при работе с сетом он не учитывается
dishes={"bowl","plate","cup","knife"}
dishes2=["dishes1","dishes2","spoon"]
dishes3=("dishes3","dishes4","fork")

stoloviye_pribori.add("something")
#stoloviye_pribori.remove("fork")
#stoloviye_pribori.clear()

# stoloviye_pribori.update(dishes) # добавляет один сет в другой, также можно добавить лист или тапл (ниже)
# stoloviye_pribori.update(dishes2)
# stoloviye_pribori.update(dishes3)

# dinner=stoloviye_pribori.union(dishes)
# union в качестве результат возвращает новое множество, не меняя исходные, а update ничего не возвращает, но добавит в первое множество элементы второго.

print(stoloviye_pribori.difference(dishes)) # выводит отличные элементы именно ПЕРВОГО от ВТОРОГО, работает с листами и тайплами
print(stoloviye_pribori.difference(dishes2)) # "knife" есть в stoloviye_pribori, но нет нет в dishes2, поэтому он отображается, а spoon есть и там, и там. При этом "dishes1" и "dishes2" есть в dishes2, но нет в stoloviye_pribori, но т.к. сравниваем именно приборы - они не выводятся
print(stoloviye_pribori.difference(dishes3)) # аналогично "fork" есть, "spoon" нет
print(stoloviye_pribori.intersection(dishes)) # выводит одинаковые значения

# for x in stoloviye_pribori:
#     print(x)