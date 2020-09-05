s1 = int(input('Enter the first side value: '))
s2 = int(input('Enter the second side value: '))
s3 = int(input('Enter the hypotenuse value: '))
def check_right(s1, s2, s3):
    side1 = s1 * s1
    side2 = s2 * s2
    side3 = s3 * s3
    if side3 == side1 + side2:
        print("True")
    else:
        print("False")


check_right(s1, s2, s3)