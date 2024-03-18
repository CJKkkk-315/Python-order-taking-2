# -*- coding: utf-8 -*-
import os
import json
import csv
import pickle
import torch
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
#导入对应的模型
from model import swin_tiny_patch4_window7_224 as create_model


def main():
    device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")
    img_size = 224
    data_transform = transforms.Compose(
        [transforms.Resize(int(img_size * 1.14)),
         transforms.CenterCrop(img_size),
         transforms.ToTensor(),
         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    pred = []
    label = []
    prob = []
    test_path = '/home/ubuntu/baimanamu/your_dataset/test/'
    # create model
    # num_classes=2是分类的类别个数
    model = create_model(num_classes=2).to(device)
    # load model weights
    model_weight_path = "./weights/model-98.pth"
    model.load_state_dict(torch.load(model_weight_path, map_location=device))
    model.eval()
    count = 0
    for classname in os.listdir(test_path):
        for file in os.listdir(test_path + classname):
            if classname == 'benign':
                ture_label = 0
            elif classname == 'malignant':
                ture_label = 1
            # load image,img_path这个地址是要预测的图片的文件位置
            img_path = test_path + classname + '/' + file
            assert os.path.exists(img_path), "file: '{}' dose not exist.".format(img_path)
            img = Image.open(img_path)
            # [N, C, H, W]
            img = data_transform(img)
            # expand batch dimension
            img = torch.unsqueeze(img, dim=0)
            with torch.no_grad():
                # predict class
                output = torch.squeeze(model(img.to(device))).cpu()
                predict = torch.softmax(output, dim=0)
                predict_cla = torch.argmax(predict).numpy()
            label.append(ture_label)
            pred.append(int(predict_cla))
            prob.append(predict[ture_label].item())
            count += 1
            print('finished:', count)
    result = {
        'label': label,
        'pred': pred,
        'prob': prob
    }
    tf = open("result.json", "w")
    json.dump(result, tf)
    tf.close()

if __name__ == '__main__':
    main()
