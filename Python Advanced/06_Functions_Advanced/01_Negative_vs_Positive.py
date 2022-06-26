numbers = [int(x) for x in input().split()]

positives = [x for x in numbers if x > 0]
negatives = [x for x in numbers if x < 0]

print(sum(negatives))
print(sum(positives))
if abs(sum(negatives)) > abs(sum(positives)):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
