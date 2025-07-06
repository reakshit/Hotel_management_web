def kryptos(message):
    list1 = ['K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z',\
    'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K',\
    'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R',\
    'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y',\
    'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P',\
    'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T',\
    'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O',\
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S',\
    'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A',\
    'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B',\
    'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C',\
    'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D',\
    'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E',\
    'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F',\
    'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G',\
    'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',\
    'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',\
    'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',\
    'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L',\
    'N', 'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M',\
    'Q', 'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N',\
    'U', 'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q',\
    'V', 'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U',\
    'W', 'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V',\
    'X', 'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W',\
    'Z', 'K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X']

    ref = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    imp2 = "hotel"
    
    encr = ''
    fcr=""
    l1 = ['1', ':', '|', '^', '|', 'B', '$', '4', '!', '.', '5', '?', '+', '<', 'T', 'E', '{', 'C', '5', '=', '_', '!', ',', 'L', 'R', '=']

    if len(imp2) != len(message):
        if len(imp2) < len(message):
            repetitions = (len(message) // len(imp2)) + 1
            imp2 = imp2 * repetitions
        else:
            imp2 = imp2[:len(message)]

    message_no_spaces = "".join(message.split())  

    limp2 = list(imp2)
    lmess = list(message_no_spaces)

    new_message = []
    ctr = 0
    while len(new_message) < len(message_no_spaces):
        new_message.append(limp2[ctr % len(limp2)])
        ctr += 1


    for i in range(len(lmess)):
        x= lmess[i]
        y=new_message[i]
        ix= list1.index(x.upper())
        iy = list1.index(y.upper())
        ecry = list1[(26*iy)+ix]
        encr+=ecry
   
    for i in range(len(encr)):
        a=ref.index(encr[i])
        fcr+= l1[a]

    return fcr