txtfull = ''
while True:
    txt = input()
    txtfull += txt + ' '
    if txt == '':
        break
lsttxtfull = txtfull.split(' ')
wlsttxtfull = []

for word in lsttxtfull:
        wlsttxtfull.append(word.strip('.,?!:;').lower())

reslst = []

for word in wlsttxtfull:
    if word not in reslst:
        reslst.append(word)

freq = []

for word in reslst:
    freq.append(wlsttxtfull.count(word))

freq.sort(reverse=True)
words = []

for c in freq:
    for word in reslst:
        if (wlsttxtfull.count(word) == c) and (words.count(word) == 0):
            words.append(word)

for w in words:
    if len(w) != 0:
        print(w)
