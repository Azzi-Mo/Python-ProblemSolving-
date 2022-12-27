# print(convert(564987654)) # [4, 5, 6, 7, 8, 9, 4, 6, 5]
# print(convert(529132)) # [2, 3, 1, 9, 2, 5]

def convert(n):
 st = str(n)
 res = []
 for num in st:
      res.append(int(num))
 res.reverse()
 return res

print(convert(529132))