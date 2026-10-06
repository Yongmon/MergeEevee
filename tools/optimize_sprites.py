#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRUIT_DIR = os.path.join(ROOT, "assets", "fruits")

ASSET_FILL = 0.92
MAX_SIZE = 512
MIN_SIZE = 72

# ==========================
# 伊布九个等级半径（与 game.js 保持一致）
# ==========================
RADII = [
    17,  # 伊布
    23,  # 水伊布
    31,  # 火伊布
    39,  # 雷伊布
    48,  # 太阳伊布
    58,  # 月亮伊布
    69,  # 叶伊布
    81,  # 冰伊布
    94   # 仙子伊布
]


def target_size(radius):
    """根据游戏中的显示尺寸计算图片大小"""
    box = (radius * 2) / ASSET_FILL
    need = int(box * 2 + 0.5)
    need = max(MIN_SIZE, min(MAX_SIZE, need))
    return need + (-need % 4)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--quality",
        type=int,
        default=88,
        help="WebP质量（默认88）"
    )
    parser.add_argument(
        "--lossless",
        action="store_true",
        help="生成无损WebP"
    )
    args = parser.parse_args()

    files = sorted(
        f for f in os.listdir(FRUIT_DIR)
        if f.lower().endswith(".png")
    )

    if len(files) != len(RADII):
        print(
            f"assets/fruits 中应有 {len(RADII)} 张 PNG，"
            f"实际找到 {len(files)} 张。"
        )
        return

    before = sum(
        os.path.getsize(os.path.join(FRUIT_DIR, f))
        for f in files
    )

    after = 0

    print("{:<25}{:<12}{:<12}{}".format(
        "文件",
        "原始",
        "优化后",
        "尺寸"
    ))

    print("-" * 65)

    for radius, name in zip(RADII, files):

        src = os.path.join(FRUIT_DIR, name)
        dst = os.path.splitext(src)[0] + ".webp"

        img = Image.open(src).convert("RGBA")

        size = target_size(radius)

        if img.size != (size, size):
            img = img.resize((size, size), Image.LANCZOS)

        if args.lossless:
            img.save(
                dst,
                "WEBP",
                lossless=True,
                quality=100,
                method=6
            )
        else:
            img.save(
                dst,
                "WEBP",
                quality=args.quality,
                method=6,
                exact=True
            )

        old_size = os.path.getsize(src)
        new_size = os.path.getsize(dst)

        after += new_size

        print(
            "{:<25}{:<12}{:<12}{}x{}".format(
                name,
                f"{old_size/1024:.0f} KB",
                f"{new_size/1024:.0f} KB",
                size,
                size
            )
        )

    print("-" * 65)

    print(
        "合计 {:.2f} MB → {:.2f} MB（减少 {:.0f}%）".format(
            before / 1048576,
            after / 1048576,
            100 * (1 - after / before)
        )
    )

    if args.lossless:
        print("模式：无损 WebP")
    else:
        print(f"模式：有损 WebP（质量 {args.quality}）")


if __name__ == "__main__":
    main()