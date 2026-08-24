"""
Небольшое задание именно на наследование и 
переопределение методов. Создайте базовый класс: 
Notification. У него должен быть метод: send(message). 
Затем создайте: 
●  EmailNotification; 
●  SMSNotification; 
●  PushNotification. 
 
Каждый класс должен по-своему реализовать send(). 
Проверить в цикле. 
 
Дополнительное усложнение: добавить в Notification общий 
атрибут recipient и использовать super().__init__() в дочерних 
классах. 
"""

class Notification:

    def __init__(self, recipient) -> None:
        self._recipient = recipient

    def send(self, message: str) -> str:
        pass

class EmailNotification(Notification):

    def __init__(self, recipient) -> None:
        super().__init__(recipient)

    def send(self, message: str) -> str:    
        print(f"[Email] Письмо отправлено следующему получателю: {self._recipient}.\n Содержание: {message}")
    
class SMSNotification(Notification):

    def __init__(self, recipient) -> None:
        super().__init__(recipient)

    def send(self, message: str) -> str:
        print(f"[SMS] Сообщение отправлено следующему получателю: {self._recipient}.\n Содержание: {message}")

class PushNotification(Notification):

    def __init__(self, recipient) -> None:
        super().__init__(recipient)

    def send(self, message: str) -> str:
        print(f"[Push] Уведомление отправлено следующему получателю: {self._recipient}.\n Содержание: {message}")

not1 = EmailNotification("Pavel")
not2 = SMSNotification("Maksim")
not3 = PushNotification("Nikita")

for i in [not1,not2,not3]:
    i.send("Привет, ты выиграл автомобиль.")