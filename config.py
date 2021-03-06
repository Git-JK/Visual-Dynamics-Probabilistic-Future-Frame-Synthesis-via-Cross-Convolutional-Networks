
## 数据目录设置

data_dir = 'data/shape/3Shapes2_large'
data_train_list = 'data/shape/3Shapes2_large/train.txt'
data_test_list = 'data/shape/3Shapes2_large/test.txt'
data_visualize_list = 'data/shape/3Shapes2_large/visualize.txt'

## 训练设置

cnt_epoch = 128
batch_size = 32
learning_rate = 0.001
kl_weight = 0.005  # https://github.com/yzwxx/vae-celebA/blob/master/train_vae.py#L99

log_every = 8
save_snapshot_to = 'result/current/models'
save_visualization_to = 'result/current/visualizations'
save_logs_to = 'result/current/logs'
