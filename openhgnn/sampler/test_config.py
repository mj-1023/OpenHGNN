CONFIG={
    # 'max_epoch': 100, 'patience': 30, 'lr': 0.005, 'weight_decay': 0.001, 'dropout': 0.5, 'hidden_dim': 64,
    # 'encoder_type': 'RotateE', 'inter_attn_feats': 128, 'num_heads': 8, 'num_layers': 2,
    # 'dataset': 'imdb4MAGNN', 'gpu':-1, 'batch_size':16
    'max_epoch': 10, 'patience': 30, 'lr': 0.005, 'weight_decay': 0.001, 'dropout': 0.5, 'hidden_dim': 4,
    'encoder_type': 'RotateE', 'inter_attn_feats': 4, 'num_heads': 2, 'num_layers': 2, 'out_dim':3,
    'dataset': 'imdb4MAGNN', 'category':'M', 'batch_size':5, 'device':'cpu'
}