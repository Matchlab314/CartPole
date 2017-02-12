# coding : utf-8

# 正負でクラップしたPD制御のエージェントを使ったCartPole-v0のデモンストレーション

# 値の意味
#  observation : [カートの位置(単位不明), カートの速度(単位不明), ポールの角度(ラジアン), ポールの角速度(単位不明)]
#  action : 0->-1, 1->+1
#  step : 100step = 1秒
# 終了条件 : 15度以上傾く or 2.4(単位不明)以上中心から移動 or 200ステップ

import agents
import gym
from gym import wrappers

video_path = './video' # ビデオを保存するパス
n_episode = 1 # エピソード数
n_step = 200 # ステップ数
# PD制御パラメータ(ちなみP制御だけだと上手く行かない)
# ※正負でクラップしているので、比しか意味ない
kp = 0.1
kd = 0.01

myagent = agents.PDAgent(kp, kd) # 正負でクラップしたPD制御のエージェント
env = gym.make('CartPole-v0') # 環境作成
# 指定のディレクトリにビデオを保存する環境のラップクラス
# force=True：以前のモニタファイルを自動的にクリア
env = wrappers.Monitor(env, video_path, force=True)
for i_episode in range(n_episode):
    observation = env.reset() # 環境初期化＆初期観察取得
    for t in range(n_step):
        env.render() # 環境を表示(でもMonitorを使うとなくても表示される)
        print(observation)
        action = myagent.action(observation) # エージェントクラスから行動を取得
        observation, reward, done, info = env.step(action) # １ステップ進める
        if done: # 終了フラグ
            print('Episode finished after {} timesteps'.format(t+1))
            break
