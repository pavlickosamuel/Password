password = input("Enter your password: ")

has_digit = False
has_lower = False
has_special = False

if len(password) >= 8:
    for znak in password:
        if znak.isdigit():
            has_digit = True
        elif znak.islower():
            has_lower = True
        elif znak.isascii() and not znak.isalnum() and ord(znak) > 32:
            has_special = True

    if not has_digit:
        print("Password must contain at least one digit.")
    elif not has_lower:
        print("Password must contain at least one lowercase letter.")
    elif not has_special:
        print("Password must contain at least one special character.")
    else:
        print("Password is valid.")
else:
    print("Password must be at least 8 characters long.")




