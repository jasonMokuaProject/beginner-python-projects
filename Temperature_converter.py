def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


c = 24
f = 67


print(f"{c}°C = {celsius_to_fahrenheit(c):.1f}°F")

print(f"{f}°F = {fahrenheit_to_celsius(f):.1f}°C ")