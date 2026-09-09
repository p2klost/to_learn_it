from crud import *

def execute(input_num: int) -> None:
    try:
        if input_num == 1:
            in_par = input("Введите данные (имя, почта):").split(", ")
            create_user(in_par[0],in_par[1])
            print("Пользователь создан")
        elif input_num == 2:
            show_users()
        elif input_num == 3:
            in_par = input("Введите данные (id пользователя, продукт, статус):").split(", ")
            create_order(in_par[0],in_par[1],in_par[2])
            print("Пользователь создан")
        elif input_num == 4:
            show_orders()
        elif input_num == 5:
            in_par = input("Введите вашу почту:")
            show_my_orders(in_par)
        elif input_num == 6:
            in_par = input("Введите id заказа:")
            show_order_status(in_par[0])
        elif input_num == 7:
            in_par = input("Введите данные (id заказа, новый статус):").split(", ")
            update_order_status(in_par[0],in_par[1])
            print(f"Статус заказа с id {in_par[0]} обновлен")
        elif input_num == 8:
            in_par = input("Введите данные id заказа:")
            delete_order(in_par[0])
            print(f"Заказ с id {in_par[0]} удален")
        elif input_num == 9:
            in_par = input("Введите название товара:")
            find_order(in_par)
    except Exception:
        print("Произошла ошибка, попробуйте еще раз") 
        # понимаю, что стоило бы сделать проверку на различные ошибки при вводе, но в данном случае
        # представим, что пользователь вводит всё правильно (как задумано)

def main() -> None:
    while True:
        print(
        """
        1. Создать пользователя  
        2. Показать пользователей  
        3. Создать заказ
        4. Показать все заказы
        5. Показать мои заказы  
        6. Показать статус заказа
        7. Изменить статус заказа
        8. Удалить заказ
        9. Найти заказ 
        0. Выход 
        """
        )
        input_num = int(input("Выберите действие: "))
        if input_num == 0:
            break
        if input_num not in range(1,10):
            print("Такого действия нет, введите другую цифру.")
        else:
            execute(input_num)


if __name__ == "__main__":
    main()