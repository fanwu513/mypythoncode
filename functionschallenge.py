def max_number(num1, num2, num3):
    return max(num1, max(num2, num3))


def sum_numbers():
    numbers = [8, 2, 3, 0, 7]
    return sum(numbers)


def multiply_numbers(nums):
    product = 1
    for num in nums:
        product = product * num
    return product


def is_even(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


def main():
    num1 = input("Enter first number\n")
    num2 = input("Enter second number\n")
    num3 = input("Enter third number\n")
    print("Max number is: ", max_number(num1, num2, num3))
    print("Sum of numbers is: ", sum_numbers())
    print("Product of list is: ", multiply_numbers((8, 2, 3, -1, 7)))
    print("Even numbers of list are: ", is_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))

main()
