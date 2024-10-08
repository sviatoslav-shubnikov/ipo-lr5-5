string = input("Введите строку для нахождения слова 'Python': ")

python_word = "Python"

count = 0
words = string.split()

for word in words:
    
    if word == python_word:
        count += 1
        
print(f"Количество нахождений слова 'Python': {count}")