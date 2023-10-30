try:
    num1=int(input("Первое число: "))
    num2=int(input("Второе число: "))
    result=num1/num2
    print(result)

# except ZeroDivisionError: # срабатывает при прерывании только с этой ошибкой
#     print("Деление на 0")
# except ValueError:
#     print("Некорректное значение")
# except Exception: # позволяет вывести информацию не прерывая выполнение программы; Exception - включает в себя все прерывания
#     print("Something went wrong")

except ZeroDivisionError as e: # as e - выводит текст ошибки
    print(e)
    print("Деление на 0")
except ValueError as e: # invalid literal for int() with base 10: 's'
    print(e)
    print("Некорректное значение")
except Exception as e:
    print(e)
    print("Something went wrong")
else:                   # срабатывает, если не произошли прерывания
    print("All good")
finally:                # срабатывает всегда в конце вне зависимости от того, были ли прерывания
    print("This will always execute")