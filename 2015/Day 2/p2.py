def surfaceArea(l: int, w: int, h: int):
  return 2 * l * w + 2 * w * h + 2 * h * l

def wrappingPaper(l: int, w: int, h: int):
    sa = surfaceArea(l, w, h)
    extra = min(l * w, l * h, w * h)
    return sa + extra

def totalSqFeet()