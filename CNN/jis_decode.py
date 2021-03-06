dict_decode_jisx0201 = {
    '0xa6': 'ヲ',
    '0xa7': 'ァ',
    '0xa8': 'ィ',
    '0xa9': 'ゥ',
    '0xaa': 'ェ',
    '0xab': 'ォ',
    '0xac': 'ャ',
    '0xad': 'ョ',
    '0xae': 'ッ',
    '0xaf': 'ァ',
    '0xb0': 'ー',
    '0xb1': 'ア',
    '0xb2': 'イ',
    '0xb3': 'ウ',
    '0xb4': 'エ',
    '0xb5': 'オ',
    '0xb6': 'カ',
    '0xb7': 'キ',
    '0xb8': 'ク',
    '0xb9': 'ケ',
    '0xba': 'コ',
    '0xbb': 'サ',
    '0xbc': 'シ',
    '0xbd': 'ス',
    '0xbe': 'セ',
    '0xbf': 'ソ',
    '0xc0': 'タ',
    '0xc1': 'チ',
    '0xc2': 'ツ',
    '0xc3': 'テ',
    '0xc4': 'ト',
    '0xc5': 'ナ',
    '0xc6': 'ニ',
    '0xc7': 'ヌ',
    '0xc8': 'ネ',
    '0xc9': 'ノ',
    '0xca': 'ハ',
    '0xcb': 'ヒ',
    '0xcc': 'フ',
    '0xcd': 'ヘ',
    '0xce': 'ホ',
    '0xcf': 'マ',
    '0xd0': 'ミ',
    '0xd1': 'ム',
    '0xd2': 'メ',
    '0xd3': 'モ',
    '0xd4': 'ヤ',
    '0xd5': 'ユ',
    '0xd6': 'ヨ',
    '0xd7': 'ラ',
    '0xd8': 'リ',
    '0xd9': 'ル',
    '0xda': 'レ',
    '0xdb': 'ロ',
    '0xdc': 'ワ',
    '0xdd': 'ン',
    '0xde': '゛',
    '0xdf': '゜'
}

def decode_jisx0201(dec):
    return dict_decode_jisx0201[hex(dec)]

def decode_jisx0208(dec):
    b = b'\033$B'+bytes.fromhex(hex(dec)[2:])
    return b.decode('iso2022_jp')