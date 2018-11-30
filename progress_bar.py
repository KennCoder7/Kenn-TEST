import time
EACH_STEP_COST_TIME = 0.3
PROCESS_TOTAL_STEP = 30

# print("Flowing light:")
# for i in range(LENGTH):
#     bar = ['['] + ['o'] * LENGTH + [']']
#     bar[i + 1] = '*'
#     bar_show = ''.join(bar)
#     print('\r{}'.format(bar_show), end='')
#     time.sleep(FRESH_TIME)


def process_bar(current_state, total_state, bar_length=20):
    bar = ['['] + ['-'] * bar_length + [']']
    current_bar = int(current_state/total_state*bar_length)
    for j in range(current_bar+1):
        bar[j+1] = '#'
    bar_show = ''.join(bar)
    print('\r{}%d%%'.format(bar_show) % ((current_state+1)/total_state*100), end='')
    if current_state == total_state-1:
        bar = ['['] + ['#'] * bar_length + [']']
        bar_show = ''.join(bar)
        print('\r{}%d%%'.format(bar_show) % 100, end='')
        print('\r')


print("Progress start:")
for step in range(PROCESS_TOTAL_STEP):
    process_bar(step, PROCESS_TOTAL_STEP)
    time.sleep(EACH_STEP_COST_TIME)
print("Process finished.")
