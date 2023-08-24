import datetime,requests,json

game_number = (datetime.date.today() - datetime.date(2022,1,8)).days
word = 'دیروز'  #just a rondom word for first guess
is_present = set()
correct_chars = dict()
with open('Persian_Words.txt' , 'r',encoding='utf-8') as f:
    words = [word[:-1] for word in f.readlines()]

url = f'https://www.vaajoor.com/api/check?word={word}&g={game_number}'
result = requests.get(url)
result = (json.loads(result.text)).get('match')

for i in range(5):
    if result[i] == 'y':
        is_present.add(word[i])

for i in range(5):
    if result[i] == 'g':
        correct_chars[i] = word[i]

print(is_present)
print(correct_chars)

for word in words:
    if all(char in word for char in is_present) and all(word[i] == correct_chars[i] for i in correct_chars.keys()):
        
        print(word)
        
        url = f'https://www.vaajoor.com/api/check?word={word}&g={game_number}'
        result = requests.get(url)
        result = (json.loads(result.text)).get('match')
        if result == ["g","g","g","g","g"]:break
            
        for i in range(5):
            if result[i] == 'y':
                is_present.add(word[i])
        for i in range(5):
            if result[i] == 'g':
                correct_chars[i] = word[i]
        
        print(is_present)
        print(correct_chars)
    

print(word[::-1])