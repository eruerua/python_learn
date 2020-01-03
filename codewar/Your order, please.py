def order(sentence):
  # code here
  if sentence:
    new_l=sorted(sentence.split(' '),key=lambda x:int(list(filter(str.isdigit,x))[0]))
    return ' '.join(new_l)
  else:
      return sentence

print(order("is2 Thi1s T4est 3a"))