def perim(l, w):
    ans = (2 * l) + (2 * w)
    return ans

print("give me the lwngth.")
lwngth = float(input("> "))
print("give me the width.")
width = float(input("> "))
perimeter = perim(lwngth, width)
print(f"the perimeter of this shape is {perim}.")