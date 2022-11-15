# no pandas

with open('input.csv') as f:
  input_from_file = f.read()

lines = input_from_file.split('\n')

headers = lines[0].split(',')

data = []

for line in lines[1:]:
  processed_line = [int(x) for x in line.split(',')]
  data.append(processed_line)

def average(t):
  total = 0
  for x in t:
    total += x
  result = total / len(t)
  return result

for row in data:
  row.append(average(row))

output = ','.join(headers) + '\n'

for row in data:
  processed_row = [str(x) for x in row]
  output += ','.join(processed_row) + '\n'

with open('output.txt', 'w') as f:
  f.write(output)