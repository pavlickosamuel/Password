password = input("Enter your password: ")
count_char = 0
count_digit = 0
count_spec_char = 0
if len(password) >= 8:
    for znak in password:
         if znak.isdigit():
              count_digit += 1
    if count_digit > 0:
        for znak in password:
             if not znak.isupper():
                  count_char += 1 
        if count_char > 0:
            for znak in password:
                if znak.isascii() and not(znak.isdigit()) and not(znak.isalpha()) and ord(znak) > 32:
                    count_spec_char += 1
            if count_spec_char > 0: 
                print("Password is valid.") 
            else: 
                print("Password must contain at least one special character.")         
        else:
           print("Password must contain at least one lowercase letter.")
    else:
        print("Password must contain at least one digit.")
else:
     print ("Password must be at least 8 characters long.")
