class poly:
    def _init_(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
a= int(input("a="))
b= int(input("b="))
c= int(input("c="))

class triangle(poly):
    def _init_(self,a,b,c):
        super()._init_(a,b,c)

    def get_area(self):
        s = (a + b + c) / 2
        return (s*(s-a)(s-b)(s-c)) **
        #question (4b)
def filterlongword(string,number):

    for i in range(len(string)):
        listwords = []
        if len(string[i]) > number:
            listwords.append(string[i])

        return listwords 


def main():
    words = input("Please input the list of words: ")
    integer = eval(input("Please input an integer: "))

    words1 = filterlongword(words,integer)

    print("The list of words greater than the integer is",words1)

main()