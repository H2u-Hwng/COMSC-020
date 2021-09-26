# Huu Hung Nguyen
# 09/25/2021
# Nguyen_HuuHung_57Exercises.py
# Do 19.

# 19
# https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
s = []
for n in range(101):
    ele = ((4 / (n * 8 + 1)) - (2 / (n * 8 + 4)) -
         (1 / (n * 8 + 5)) - (1 / (n * 8 + 6)))
    s.append(ele / (16**n))

print(f"Approx. using Bailey–Borwein–Plouffe formula: {sum(s)}.")
print(f"Using math.pi: {math.pi}.")