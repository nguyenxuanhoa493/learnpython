import os
import csv
PATH_ITEM_CSV = os.path.dirname(__file__)+'/data/item.csv'
os.system('cls||clear')
temp=["","",""]
temp[0] = input('Mời nhập mã sản phẩm: ')
temp[1] = input('Mời nhập tên sản phẩm: ')
temp[2] = input('Mời nhập giá bán (Ngàn/Kg): ')
with open(PATH_ITEM_CSV, 'a',encoding="UTF8") as file:
        writer = csv.writer(file)
        writer.writerow(temp)  