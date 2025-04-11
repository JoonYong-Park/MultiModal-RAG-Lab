import os
import json
import pandas as pd

MODEL_FOLDER = 'qasper_gpt_4o_limit_20'
INPUT_FOLDER = f'evaluation/data/{MODEL_FOLDER}'
OUTPUT_FOLDER = f'evaluation/output/{MODEL_FOLDER}'

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file_name in os.listdir(INPUT_FOLDER):
    if file_name.endswith('.jsonl') or file_name.endswith('.json'):
        input_path = os.path.join(INPUT_FOLDER, file_name)
        output_path = os.path.join(
            OUTPUT_FOLDER,
            file_name.replace('.jsonl', '.xlsx').replace('.json', '.xlsx')
        )

        if os.path.exists(output_path):
            print(f"[⏭] 이미 존재하여 건너뜀: {output_path}")
            continue

        data = []
        with open(input_path, 'r', encoding='utf-8-sig') as file:
            if file_name.endswith('.jsonl'):
                for line in file:
                    data.append(json.loads(line.strip()))
            elif file_name.endswith('.json'):
                data = json.load(file)
                if isinstance(data, dict):
                    data = [data]

        df = pd.DataFrame(data)
        df.to_excel(output_path, index=False)

        print(f"[✔] {file_name} → {output_path}")
