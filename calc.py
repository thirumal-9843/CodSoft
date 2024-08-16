class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def power(self, x, y):
        return x ** y

    def remainder(self, x, y):
        return x % y

    def display_menu(self):
        print("Select Operation")
        print("1.Add      --> + ")
        print("2.Subtract --> - ")
        print("3.Multiply --> * ")
        print("4.Divide   --> / ")
        print("5.Power    --> ^ ")
        print("6.Remainder--> % ")
        print("7.Reset    --> $ ")
        print("8.Terminate--> # ")

    def execute(self):
        while True:
            self.display_menu()
            choice = input("Enter Choice : ")
            if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
                if choice == '7':
                    continue
                if choice == '8':
                    break
                num1 = int(input("Enter First Number = "))
                num2 = int(input("Enter second Number = "))

                if choice == '1':
                    print(num1, "+", num2, "=", self.add(num1, num2))
                elif choice == '2':
                    print(num1, "-", num2, "=", self.subtract(num1, num2))
                elif choice == '3':
                    print(num1, "*", num2, "=", self.multiply(num1, num2))
                elif choice == '4':
                    print(num1, "/", num2, "=", self.divide(num1, num2))
                elif choice == '5':
                    print(num1, "^", num2, "=", self.power(num1, num2))
                elif choice == '6':
                    print(num1, "%", num2, "=", self.remainder(num1, num2))
            else:
                print("-----------------------------Invalid Input------------------------------")

calc = Calculator()
calc.execute()
