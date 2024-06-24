import sys
import gzip
import json
import random

def insert_random_upper_character(text):
    if not text:
        return text
    index = random.randint(0, len(text))
    random_char = chr(random.randint(65, 90))  # a-z 중에서 임의의 철자 선택
    return text[:index] + random_char + text[index:]

count = 0
new_data = []
with open("no_perturb.txt", "r", encoding='utf-8') as file:
    for line in file:
        if random.random() < 0.1:
            line = line.strip()
            #print(line."supervisions")
            count += 1
            record = json.loads(line.strip())
            supervisions = record.get("supervisions", [])
            for supervision in supervisions:
                text = supervision.get("text", "")
                modified_text = insert_random_upper_character(text)
                supervision["text"] = modified_text
            new_data.append(record)
    #print(new_data)
    #exit()
        else:
            record = json.loads(line.strip())
            new_data.append(record)

#with open('input.txt', 'w', encoding='utf-8') as f:
    #f.writelines(file)


#exit()
'''
with gzip.open('/workspace/icefall_test/egs/speech_llm/ASR_LLM/data/fbank/librispeech_cuts_train-all-shuf_instruction_test.txt', 'w') as file:
    for record in new_data:
        #print(record)
        #print(type(record))
        #exit()
        json.dump(record, file)
        file.write('\n')
'''
with open('input.txt', 'w', encoding='utf-8') as file:
    for record in new_data:
        file.write(json.dumps(record) + '\n')

print(count)
