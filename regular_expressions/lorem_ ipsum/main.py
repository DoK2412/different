import re

text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""
# регулярное вырадение
regular = r'\b[a-z]\w{3}\b'
# фильтрация текста по регулярке
final_list = re.findall(regular, text)
# вывод результата
print(final_list)
