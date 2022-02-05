import sys

inf = sys.maxsize

pitchers = list(map(int, input().split(',')))
target = int(input())


def heruistic(state, target):
    h = 0
    diff = abs(target - state[-1][0])
    for c in reversed(sorted(pitchers)):
        h += diff // c
        diff = diff % c
    if diff > 0:
        h += 2
    return h


def get_next_state(p):
    for i, pi in enumerate(p):
        for j, pj in enumerate(p):
            if (i != j) and (pj[1] > pj[0]) and pi[0] > 0:
                p_new = list(p)
                p_new[i] = (max([pi[0] + pj[0] - pj[1], 0]), pi[1])
                p_new[j] = (min([pi[0] + pj[0], pj[1]]), pj[1])
                yield tuple(p_new)


def print_path(came_from, state):
    if came_from[state] != -1:
        print_path(came_from, came_from[state])
    print(state)


def A_star(pitchers, target):
    state = tuple([(inf, inf)] + [(0, capacity) for capacity in pitchers] + [(0, inf)])
    f_score = {}
    g_score = {}
    h_score = {}
    came_from = {state: -1}

    h_score[state] = heruistic(state, target)
    g_score[state] = 0
    f_score[state] = h_score[state] + g_score[state]

    closedSet = set()
    openSet = set()
    openSet.add((f_score[state], h_score[state], state))
    while len(openSet) > 0:
        _, _, cur = min(openSet)
        openSet.remove(min(openSet))
        # print(cur, "g=", g_score[cur], "h=", h_score[cur], "f=", f_score[cur])
        if cur[-1][0] == target:
            # print_path(came_from, cur)
            return g_score[cur]
            break
        closedSet.add(cur)
        for next_state in get_next_state(cur):
            if not next_state in closedSet:
                g_tentative = g_score[cur] + 1
                if g_tentative < g_score.get(next_state, inf):
                    openSet.discard((f_score.get(next_state), h_score.get(next_state), next_state))
                    g_score[next_state] = g_tentative
                    h_score[next_state] = heruistic(next_state, target)
                    f_score[next_state] = g_score[next_state] + h_score[next_state]
                    came_from[next_state] = cur
                    openSet.add((f_score[next_state], h_score[next_state], next_state))


if __name__ == '__main__':
    A_star(pitchers, target)
