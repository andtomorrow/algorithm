from sys import stdin

for _ in range(3):
    # time_in, time_out = stdin.readline().split()[
    #     0:3], stdin.readline().split()[3:]

    input_line = stdin.readline().split()
    time_in, time_out = input_line[:3], input_line[3:]

    int_time_in = list(map(int, time_in))
    int_time_out = list(map(int, time_out))

    sec_time_in = int_time_in[0] * 60 * 60 + \
        int_time_in[1] * 60 + int_time_in[2]

    sec_time_out = int_time_out[0] * 60 * 60 + \
        int_time_out[1] * 60 + int_time_out[2]

    sec_duration = sec_time_out - sec_time_in

    duration_h, duration_m = divmod(sec_duration, 3600)
    duration_m, duration_s = divmod(duration_m, 60)

    print(duration_h, duration_m, duration_s)
