def isCode(cmd) :
    for s in cmd :
        #print(s)
        if(s != '0' and s != '1') :
            return 0
    return 1    

def decode(cmd) :
    print("decoding")
    w = ''
    dots = ''
    for c in cmd :
        w += c
        if len(w) == 9 :
            dots += w 
            dots += '.'
            w = '' 
    #print(dots)
    res = dots.split('.')
    #print(res)
    asciis = []
    for i in res :
        if i != '' :
            asciis.append(int(str(i) , 2))
    #print(asciis)   

    key = asciis[0] - ord('r')
    msg = ''
    for i in asciis :
        #print(chr(int(i) - key)) 
        msg += chr(int(i) - key)
    print(msg[14:])

def code(cmd) :
    print("coding...")
    const = "rick and morty"
    cmd = const + cmd 
    key = len(cmd)
    extraKey = -1 
    while extraKey < 0 :
        extraKey = int(input("enter (+) extra key : "))
    key += int(extraKey) 
    #print(key)
    asciis = []
    #print(cmd)
    for alpha in cmd :
        #print(ord(alpha))
        asciis.append(ord(alpha) + key % 20)

    #print(asciis)
    binary = []
    res = ''
    for i in asciis :
        #print(format(i , 'b'))
        #
        #print(len(str(format(i , 'b'))))
        nominal = (9 - len(str(format(i , 'b')))) * '0' + format(i , 'b')
        #
        binary.append(nominal)
        #print(len(nominal))
        #print(nominal)
        res += nominal

    #print(binary)
    print(res)


#isCode("azer")

while 1 :
    cmd = input(">")
    if(isCode(cmd)) :
        decode(cmd) 
    else :
        code(cmd)    