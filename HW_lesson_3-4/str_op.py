s = "У лукоморья 123 дуб зеленый 456"

if s.find('я') != -1:
    print(s.find('я'))
    
print((s.lower()).count('у'))

if not s.isalpha():
    print(s.upper())
    
if len(s) >= 4:
    print(s.lower())
    
s = 'О' + s[1:]
print(s)
