#Задача "Учёт товаров":
class Product:

    def __init__(self, name=str, weight=float, category=str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'
    str_file = ''

    def get_products(self):
        file = open(self.__file_name, 'r')
        self.str_file = file.read()
        file.close()
        return self.str_file

    def add(self, *products):
        file = open(self.__file_name, 'a')
        self.get_products()
        if self.str_file == '':
            for i in products:
                file.write(str(i) + '\n')
            file.close()
        else:
            for i in products:
                if str(i.name) in self.str_file:
                    print(f'Продукт {i} уже есть в магазине')
                    continue
                else:
                    file.write(str(i) + '\n')
            file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
