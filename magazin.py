import json


class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as f:
            try:
                list_ = json.load(f)
            except:
                list_ = []
        return list_

    def write(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=3)


class User:
    def __init__(self, fullname=None, username=None, password=None,myproduct = []):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.myproduct = myproduct

    def save_user(self):
        obj = File('user.json')
        list_ = obj.read()
        list_.append(self.__dict__)
        obj.write(list_)

    def check_user(self):
        obj = File('user.json')
        for i in obj.read():
            if self.username == i['username']:
                return True
            else:
                return False

    def check_login(self):
        obj = File('user.json')
        for i in obj.read():
            if i['username'] == self.username and i['password'] == self.password:
                return True
            else:
                return False
    def user_product(self):
        user = File('user.json').read()
        for i in user:
            print(*i['myproduct'], end='')

    def add_product(self, product):
        obj = File('user.json')
        userss = obj.read()
        for i in userss:
            if i['username'] == self.username:
                i["myproduct"].append(product)
        File('user.json').write(userss)

class Product:
    def __init__(self, name = None, count = None):
        self.name = name
        self.count = count

    def save_product(self):
        products = File('product.json').read()
        products.append(self.__dict__)
        File('product.json').write(products)

    def get_products(self):
        return File('product.json').read()


class Sum:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def my_product(self):
        product = File('products.json').read()
        new = []
        for i in product:
            if i['name'] == self.name and i['count'] == self.count:
                new.append({
                    'name': i['name'],
                    'count': i['count']
                })
            print('mahsulot harid qlidizngiz')
            new_ = File('products.json').read()
            new_.append(new)
            File('myproduct.json').write(new_)


def my_produkt(file):
    print(File(file).read())


def user_menu(data):
    product = """
    1.Products
    2.My products
    3. Log out
    >>>> """
    choise = input(product)
    if choise == '1':
        d = open('product.json','r')
        print(*d)

def UZUM_MARKET():
    print('Uzum market')
    text = """
    1.Login
    2.Registor
    >>>>"""
    choise = input(text)
    if choise == '2':
        fulname = input('Fullname : ')
        username = input('Username : ')
        password = int(input('Password : '))
        user = User(fulname, username, password)
        bool_ = user.check_user()
        if not bool_:
            user.save_user()
            print()
            UZUM_MARKET()
        else:
            print('bunday user ishlatilgan\n')
            UZUM_MARKET()
    elif choise == '1':
        username = input('username : ')
        password = input('password : ')
        data = User(username=username, password=password).check_login()
        if not data:
            user_menu(data)
        else:
            print('Sahifa topilmadi')
            UZUM_MARKET()


UZUM_MARKET()
