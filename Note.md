## 笔记文档

### 文件夹结构

```shell
.
├── 480
├── 720
├── 1080(现在的手机一般都是2K屏,竖屏就是1440左右)
│  ├── land(横屏用)
│  ├── port(竖屏用)
│  │  ├── en_26.ini(英语26键小写)
│  │  ├── en_26s.ini(英语26键大写)
│  │  ├── gen.ini(offset坐标文件)
│  │  └── res
│  │     └── default.css(显示用字符定义文件)
│  └── res
│     ├── btn.png
│     ├── btn.til
│     └── sym_num.til
├── demo.png(预览图)
└── Info.txt(信息文档)
```

### 主要说明

```ini
[KEY16]
BACK_STYLE=118(背景css的id)
FORE_STYLE=45,38,39(前景css的id)
POS_TYPE=0,11,63(前景css偏置的id,数量上需要和fore_style的个数相同,如果不同则默认为offset0)
VIEW_RECT=545,183,94,130(视觉位置)
TOUCH_RECT=546,185,108,155(触摸位置)
UP=- (向上滑发向内核的信号字符)
LEFT=e
RIGHT=e
DOWN=_
CENTER=e
```

大部分的css的内容是直接绘制字体,比如style45, style38等

而少部分的css内容是图片,可以从 `*.til` 和`*.png`文件中找到线索

```ini
[STYLE118]
NM_IMG=btn,1
HL_IMG=btn,4

[STYLE45]
SHOW=e
NM_COLOR=ffffff
HL_COLOR=ffffff
FONT_SIZE=64
BORDER_COLOR=00FFFFFF
BORDER_SIZE=2

[STYLE38]
SHOW=-
NM_COLOR=7a7a7a
HL_COLOR=7a7a7a
FONT_SIZE=40
BORDER_COLOR=00FFFFFF
BORDER_SIZE=1

[STYLE39]
SHOW=_
NM_COLOR=7a7a7a
HL_COLOR=7a7a7a
FONT_SIZE=40
BORDER_COLOR=00FFFFFF
BORDER_SIZE=1
```

偏置文件主要设置一个css样式,相对于矩形的中心有怎样的偏置.

默认offset0表示中心位置

此处的offset9则表示相对于中心向上一些(字符上方符号)的位置

```ini
[OFFSET9]
POS=0,-40

[OFFSET63]
POS=0,40
```

### 功能键

只摘录一些常用的

| 代号 | 含义                                                     |
| :--- | -------------------------------------------------------- |
| F1   | 切换到符号                                               |
| F6   | 切换到数字                                               |
| F10  | 小写切换到大写                                           |
| F11  | 大写切换到固定大写或小写                                 |
| F15  | 切换到中文输入                                           |
| F16  | 切换到英文输入                                           |
| F36  | Del                                                      |
| F37  | BackSpace                                                |
| F38  | 空格                                                     |
| F39  | 回车                                                     |
| F40  | 清除输入的字符(专指中文输入状态下输入却还没有上屏的拼音) |
| F41  | Tab                                                      |
| F42  | Home                                                     |
| F43  | End                                                      |
| F49  | 上                                                       |
| F50  | 下                                                       |
| F51  | 左                                                       |
| F52  | 右                                                       |

