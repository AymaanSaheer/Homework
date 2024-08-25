base = int(input("Enter the base of the object: "))
height = int(input("Enter the height of the object: "))

def areaOfTriangle():
    area = 0.5 * base * height
    print(f"The Area of Triangle is {area}")

def areaOfParallelogram():
    area = base * height
    print(f"The Area of Parallelogram is {area}")
areaOfParallelogram()
areaOfTriangle()
