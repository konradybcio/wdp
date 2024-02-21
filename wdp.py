import sys

data = []
with open(sys.argv[1]) as f:
	REG_BASE = int(f.readline().strip().split()[2], 16)

	for line in f:
		# Each line has up to 4 32-bit values prepended by the #cur_addr
		data.append(line.strip().split()[1:])

for i in range(len(data)):
	print(f"{hex(REG_BASE + 4 * i)}: 0x{data[i // 4][i % 4]}")
