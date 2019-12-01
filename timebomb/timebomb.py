import sys
def take(arr):
    digit = [arr[r][0:3] for r in range(len(arr))]
    return digit, [arr[r][4:] for r in range(len(arr))]

def parse():
    valids = [list(l) for l in ["***   * *** *** * * *** *** *** *** ***",
        "* *   *   *   * * * *   *     * * * * *",
        "* *   * *** *** *** *** ***   * *** ***",
        "* *   * *     *   *   * * *   * * *   *",
        "***   * *** ***   * *** ***   * *** ***"]]

    digits = []
    for i in range(10):
        d, valids = take(valids)
        digits.append(d)
    return digits

lines = [list(input()) for i in range(5)]
valids = parse()
s = ""
while len(lines[0]) > 0:
    digit, lines = take(lines)
    match = next((i for i in range(len(valids)) if valids[i] == digit), None)
    if match is None:
        print("BOOM!!")
        sys.exit(0)
    else:
        s = s + str(match)

if int(s) % 6 == 0:
    print("BEER!!")
else:
    print("BOOM!!")

    



    
        

