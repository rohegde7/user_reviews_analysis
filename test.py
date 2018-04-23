import re
string1 = "4-98 20/20 results269 should get"

list_usb_speed_numbers = list(map(str, re.findall(r'(\d+)', str(string1))))


x = 'abcd4'
print(x.lower)
