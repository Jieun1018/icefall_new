import json
import gzip
import sys

# 파일 읽기
#with open('input.txt', 'r', encoding='utf-8') as file:
#    data = file.readlines()

new_data = []

with gzip.open("/workspace/icefall_test/egs/speech_llm/ASR_LLM/data/fbank/librispeech_cuts_train-all-shuf_instruction.jsonl.gz","rt") as file:
    for line in file:
        record = json.loads(line.strip())
        recording = record.get("recording", {})
        transforms = recording.get("transforms", None)
        if transforms is None:
            new_data.append(record)


with open('no_perturb.txt', 'w', encoding='utf-8') as f:
    for record in new_data:
        f.write(json.dumps(record) + '\n')
