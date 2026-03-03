num = float(input("Enter a decimal number: "))
base = int(input("Enter the target base (2-16): "))

# Handle sign
is_negative = num < 0
num = abs(num)


integer_part = int(num)
fractional_part = num - integer_part


chars = "0123456789ABCDEF"

# --- 1. Convert Integer Part ---
res_int_list = []
temp_int = integer_part

if temp_int == 0:
    res_int_list.append("0")
else:
    while temp_int > 0:
        remainder = temp_int % base
        res_int_list.append(chars[remainder])
        temp_int //= base
    res_int_list.reverse()



res_frac_list = []
temp_frac = fractional_part
precision = 10


while temp_frac > 0 and len(res_frac_list) < precision:
    temp_frac *= base
    digit = int(temp_frac)
    res_frac_list.append(chars[digit])
    temp_frac -= digit



final_result = "".join(res_int_list)



if res_frac_list:
    final_result += "." + "".join(res_frac_list)


if is_negative:
    final_result = "-" + final_result

print("Result:", final_result)


"""
Output
Enter a decimal number: -4576
Enter the target base (2-16): 5
Result: -121301
"""
