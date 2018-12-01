import time
import sys
FRESH_TIME = 0.3
LENGTH = 7

mod = 5
if mod == 1:
    print("Flowing light:")
    while mod == 1:
        for i in range(LENGTH):
            bar = ['['] + [' '] * LENGTH + [']']
            bar[i + 1] = '*'
            bar_show = ''.join(bar)
            print('\r{}'.format(bar_show), end='')
            time.sleep(FRESH_TIME)
elif mod == 2:
    print("Accumulated flowing light:")
    while mod == 2:
        for j in range(LENGTH):
            for i in range(LENGTH - j):
                bar = ['['] + [' '] * (LENGTH - j) + ['*'] * j + [']']
                bar[i + 1] = '*'
                bar_show = ''.join(bar)
                print('\r{}'.format(bar_show), end='')
                time.sleep(FRESH_TIME)
        time.sleep(FRESH_TIME)
elif mod == 3:
    print("Round flowing light:")
    while mod == 3:
        for j in range(2):
            for i in range(LENGTH):
                bar = ['['] + [' '] * LENGTH + [']']
                if j == 0:
                    bar[i + 1] = '*'
                else:
                    bar[-(i + 2)] = '*'
                bar_show = ''.join(bar)
                print('\r{}'.format(bar_show), end='')
                time.sleep(FRESH_TIME)
elif mod == 4:
    print("Flowing word light:")
    word = "I LOVE U"
    while mod == 4:
        bar = ['['] + ['*'] * len(word) + [']']
        bar_show = ''.join(bar)
        print('\r{}'.format(bar_show), end='')
        time.sleep(FRESH_TIME)
        for i in range(len(word)):
            bar[i + 1] = word[i]
            bar_show = ''.join(bar)
            print('\r{}'.format(bar_show), end='')
            time.sleep(FRESH_TIME)
elif mod == 5:
    print("Process bar:")
    while mod == 5:
        for i in range(LENGTH):
            bar = ['['] + [' '] * LENGTH + [']']
            for j in range(i + 1):
                bar[j + 1] = '*'
            bar_show = ''.join(bar)
            print('\r{}'.format(bar_show), end='')
            time.sleep(FRESH_TIME)
else:
    sys.exit(0)
