"""
Разработайте систему отправки уведомлений 
пользователям. 
1.  Создайте общий базовый интерфейс для уведомлений. 
Отправка сообщения должна выполняться через 
единый метод. 
2.  Реализуйте отдельные классы для:  
○  Email; 
○  SMS; 
○  Push. 
3.  Каждый способ отправки должен иметь собственное 
поведение.  
4.  Создайте функцию, которая получает список 
уведомлений и отправляет через них одно сообщение. 
  Функция должна работать с разными типами 
уведомлений через полиморфизм, без проверки 
конкретного класса объекта.  
5.  Добавьте возможность создавать уведомление 
альтернативным способом из конфигурации, например 
из словаря с настройками получателя. 
6.  Добавьте статический метод для проверки 
корректности данных получателя. 
7.  Создайте собственную иерархию исключений для 
ошибок системы уведомлений. Предусмотрите как 
минимум: 
○  некорректного получателя; 
○  ошибку отправки уведомления. 
8.  Реализуйте __str__(), чтобы объекты уведомлений 
имели понятное строковое представление.
"""

from re import fullmatch

class NotificationError(Exception):
    pass

class RecipientNotificationError(NotificationError):
    pass

class SendNotificationError(NotificationError):
    pass

class Notification:

    def send(self, message: str, recipient: str) -> None:
        
        print(f"Получатель: {recipient}.\nСодержание: {message}")

    @classmethod
    def create_from_dict(cls,get_dict: dict) -> object:
          t_class = globals()[f"{get_dict["type"]}Notification"]
          return t_class(get_dict["recipient"])

class EmailNotification(Notification):

    def __init__(self, recipient) -> None:
        self.recipient = recipient

    def send(self, message: str) -> str:     
        if message is None:
            raise SendNotificationError("Ошибка. Некорректное содержание письма.")
        if self.valid_recipient(self.recipient):
            print(f"[Email] Новое письмо ")
            super().send(message, self.recipient)

    @staticmethod
    def valid_recipient(recipient) -> str:
        if fullmatch(r"\S+\@\S+\.\S+",recipient) is None:
          raise RecipientNotificationError("Некорректный email получателя.")
        else:
          return recipient

    def __str__(self) -> str:
        return f"Получатель уведомления: {self.recipient}"

class SMSNotification(Notification):

    def __init__(self, recipient) -> None:
        self.recipient = recipient

    def send(self, message: str) -> str:
        if message is None:
            raise SendNotificationError("Ошибка. Некорректное содержание сообщения.")
        if self.valid_recipient(self.recipient):
            print(f"[SMS] Новое сообщение")
            super().send(message, self.recipient)

    @staticmethod
    def valid_recipient(recipient) -> str:
        if fullmatch(r"\+375(29|33|44|25)\d{7}",recipient.replace("-","").replace(" ","").replace("(","").replace(")","")) is None:
          raise RecipientNotificationError("Некорректный номер получателя.")
        else:
          return recipient

    def __str__(self) -> str:
        return f"Получатель уведомления: {self.recipient}"
        
class PushNotification(Notification):

    def __init__(self, recipient) -> None:
        self.recipient = recipient

    def send(self, message: str) -> str:
        if message is None:
            raise SendNotificationError("Ошибка. Некорректное содержание уведомления.")
        if self.valid_recipient(self.recipient):
            print(f"[Push] Новое уведомление")
            super().send(message, self.recipient)

    @staticmethod
    def valid_recipient(recipient) -> str:
        if fullmatch(r"\w+[a-zA-Zа-яА-Я]",recipient) is None:
          raise RecipientNotificationError("Некорректный получатель.")
        else:
          return recipient

    def __str__(self) -> str:
        return f"Получатель уведомления: {self.recipient}"


def send_message(push: list, message: str) -> None:
      for i in push:
        i.send(message)

notif1 = EmailNotification("Pavel@gmail.com")
notif2 = SMSNotification("+375295341286")
notif3 = PushNotification("Павел")

dict_notif = \
{   "type": "Email",
    "recipient": "vt43ghb.v@gmail.com"}

push_to = [notif1,notif2,notif3,Notification.create_from_dict(dict_notif)]


# print(notif1)
# send_message(push_to,"Приглашаем вас посетить наше мероприятие.")
# send_message(push_to,None) # как пример ошибки SendNotificationError