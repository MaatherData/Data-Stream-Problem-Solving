
input_text = input("Enter candle heights (space separated): ")

candle_heights = input_text.split()
numbers = []
i = 0
while i < len(candle_heights):
    numbers.append(int(candle_heights[i]))
    i = i + 1

tallest = numbers[0]  
i = 1
while i < len(numbers):
    if numbers[i] > tallest:
        tallest = numbers[i]
    i = i + 1

count = 0
i = 0
while i < len(numbers):
    if numbers[i] == tallest:
        count = count + 1
    i = i + 1

print(count)



