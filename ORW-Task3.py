inputText = []
for file in ['1.txt', '2.txt', '3.txt']:
    with open(file, 'r') as f:
        inputText.extend(f.readlines()+['\n'])
with open('4.txt', 'w') as output:
    for line in inputText:
        output.write(line)