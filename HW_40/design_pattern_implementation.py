from abc import ABC, abstractmethod

"""Design pattern: Factory Method"""


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email with message: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS with message: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"Sending push notification with message: {message}")


class EmailNotificationCreator(NotificationCreator):
    def create_notification(self):
        return EmailNotification()


class SMSNotificationCreator(NotificationCreator):
    def create_notification(self):
        return SMSNotification()


class PushNotificationCreator(NotificationCreator):
    def create_notification(self):
        return PushNotification()


def client_code(creator: NotificationCreator, message):
    notification = creator.create_notification()
    notification.send(message)


message = "You're breathtaking."

client_code(EmailNotificationCreator(), message)
client_code(SMSNotificationCreator(), message)
client_code(PushNotificationCreator(), message)
