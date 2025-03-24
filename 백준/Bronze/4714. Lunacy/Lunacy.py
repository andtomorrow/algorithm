from sys import stdin

while True:
    input_weight = float(stdin.readline())

    if input_weight < 0:
        break

    weight_on_moon = input_weight * 0.167

    print(
        f"Objects weighing {input_weight:.2f} on Earth will weigh {weight_on_moon:.2f} on the moon.")
