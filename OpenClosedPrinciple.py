class Notification:
    def sendNotification(self):
        pass


class MobileNotification(Notification):
    def sendNotification(self):
        print("Mobile Notification Sent")


class EmailNotification(Notification):
    def sendNotification(self):
        print("Email Notification Sent")