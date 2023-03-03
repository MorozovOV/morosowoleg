# Имеется список вещественных чисел [1.3, 2.5, 3.1]. Создайте множество квадратов этих чисел, использовав для этого генератор множеств. Выведите полученное множество на экран.
n = int(input('Введите n: '))
list_fib = [0, 1]
def gen_fib(num):
  k = 2
  for num in list_fib:
    while k < n:
      new_num = list_fib[k-1] + list_fib[k-2]
      list_fib.append(new_num)
      k += 1
  return list_fib
print(gen_fib(n))
print(sum(list_fib))