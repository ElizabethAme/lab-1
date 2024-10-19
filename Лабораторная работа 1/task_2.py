# TODO Найдите количество книг, которое можно разместить на дискете
one_simbol = 4 # в байтах
one_in_line = 25 * one_simbol
one_in_page = 50 * one_in_line
one_in_book = 100 * one_in_page

book = one_in_book / 1024 / 1024 # в мегабайтах

total = 1.44
count_of_book = total / book

print("Количество книг, помещающихся на дискету:", int(count_of_book))
