import csv
from importlib.metadata import packages_distributions
import os
from turtle import goto

class Goods:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
class Customer:
    def __init__(self, phone, name, adress ):
        self.phone = phone
        self.name = name
        self.adress = adress

class List_Goods:
    def __init__(self):
        self.list=[]
        self.db = os.path.dirname(__file__)+'/data/item.csv'
        self.headers=["code","name","price"]
    
    def read_db(self):
        with open(self.db, newline='\n') as f:
            list_temp = csv.reader(f)
            temp = list(list_temp)
            header=temp.pop(0)
            for i in temp:
                item = Goods(i[0],i[1],i[2])
                self.list.append(item)

    def add_item(self,item):
        self.list.append(item)
        self.save()

    def print_list(self):
        os.system('cls||clear')
        print("-"*LINE)
        print("|{:<39}{:<59}|".format(" ","DANH SÁCH HÀNG HOÁ"))
        print("-"*LINE)
        print("| STT | {:<20} | {:<44} | {:<12}(Ngàn/kg)|".format("Mã sản phẩm","Tên sản phẩm","Giá bán"))
        print("-"*LINE)
        for i in range(len(self.list)):
            print("| {:<3} | {:<20} | {:<44} | {:<21}|".format(i+1,self.list[i].code,self.list[i].name,self.list[i].price))
            print("-"*LINE)
        self.print_menu()
        
    def print_menu(self):
        while True:
            print("|{:<47}{:<51}|".format(" ","MENU"))
            print("-"*LINE)
            print("|{:<27} | {:<30} | {:<21} | {:<10}|".format("1. Thêm sản phẩm","2. Sửa sản phẩm","3. Xoá sản phẩm","4. Quay lại"))
            print("-"*LINE) 
            action = input('Mời chọn chức năng: ')
            if action =='1':
                temp=["","",""]
                temp[0] = input('Mời nhập mã sản phẩm: ')
                temp[1] = input('Mời nhập tên sản phẩm: ')
                temp[2] = input('Mời nhập giá bán (Ngàn/Kg): ')
                self.add_item(Goods(temp[0],temp[1],temp[2]))
                self.print_list()

            elif action =='2':
                index_edit = int(input("Mời nhập STT sản phẩm cần sửa: "))-1
                self.list[index_edit].code = input("Mã sản phẩm : {:<21} ->: ".format(self.list[index_edit].code))
                self.list[index_edit].name = input("Tên sản phẩm : {:<20} ->: ".format(self.list[index_edit].name))
                self.list[index_edit].price = input("Giá sản phẩm : {:<20} ->: ".format(self.list[index_edit].price))
                self.save()
                self.print_list()

            elif action =='3':
                index_del =  int(input("Mời nhập STT sản phẩm cần xoá: "))-1
                item_del=self.list.pop(index_del)
                self.save()
                self.print_list()
            elif action=='4':
                main()

            else:
                self.print_list()
                continue
    
    def save(self):
        list1=[]
        for i in self.list:
            temp = [i.code,i.name,i.price]
            list1.append(temp)
        with open(self.db, 'w',encoding="UTF8") as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
                writer.writerows(list1) 

class List_customer:
    def __init__(self):
        self.list=[]
        self.db = os.path.dirname(__file__)+'/data/customer.csv'
        self.headers=["phone","name","adress"]
    
    def read_db(self):
        with open(self.db, newline='\n') as f:
            list_temp = csv.reader(f)
            temp = list(list_temp)
            header=temp.pop(0)
            for i in temp:
                item = Customer(i[0],i[1],i[2])
                self.list.append(item)

    def add_item(self,item):
        self.list.append(item)
        self.save()

    def print_list(self):
        os.system('cls||clear')
        print("-"*LINE)
        print("|{:<39}{:<59}|".format(" ","DANH SÁCH KHÁCH HÀNG"))
        print("-"*LINE)
        print("| STT | {:<21} | {:<32} | {:<31} |".format("Số điện thoại","Họ và tên","Địa chỉ"))
        print("-"*LINE)
        for i in range(len(self.list)):
            print("| {:<3} | {:<21} | {:<32} | {:<32}|".format(i+1,self.list[i].phone,self.list[i].name,self.list[i].adress))
            print("-"*LINE)
        self.print_menu()
        
    def print_menu(self):
        while True:
            print("|{:<47}{:<51}|".format(" ","MENU"))
            print("-"*LINE)
            print("|{:<27} | {:<30} | {:<21} | {:<10} |".format("1. Thêm khách hàng","2. Sửa thông tin","3. Xoá khách hàng","4.Quay lại"))
            print("-"*LINE) 
            action = input('Mời chọn chức năng: ')
            if action =='1':
                temp=["","",""]
                temp[0] = input('Mời nhập số điên thoại: ')
                temp[1] = input('Mời nhập tên khách hàng: ')
                temp[2] = input('Mời nhập địa chỉ: ')
                self.add_item(Customer(temp[0],temp[1],temp[2]))
                self.print_list()

            elif action =='2':
                index_edit = int(input("Mời nhập STT khách hàng cần sửa: "))-1
                self.list[index_edit].phone = input("Số điện thoại : {:<20} ->: ".format(self.list[index_edit].phone))
                self.list[index_edit].name = input("Họ và tên : {:<20} ->: ".format(self.list[index_edit].name))
                self.list[index_edit].adress = input("Địa chỉ : {:<20} ->: ".format(self.list[index_edit].adress))
                self.save()
                self.print_list()

            elif action =='3':
                index_del =  int(input("Mời nhập STT khách hàng cần xoá: "))-1
                item_del=self.list.pop(index_del)
                self.save()
                self.print_list()
            elif action=='4':
                main()

            else:
                self.print_list()
                continue
    
    def save(self):
        list1=[]
        for i in self.list:
            temp = [i.phone,i.name,i.adress]
            list1.append(temp)
        with open(self.db, 'w',encoding="UTF8") as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
                writer.writerows(list1) 

def main():
    os.system('cls||clear')
    while True:
        print('1.Quản lý hàng hoá                       2. Quản lý khách hàng')
        action = input('Mời chọn menu: ')
        if action=='1':
            items.print_list()
        elif action == '2':
            customers.print_list()
        else:
            continue

LINE=100
items =List_Goods()
items.read_db()
customers = List_customer()
customers.read_db()
# list_item.del_item(1)
main()
