## Hi there 👋

Everyday Challenge: Making sense of nonsense, one weird pattern at a time.

![Image Alt](https://github.com/MaatherData/MaatherData/blob/dd33180b02dc2408e16b3f42722b0ad59b0e475d/IMG-20250413-WA0042.jpg)


Solution:

🧠 Computational Thinking
Read the input (space-separated candle heights)

Find the maximum height (tallest candle)

Count how many candles have that height

Return the count



💻 coding

candles = list(map(int, input().split()))

max_height = max(candles)

count = candles.count(max_height)

print(count)


