class jioCaller():
    def call(self):
        print ("Calling")

class trueCaller():
    def call(self):
        print("Ringing")
        print("Caller data")

class Phone:
    def callFunc(self, phoneApp):
        phoneApp.call()

phoneApp = jioCaller()
p1 = Phone()
p1.callFunc(phoneApp)
