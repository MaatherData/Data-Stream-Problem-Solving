 Hi there 👋

Everyday Challenge: Making sense of nonsense, one weird pattern at a time.

Welcome to the madness — this beast of a repo is about to unload every single detail living inside it. Code? Explained. Logic? Exposed. Sanity? Long gone.

![Image Alt](https://github.com/MaatherData/MaatherData/blob/dd33180b02dc2408e16b3f42722b0ad59b0e475d/IMG-20250413-WA0042.jpg)


Solution:

🧠 Computational Thinking
Read the input (space-separated candle heights)

Find the maximum height (tallest candle)

Count how many candles have that height

Return the count



💻 coding

input_text = input("Enter candle heights (space separated): ")


candle_heights = input_text.split()
numbers = []
i = 0
while i < len(candle_heights):
    numbers.append(int(candle_heights[i]))
    i = i + 1


tallest = numbers[0]  # start with the first number
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


