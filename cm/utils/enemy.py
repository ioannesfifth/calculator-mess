# Based on Masanori Max WL

def res_multiplier(res_shred):
    res = 0.1 - res_shred
    if res < 0:
        return 1 - (res / 2)
    elif res > 0.75:
        return 1/(4 * res + 1)
    else:
        return 1 - res

def def_multiplier():
    return (90 + 100)/((190)+(195))