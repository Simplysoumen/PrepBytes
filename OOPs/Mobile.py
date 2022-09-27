class Mobile:
    def __init__(self, brandName, color, isJack):
        self.brandName = brandName
        self.color = color
        self.isJack = isJack

    def calling(self):
        print("Calling")

    def cameraClick(self):
        print("Picture is clicking")

    def message(self):
        print("Message sent")


def main():
    m1 = Mobile("Apple", "White", False)
    print(m1.brandName)
    print(m1.color)
    print(m1.isJack)
    m1.calling()
    m1.cameraClick()
    m1.message()
    print("----------------------")
    m2 = Mobile("Samsung", "Black", True)
    print(m2.brandName)
    print(m2.color)
    print(m2.isJack)
    m2.calling()
    m2.cameraClick()
    m2.message()

 if __name__ =='__main__':
        main()
