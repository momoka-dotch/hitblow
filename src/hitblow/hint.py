import random


def hint(secret):
    """秘密の数字から1桁だけ位置付きで教える"""
    index = random.randrange(len(secret))
    return f"ヒント：{index + 1}桁目は {secret[index]} です！"