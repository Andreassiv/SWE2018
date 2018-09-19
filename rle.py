import sys

def rle_encoder(txt):
    """ RLE encoder modetager en streng og returner en streng
        med saa gentagne bogstaver bilver erstattet med bogstavet og
         antallet af gentagelser

         "bbbkkk" bliver "b3k3"
         """
    if not txt:
        return '' 
    c = txt[0]
    i = 1
    res = []
    for x in txt[1:]:
        if x == c:
            i += 1
        else:
            res.append('%c%d'%(c,i))
            c = x
            i = 1
    res.append('%c%d'%(c,i))
    return ''.join(res)


def rle_decoder(txt):
    """ Decoder en streng og returner en streng.
	input: "b3k3" output: "bbbkkk"
        """

    k = 0
    count = 1
    res = []

    for x in txt[1:]:
        k = k + 1
        count = 1
        if txt[k].isdigit():
            while  int(txt[k]) >= count:
                count = count + 1
                res.append(txt[k-1])


    return ''.join(res)
