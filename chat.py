def read_file(file):
	chat = []

	with open(file, 'r', encoding='utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat

def convert(chat):
	new = []
	persion = None
	for line in chat:
		if line == 'Allen':
			person = line
			continue
		elif line == 'Tom':
			person = line
			continue
		if person:    #如果有值
			new.append(person + ': ' + line)
	return new

def write_file(file, chat):
	with open(file, 'w') as f:
		for line in chat:
			f.write(line + '\n')

def main():
	chat = read_file('input.txt')
	chat = convert(chat)
	write_file('output.txt', chat)
main()