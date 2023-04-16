# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    ###
    mode = input()
    if mode[0] == "F" :
        fname = "./tests/06"
        f = open(fname, "r")
        p = f.readline()
        t = f.readline()
        f.close()
        return (p.rstrip(), t.rstrip())

    if mode[0] == "I" :
        return (input().rstrip(), input().rstrip())
    ###
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    ###return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    ###
    def h(txt, p) :
        s = 0
        for c in txt :
            s += ord(c)
        return s % p
    
    result = []
    
    pl = len(pattern)
    tl = len(text)
    ph = h(pattern, pl)
    i = 0
    while i <= tl - pl :
        token = text[i : i + pl]
        if ph == h(token, pl) :
            if pattern == token :
                result.append(i)
            # equal = True
            # j = 0
            # while True :
            #     if pattern[j] != token[j] :
            #         equal = False
            #         break
            #     else :
            #         if j < pl-1 : j += 1
            #         else : break

        i += 1

    return result
    ###

    # and return an iterable variable
    #return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

