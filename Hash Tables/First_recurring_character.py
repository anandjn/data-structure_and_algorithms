
'''
//Google Question
//Given an array = [2,5,1,2,3,5,1,2,4]:
//It should return 2

//Given an array = [2,1,1,2,3,5,1,2,4]:
//It should return 1

//Given an array = [2,3,4,5]:
//It should return None

//Bonus... What if we had this:
// [2,5,5,2,3,5,1,2,4]
// return 5 because the pairs are before 2,2

      TASK                  Time-complexity
find recurring character        O(n)
'''
#using hash tables/ Dictionary
def firstRecurringCharacter(input):
  myHash = {}
  for number in input:
    #if key of that number exist its recurring number
    if number in myHash:
      return number
    #else put this number in our table
    else:
      myHash[number] = True
  return None



x = firstRecurringCharacter([2,5,1,2,3,5,1,2,4])
y = firstRecurringCharacter([2,1,1,2,3,5,1,2,4])
z = firstRecurringCharacter([2,3,4,5])

b= firstRecurringCharacter([2,5,5,2,3,5,1,2,4])

print(x)
print(y)
print(z)
print(b)
