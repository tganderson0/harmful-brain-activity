import torch
from transformer import ViT

if __name__ == "__main__":
  v = ViT(
    image_size=400,
    patch_size=20,
    num_classes=6,
    dim=1024,
    depth=6,
    heads=16,
    mlp_dim=2048,
    dropout=0.1,
    emb_dropout=0.1,
  )

  