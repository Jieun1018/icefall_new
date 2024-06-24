import json
import random

def insert_random_space(text):
    if not text:
        return text
    index = random.randint(0, len(text))
    return text[:index] + ' ' + text[index:]

with open('input.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

count = 0
new_data = []
for line in data:
    if random.random() < 0.1:
        count += 1
        record = json.loads(line.strip())
        supervisions = record.get("supervisions", [])
        for supervision in supervisions:
            text = supervision.get("text", "")
            modified_text = insert_random_space(text)
            supervision["text"] = modified_text
        new_data.append(record)
    else:
        record = json.loads(line.strip())
        new_data.append(record)

print(count)

with open('input_fin.txt', 'w', encoding='utf-8') as file:
    for record in new_data:
        file.write(json.dumps(record) + '\n')

