from typing import List


def tri(datas: any, item: str) -> List[list]:
  names = list(datas['Joueur'])
  numbers = list(datas[item])
  n = len(names)
  for i in range(n-1):
    for j in range(n-1):
      if numbers[j] < numbers[j+1]:
        temp_name = names[j+1]
        temp_number = numbers[j+1]
        names[j+1] = names[j]
        numbers[j+1] = numbers[j]
        names[j] = temp_name
        numbers[j] = temp_number
  return [[names[i], numbers[i]] for i in range(n)]