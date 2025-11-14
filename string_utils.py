def split_before_each_uppercases(formula):
    split_formula = []
    
    if not formula:
      return split_formula
    start = 0
    end = 1
    for i in formula [1:]:
      if i.isupper():
        split_part = formula[start:end]
        split_formula.append(split_part)
        start = end
      end +=1
    split_formula.append(formula[start:end])
    return split_formula

def split_at_first_digit(formula):
  digit_location = 1
  for i in formula [1:]:
    if not i.isdigit():
      digit_location += 1
    elif i.isdigit ():
      break
  if digit_location == len(formula):
    return (formula , 1)
  else:
    new_formula_1 = formula[:digit_location]
    new_formula_2 = formula[digit_location:]
    return (new_formula_1 , int(new_formula_2))
