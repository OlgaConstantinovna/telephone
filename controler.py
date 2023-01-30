import view
import model_menu

def start():
    view.creat_menu()

def select():
    view.imput_number()
    number = int(input())  
    model_menu.select(number)  