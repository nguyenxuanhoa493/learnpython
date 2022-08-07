import csv
import os

class Goods:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
    
def read_item():
    with open(PATH_ITEM_CSV, newline='\n') as f:
        list1 = csv.reader(f)
        list1 = list(list1)
        header=list1.pop(0)
        list2=[]
        for i in list1:
            temp= Goods(i[0],i[1],i[2])
            list2.append(temp)
        return list2

def show_menu(list):
    os.system('cls||clear')
    print_all_list(list)
    print_menu(list)


def print_menu(list):
    while True:
        print("|{:<47}{:<51}|".format(" ","MENU"))
        print("-"*LINE)
        print("|{:<27} | {:<44} | {:<21}|".format("1. Thêm sản phẩm","2. Sửa sản phẩm","3. Xoá sản phẩm"))
        print("-"*LINE) 
        action = input('Mời chọn chức năng: ')
        if action =='1':
            add_item()
            show_menu(read_item())
        elif action =='2':
            index_edit = int(input("Mời nhập STT sản phẩm cần sửa: "))-1
            list[index_edit].code = input("Mã sản phẩm : {:<20} ->: ".format(list[index_edit].code))
            list[index_edit].name = input("Tên sản phẩm : {:<20} ->: ".format(list[index_edit].name))
            list[index_edit].price = input("Giá sản phẩm : {:<20} ->: ".format(list[index_edit].price))
            save_to_file(list)
            show_menu(read_item())
        elif action =='3':
            index_del =  int(input("Mời nhập STT sản phẩm cần xoá: "))-1
            item_del=list.pop(index_del)
            save_to_file(list)
            show_menu(read_item())
        else:
            show_menu(list)
            continue

def add_item():
    temp=["","",""]
    temp[0] = input('Mời nhập mã sản phẩm: ')
    temp[1] = input('Mời nhập tên sản phẩm: ')
    temp[2] = input('Mời nhập giá bán (Ngàn/Kg): ')
    with open(PATH_ITEM_CSV, 'a',encoding="UTF8") as file:
        writer = csv.writer(file)
        writer.writerow(temp)     

def save_to_file(list):
    headers=["code","name","price"]
    list1=[]
    for i in list:
        temp = [i.code,i.name,i.price]
        list1.append(temp)
    with open(PATH_ITEM_CSV, 'w',encoding="UTF8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(list1)   

def print_all_list(list):
    print("-"*LINE)
    print("|{:<39}{:<59}|".format(" ","DANH SÁCH HÀNG HOÁ"))
    print("-"*LINE)
    print("| STT | {:<20} | {:<44} | {:<12}(Ngàn/kg)|".format("Mã sản phẩm","Tên sản phẩm","Giá bán"))
    print("-"*LINE)
    for i in range(len(list)):
        print("| {:<3} | {:<20} | {:<44} | {:<21}|".format(i+1,list[i].code,list[i].name,list[i].price))
        print("-"*LINE)

LINE=100
PATH_ITEM_CSV = os.path.dirname(__file__)+'/data/item.csv'
def main():
        show_menu(read_item())      
main()        