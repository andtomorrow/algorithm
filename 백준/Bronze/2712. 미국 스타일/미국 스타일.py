from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    input_num, input_unit = stdin.readline().split()
    input_num = float(input_num)
    match input_unit:
        case "kg":
            output_num = round(input_num * 2.2046, 4)
            output_unit = "lb"
        case "lb":
            output_num = round(input_num * 0.4536, 4)
            output_unit = "kg"
        case "l":
            output_num = round(input_num * 0.2642, 4)
            output_unit = "g"
        case "g":
            output_num = round(input_num * 3.7854, 4)
            output_unit = "l"
    print(f"{output_num:.4f}", output_unit)
