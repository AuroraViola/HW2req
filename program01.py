def decode_XKCD_tuple(xkcd_values : tuple[str, ...], k : int) -> list[int]:
    midlist = []
    for i in range(len(xkcd_values)):
        midlist.append(decode_value(xkcd_values[i]))

    midlist.sort(reverse=True)

    while len(midlist) > k:
        midlist.pop(k)

    return midlist

    #finallist = []
    #for i in range(k):
        #finallist.append(midlist[i])

    #return finallist


def decode_value(xkcd : str ) -> int:
    return list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))


def xkcd_to_list_of_weights(xkcd : str) -> list[int]:
    newlist = []
    exp = 0
    for i in reversed(range(len(xkcd))):
        if xkcd[i] != "0":
            newlist.append(int(xkcd[i]) * 10**exp)
            if exp != 0:
                exp = 0
        else:
            exp += 1
    return newlist[::-1]


def list_of_weights_to_number(weigths : list[int] ) -> int:
    lenlist = len(weigths)-1
    num = weigths[lenlist]
    for i in reversed(range(lenlist)):
        if weigths[i] >= weigths[i+1]:
            num += weigths[i]
        else:
            num -= weigths[i]
    return num



###################################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test
    a = 1
