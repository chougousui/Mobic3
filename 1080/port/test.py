import configparser
import matplotlib.pyplot as plt


def render_key(ax, section):
    touch_rect = section['TOUCH_RECT']
    a, b, c, d = map(int, touch_rect.split(','))
    rect_t = plt.Rectangle((a + 5, b + 5),
                           c - 10,
                           d - 10,
                           edgecolor='red',
                           fill=False)
    ax.add_patch(rect_t)

    view_rect = section['VIEW_RECT']
    x, y, w, h = map(int, view_rect.split(','))
    rect = plt.Rectangle((x, y), w, h)
    ax.add_patch(rect)

    ax.text(x, y, section.name)
    ax.text(x + w / 2, y + h / 2, section['CENTER'])
    if 'UP' in section:
        ax.text(x + w / 2, y + 20, section['UP'])
    if 'DOWN' in section:
        ax.text(x + w / 2, y + h - 20, section['DOWN'])


def exchange_letter(sec_a, sec_b):
    sec_a['LEFT'], sec_b['LEFT'] = sec_b['LEFT'], sec_a['LEFT']
    sec_a['RIGHT'], sec_b['RIGHT'] = sec_b['RIGHT'], sec_a['RIGHT']
    sec_a['CENTER'], sec_b['CENTER'] = sec_b['CENTER'], sec_a['CENTER']
    seca = sec_a['FORE_STYLE'].split(',')
    secb = sec_b['FORE_STYLE'].split(',')
    seca[0], secb[0] = secb[0], seca[0]
    sec_a['FORE_STYLE'] = ','.join(seca)
    sec_b['FORE_STYLE'] = ','.join(secb)


def exchange_symbol(sec_a, sec_b):
    sec_a['UP'], sec_b['UP'] = sec_b['UP'], sec_a['UP']
    letter_a, symbol_a = map(int, sec_a['FORE_STYLE'].split(','))
    letter_b, symbol_b = map(int, sec_b['FORE_STYLE'].split(','))
    sec_a['FORE_STYLE'] = f'{letter_a},{symbol_b}'
    sec_b['FORE_STYLE'] = f'{letter_b},{symbol_a}'


# read file
config = configparser.ConfigParser()
config.optionxform = str
config.read('en_26.ini')

# figure
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.axis([0, 1080, 0, 600])
ax1.xaxis.set_ticks_position('top')
ax1.invert_yaxis()
ax2.axis([0, 1080, 0, 600])
ax2.xaxis.set_ticks_position('top')
ax2.invert_yaxis()

for idx in range(1, 37):
    key_name = f'KEY{idx}'
    render_key(ax1, config[key_name])

letter_pairs = [(36, 1), (36, 2), (36, 12), (36, 23), (36, 22), (36, 8),
                (36, 7), (36, 13), (36, 4), (36, 24), (36, 9), (36, 18),
                (36, 21), (36, 11), (36, 15), (36, 25), (36, 17), (36, 3),
                (36, 16), (36, 6), (36, 19), (36, 14)]
for a, b in letter_pairs:
    exchange_letter(config[f'KEY{a}'], config[f'KEY{b}'])

# symbol_pairs = [(16, 22), (19, 36), (18, 19), (18, 21)]
# for a, b in symbol_pairs:
#     exchange_symbol(config[f'KEY{a}'], config[f'KEY{b}'])

for idx in range(1, 37):
    key_name = f'KEY{idx}'
    render_key(ax2, config[key_name])

plt.show()

with open('new.ini', 'w') as configfile:
    config.write(configfile, space_around_delimiters=False)
