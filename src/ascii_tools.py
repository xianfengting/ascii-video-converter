# -*- coding:utf-8 -*-

ascii_char = list("MNHQ$OC67)oa+>!:+. ")

# 将像素转换为ascii码
def get_char_by_ARGB(r, g, b, alpha = 256):
  if alpha == 0:
    return ''
  length = len(ascii_char)
  gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
  unit = (256.0+1)/length
  return ascii_char[int(gray/unit)]
