import random
from .core import judge


def bot_guess(digits, history, difficulty=1):
    if difficulty == 1:
        return _random_guess(digits, [g for g, _, _ in history])
    if difficulty == 2:
        return _smart_guess(digits, history, noise=0.5)
    return _smart_guess(digits, history, noise=0.0)

def _random_guess(digits, used_guesses):
    while True:
        guess = "".join(random.sample("0123456789", digits))
        if guess not in used_guesses:
            return guess


def _all_candidates(digits):
    return [
        "".join(p) for p in _permutations("0123456789", digits)
    ]


def _smart_guess(digits, history, noise=0.0):
    candidates = _all_candidates(digits)
    for guess, hit, blow in history:
        candidates = [
            c for c in candidates
            if judge(c, guess) == (hit, blow)
        ]
    if not candidates:
        return _random_guess(digits, [g for g, _, _ in history])
    if random.random() < noise:
        return random.choice(candidates)
    return candidates[0]


def _permutations(pool, r):
    if r == 0:
        yield ()
        return
    for i, p in enumerate(pool):
        rest = pool[:i] + pool[i + 1:]
        for tail in _permutations(rest, r - 1):
            yield (p,) + tail