import random


def hint(secret, used_indices):
    """秘密の数字から、まだ教えてない桁を1つ選んで位置付きで教える"""
    remaining = [i for i in range(len(secret)) if i not in used_indices]
    if not remaining:
        return "もうヒントは出せません（全部教えました）"
    index = random.choice(remaining)
    used_indices.add(index)
    return f"ヒント：{index + 1}桁目は {secret[index]} です！"