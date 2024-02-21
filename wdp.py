import sys
import subprocess

data = []
with open(sys.argv[1]) as f:
	REG_BASE = int(f.readline().strip().split()[2], 16)

	for line in f:
		# Each line has up to 4 32-bit values prepended by the #cur_addr
		data.append(line.strip().split()[1:])

BUSYBOX_PATH = '/home/konrad/busybox/busybox'

for i in range(4 * (len(data) - 1) + len(data[-1])):
	val = "0x" + data[i // 4][i % 4]
	actval = subprocess.run([BUSYBOX_PATH, 'devmem', hex(REG_BASE + 4 * i)], stdout=subprocess.PIPE)
	actval = actval.stdout.decode('utf-8').strip().lower()
	print(f"{hex(REG_BASE + 4 * i)}: W={val} L={actval} {f'DIFF = {hex(int(val, 16) ^ int(actval, 16))}' if val != actval else ''}")
