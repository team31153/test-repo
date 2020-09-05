s1 = int(input('Enter the first side value:'))
s2 = int(input('Enter the second side value:'))
def find_hypot(s1, s2):
    side1 = s1 * s1
    side2 = s2 * s2
    s3 = side1 + side2
    side3 = s3 ** 0.5
    print ("Hypotenuse value = " + str(side3))

find_hypot(s1, s2)