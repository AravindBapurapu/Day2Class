import time
Enter = input("Enter a String:").strip()
if Enter == Enter[::-1]:
    print(f"{Enter} is a Palindrome")
else:
    print(f"{Enter} is not a Palindrome")