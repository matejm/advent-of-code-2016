import re
from collections import defaultdict

class Bot:
    def __init__(self, ID):
        self.low = -1
        self.high = -1
        self.id = ID
        self.next_low = -1
        self.next_high = -1

    def add(self, chip):
        if self.low == -1:
            self.low = chip
        else:
            self.high = max(chip, self.low)
            self.low = min(chip, self.low)

    def full(self):
        return self.high != -1 and self.low != -1

    def give(self):
        low = self.low
        high = self.high
        self.low = -1
        self.high = -1
        return low, high

    def __repr__(self):
        return 'Bot[{}]: ({}, {}) -> ({}, {})'.format(self.id, self.low, self.high, self.next_low, self.next_high)


commands = []
while True:
    try: line = input()
    except: break
    if not line: break
    commands.append(line)

bots = [Bot(i) for i in range(500)]
outputs = defaultdict(int)

for c in commands:
    m1 = re.findall(r'value ([0-9]+) goes to bot ([0-9]+)', c)
    m2 = re.findall(r'bot ([0-9]+) gives low to bot ([0-9]+) and high to bot ([0-9]+)', c)
    m3 = re.findall(r'bot ([0-9]+) gives low to output ([0-9]+) and high to bot ([0-9]+)', c)
    m4 = re.findall(r'bot ([0-9]+) gives low to bot ([0-9]+) and high to output ([0-9]+)', c)
    m5 = re.findall(r'bot ([0-9]+) gives low to output ([0-9]+) and high to output ([0-9]+)', c)
    if m1:
        value, bot = (int(i) for i in m1[0])
        bots[bot].add(value)
    elif m2:
        bot, bot_low, bot_high = (int(i) for i in m2[0])
        bots[bot].next_low = bot_low
        bots[bot].next_high = bot_high
    elif m3:
        bot, out_low, bot_high = (int(i) for i in m3[0])
        bots[bot].next_low = out_low+1000
        bots[bot].next_high = bot_high
    elif m4:
        bot, bot_low, out_high = (int(i) for i in m4[0])
        bots[bot].next_low = bot_low
        bots[bot].next_high = out_high+1000
    elif m5:
        bot, out_low, out_high = (int(i) for i in m5[0])
        bots[bot].next_low = out_low+1000
        bots[bot].next_high = out_high+1000

while True:
    finished = True
    for bot in bots:
        if bot.full():
            finished = False
            low, high = bot.give()
            if low == 17 and high == 61:
                print('#1', bot.id)
            out_low, out_high = bot.next_low, bot.next_high
            if out_low >= 1000:
                outputs[out_low-1000] = low
            else:
                bots[out_low].add(low)
            if out_high >= 1000:
                outputs[out_high-1000] = high
            else:
                bots[out_high].add(high)
    if finished:
        break

print('#2', outputs[0] * outputs[1] * outputs[2])
