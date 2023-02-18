import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dq = deque()

for _ in range(N):
    cmd_in = input().split()
    if len(cmd_in) == 2:
        cmd_push, push_num = cmd_in
        if len(cmd_in) == 2:
            if cmd_push.endswith('back'):
                dq.append(push_num)
            else:
                dq.appendleft(push_num)
    else:
        cmd = cmd_in[0]
        if cmd.startswith('pop'):
            if cmd.endswith('back'):
                print(dq.pop() if len(dq) else -1)
            else:
                print(dq.popleft() if len(dq) else -1)
        elif cmd == 'size':
            print(len(dq))
        elif cmd == 'empty':
            if len(dq):
                print(0)
            else:
                print(1)
        elif cmd == 'front':
            if len(dq):
                print(dq[0])
            else:
                print(-1)
        elif cmd == 'back':
            if len(dq):
                print(dq[-1])
            else:
                print(-1)