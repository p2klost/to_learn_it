from sqlalchemy.orm import Session, Mapped
from sqlalchemy import select
from bd_engine import engine
from models import User, Order

session = Session(engine)

"""
Писал везде id: str т.к. именно string отдается функциям. Почитал - sqlalchemy сам переводит его в инт, в соответсвии с типом колонки таблицы
"""

def create_user(name: str,email: str) -> None:
    """1. Создать пользователя"""
    with session:
        user = User(name=name,email=email)
        session.add(user)
        session.commit()    

def show_users() -> None:
    """2. Показать пользователей"""
    with session:
        table = User
        statement = select(table)
        result = session.scalars(statement).all()
        if not result:
            print("В базе нет пользователей")
        else:
            print("Все пользователи")
            print(f"{"\t".join([i.name for i in table.__table__.columns])}")
            for user in result:
                print(f"{user.id}\t{user.name}\t{user.email}")

def create_order(user_id: int, product: str, status: str) -> None:
    """3. Создать заказ"""
    with session:
        if not session.get(User,user_id):
            print(f"Пользователь с id {user_id} не найден, заказ не создан")
        else:
            order = Order(user_id=user_id,product=product, status=status)
            session.add(order)
            session.commit()
            print("Заказ создан")

def show_orders() -> None:
    """4. Показать все заказы"""
    with session:
        table = Order
        statement = select(table)
        result = session.scalars(statement).all()
        if not result:
            print("В базе нет заказов")
        else:
            print("Все заказы")
            print(f"{"\t".join([i.name for i in table.__table__.columns])}")
            for order in result:
                print(f"{order.id}\t{order.user_id}\t{order.product}\t{order.status}")

def show_my_orders(email: str) -> None:
    """5. Показать мои заказы"""
    with session:
        statement = select(User).where(User.email == email)
        result = session.scalar(statement)
        if not result:
            print(f"Пользователя с почтой {email} нет в базе")
        else:
            col = Order.__table__.columns
            print("Все ваши заказы")
            print(f"{col[0].name}\t{col[2].name}\t{col[3].name}")
            for order in result.orders:
                print(f"{order.id}\t{order.product}\t{order.status}")

def show_order_status(id: int) -> None:
    """6. Показать статус заказа"""
    with session:
        print(get_order_by_id(id).status)

def update_order_status(id: int, new_status: str) -> None:
    """7. Изменить статус заказа"""
    with session:
        get_order_by_id(id).status = new_status
        session.commit()

def delete_order(id: int) -> None:
    """8. Удалить заказ"""
    with session:
        order = session.get(Order,id)
        session.delete(order)
        session.commit()

def find_order(product: str) -> None:
    """9. Найти заказ"""
    with session:
        table = Order
        col = table.__table__.columns
        order = session.scalar(select(table).where(table.product == product))
        if not order:
            print("Заказов не найдено")
        else:        
            print("Найденные заказы")
            print(f"{col[0].name}\t{col[1].name}\t{col[2].name}\t{col[3].name}")
            print(f"{order.id}\t{order.user_id}\t{order.product}\t{order.status}")

def get_order_by_id(id: int) -> Order | None:
    """Получить заказ по id"""
    return session.get(Order,id)
