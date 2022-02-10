import sys
import heapq
import functools
from math import ceil, gcd

inf = sys.maxsize


def heuristic(state, target, pitchers):
    diff = ceil(abs(target - state[-1][0]) * 2 // max(pitchers))
    return diff


def get_next_state(state):
    for i, pitchers_i in enumerate(state):
        for j, pitchers_j in enumerate(state):
            if (i != j) and (pitchers_j[1] > pitchers_j[0]) and pitchers_i[0] > 0:
                next_state = list(state)
                next_state[i] = (max([pitchers_i[0] + pitchers_j[0] - pitchers_j[1], 0]), pitchers_i[1])
                next_state[j] = (min([pitchers_i[0] + pitchers_j[0], pitchers_j[1]]), pitchers_j[1])
                yield tuple(next_state)


def print_path(came_from, state, f_score, g_score, h_score):
    if came_from[state] != -1:
        print_path(came_from, came_from[state], f_score, g_score, h_score)
    print(state, "g=", g_score[state], "h=", h_score[state], "f=", f_score[state])


def A_star(pitchers, target):
    if target % functools.reduce(gcd, pitchers) != 0:
        return -1
    state = tuple([(inf, inf)] + [(0, capacity) for capacity in pitchers] + [(0, inf)])
    f_score = {}
    g_score = {}
    h_score = {}
    came_from = {state: -1}
    h_score[state] = heuristic(state, target, pitchers)
    g_score[state] = 0
    f_score[state] = h_score[state] + g_score[state]
    closed_set = set()
    open_set = []
    heapq.heapify(open_set)
    heapq.heappush(open_set, (f_score[state], h_score[state], state))
    state_no = 0
    while len(open_set) > 0:
        _, _, cur = heapq.heappop(open_set)
        print(cur, "g=", g_score[cur], "h=", h_score[cur], "f=", f_score[cur])
        if cur[-1][0] == target:
            print('Number of states evaluated: ', state_no)
            print("__________________________________________________________________________________")
            print_path(came_from, cur, f_score, g_score, h_score)
            return g_score[cur]
        closed_set.add(cur)
        for next_state in get_next_state(cur):
            if not next_state in closed_set:
                g_tentative = g_score[cur] + 1
                if g_tentative < g_score.get(next_state, inf):
                    try:
                        idx = open_set.index((f_score.get(next_state), h_score.get(next_state), next_state))
                        open_set[idx] = open_set[-1]
                        open_set.pop()
                        heapq.heapify(open_set)
                    except:
                        pass
                    g_score[next_state] = g_tentative
                    h_score[next_state] = heuristic(next_state, target, pitchers)
                    f_score[next_state] = g_score[next_state] + h_score[next_state]
                    came_from[next_state] = cur
                    heapq.heappush(open_set, (f_score[next_state], h_score[next_state], next_state))
        state_no = state_no + 1


if __name__ == '__main__':
    file = open("input.txt", "r")
    pitchers = list(map(int, file.readline().split(',')))
    target = int(file.readline())
    file.close()
    print(A_star(pitchers, target))
