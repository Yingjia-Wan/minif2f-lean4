import json

def extract_formal_statements(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            data = json.loads(line)
            formal_statement = data.get("formal_statement", "")
            if formal_statement:
                outfile.write(formal_statement + '\n\n')

input_file = 'minif2f/test.jsonl'
output_file = 'formal_statements.lean'

extract_formal_statements(input_file, output_file)
print(f'Formal statements have been written to {output_file}')
