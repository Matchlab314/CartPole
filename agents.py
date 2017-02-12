# coding: utf-8

import random

# ランダムなエージェント
class RandomAgent():
    def action(self):
        return random.randint(0, 1) # ０以上１以下の範囲の整数の乱数を返す

# 正負でクラップしたPD制御のエージェント
class PDAgent():
    def __init__(self, kp, kd):
        self.kp = kp
        self.kd = kd

    def action(self, observation):
        m = self.kp * observation[2] + self.kd * observation[3] # 操作量を計算
        if m >= 0:
            return 1
        if m < 0:
            return 0