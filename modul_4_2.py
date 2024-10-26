def test_function ():
    def inner_function ():
        print("Я нахожусь в области видимости функции test_function")

        inner_function() # ни чего не происходит

    inner_function() # ни чего не происходит


# inner_function() ошибка, имя не определено
