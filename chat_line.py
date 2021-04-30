def read_file(file):
	chat = []

	with open(file, 'r', encoding='utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat

def convert(chat):
	persion = None
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in chat:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen說了', allen_word_count, '個字') 
	print('allen傳了', allen_sticker_count, '個貼圖')
	print('allen傳了', allen_image_count, '張圖片')
	print('viki說了', viki_word_count, '個字')
	print('viki傳了', viki_sticker_count, '個貼圖')
	print('viki傳了', viki_image_count, '張圖片')

def write_file(file, chat):
	with open(file, 'w') as f:
		for line in chat:
			f.write(line + '\n')

def main():
	chat = read_file('LINE-Viki.txt')
	chat = convert(chat)
	# write_file('output.txt', chat)
main()