import os

class video:
  def __init__(self,name,id):
    self.name = name
    self.id = id
    self.link = "http//youtube.com/v="+id
    self.comment = []

  def rename(self,new_name):
    self.name=new_name
  
  def update_id(self, new_id):
    self.id = new_id
    self.link = "http//youtube.com/v="+new_id

  def add_comment(self,comment):
    self.comment.append(comment)

  def remove_comment(self,id_comment):
    self.comment.remove(self.comment[id_comment-1])
  
  def clear_comment(self):
    self.comment=[]

  def print_info(self):
    print('-'*49)
    print('| Name: {:<40}|'.format(self.name))
    print('| ID: {:<42}|'.format(self.id))
    print('| Link: {:<40}|'.format(self.link))
    for i in range(len(self.comment)):
      print('| Bình luận {:<3}: {:<31}|'.format(i+1,self.comment[i]))
    print('-'*49)

def show_menu(vd):
  os.system('cls||clear')
  vd.print_info()
  print_menu(vd)

def print_menu(vb):
  while True:
    print("1. Đổi tên video")
    print("2. Thêm bình luận")
    print("3. Xoá bình luận")
    print("4. Xoá tất cả bình luận")
    print("5. Cập nhật ID")
    action = input('Mời chọn chức năng:')

    if action =='1':
      new_name = input('Mời nhập tên mới: ')
      vb.rename(new_name)
      show_menu(vb)
    elif action =='2':
      cmt = input('Mời nhập bình luận: ')
      vb.add_comment(cmt)
      show_menu(vb)
    elif action =='3':
      index_comment = int(input('Bạn muốn xoá bình luận thứ mấy: '))
      print(index_comment)
      vb.remove_comment(index_comment)
      show_menu(vb)
    elif action =='4':
      vb.clear_comment()
      show_menu(vb)
    elif action =='5':
      new_id = input('Mời nhập ID mới: ')
      vb.update_id(new_id)
      show_menu(vb)
    else:
      show_menu(vb)
      continue
    
def main():
  vd =video("Học python","uhwe765")
  show_menu(vd)
main()