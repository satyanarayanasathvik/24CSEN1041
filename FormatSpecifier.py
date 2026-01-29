a = 15

print(f"Octal representation: {oct(a)}")
print(f"Octal representation: {a:o}")
print(f"{a:*<6o}")   # left aligned
print(f"{a:*>6o}")   # right aligned
print(f"{a:*^6o}")   # centered

#OUTPUT
Octal representation: 0o17
Octal representation: 17
17****
****17
**17**
