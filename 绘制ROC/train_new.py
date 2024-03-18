from __future__ import print_function

import os

from torch.optim import lr_scheduler
from torchvision import transforms
from torch.utils.data import DataLoader
import numpy as np
from tqdm import tqdm
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from DataSet import Dataload, ToTensor, Normalize
from save_plot import metrics
import warnings
warnings.filterwarnings('ignore')

"""导入所有模型"""
from VGG13 import VGG13 as VGG
from DarkNet import Darknet19 as DarkNet
from ResNet import ResNet101 as ResNet
from swin_transformer import SwinTransformer
from model_v3 import MobileNetV3

datadir = '/home/ubuntu/baimanamu/Jiazhuangxiandata'  # 数据集位置
modeldir = '/home/ubuntu/baimanamu/jiazhuangxian'  # 保存模型的位置
modelname = 'MobileNetV3'  # 写模型的名字（确保先导入了）

os.environ['CUDA_VISIBLE_DEVICES'] = '1'
num_category = 3
k = 0
img_size = 256



def main():
    save_metric = metrics.SaveMetric(modeldir, modelname)
    transforms_train = transforms.Compose([  # transforms.Resize(448),
        ToTensor(),
        Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    transforms_val = transforms.Compose([  # transforms.Resize(448),
        ToTensor(),
        Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    voc_data = {'Train': Dataload(root_dir=datadir, train=True,
                                  trsf=transforms_train, image_size=img_size),
                'val': Dataload(root_dir=datadir, train=False,
                                trsf=transforms_val, image_size=img_size)}
    dataloaders = {'Train': DataLoader(voc_data['Train'], batch_size=64,
                                       shuffle=True, num_workers=16),
                   'val': DataLoader(voc_data['val'], batch_size=8,
                                     shuffle=False, num_workers=4)}
    dataset_sizes = {x: len(voc_data[x]) for x in ['Train', 'val']}

    """选择模型：从导入的模型中选择"""
    assert modelname in ['VGG', 'DarkNet','ResNet','SwinTransformer','MobileNetV3']
    if modelname == 'VGG':
        Model = VGG(num_category)
    elif modelname == 'DarkNet':
        Model = DarkNet()
    elif modelname == 'ResNet':
        Model = ResNet(num_category)
    elif modelname == 'SwinTransformer':
        Model = SwinTransformer()
    elif modelname == 'MobileNetV3':
        Model = MobileNetV3(num_category,last_channel)

    num_epoch = 70
    criterion = nn.NLLLoss(ignore_index=255)
    optimizer = optim.SGD(Model.parameters(), lr=1e-3, momentum=0.99, weight_decay=0.01)  #

    # (LR) Decreased  by a factor of 10 every 2000 iterations
    exp_lr_scheduler = lr_scheduler.StepLR(optimizer, step_size=28, gamma=0.9)  #
    # Model = nn.DataParallel(Model).cuda()

    # %% Train
    for t in range(num_epoch):  #
        print('-'*40 + 'epoch ' + str(t) + '-'*40)
        Model.train()  # Set model to training mode
        tbar = tqdm(dataloaders['Train'])
        running_loss = 0
        # Iterate over data.
        print('====训练模型====')
        for i, sample in enumerate(tbar):
            image, labels = sample['image'], sample['label']
            # image = image.cuda()
            # labels = labels.cuda()

            # zero the parameter gradients
            optimizer.zero_grad()
            with torch.set_grad_enabled(True):
                # forward
                outputs = Model(image)
                outputs = F.log_softmax(outputs, dim=1)
                loss = criterion(outputs, labels.long())
                # backward + optimize
                loss.backward()
                optimizer.step()

            # statistics
            # writer.add_scalar('loss//', loss.item())
            # writer.flush()
            exp_lr_scheduler.step()
            running_loss += loss.item() * image.size(0)
        train_loss = running_loss / dataset_sizes['Train']
        print('Training Results({}): '.format(t))
        print('Loss: {:4f}'.format(train_loss))
        print(optimizer.state_dict()['param_groups'][0]['lr'])  # 打印学习率

        """保存每个epoch的模型"""
        name = modelname + '_%d' % (k) + '_%d.pkl' % (t)
        save_metric.save_model(Model,name)

        # val
        """在训练集上的指标"""
        print('====获取训练集上的指标====')

        with torch.no_grad():

            Model.eval()  # Set model to evaluate mode
            # Model.cuda()
            TP = 0
            FP = 0
            FN = 0
            TN = 0
            total_scores = []  # 记录所有样本的分类概率
            total_labels = []  # 记录所有样本的真实标签
            for sample in tqdm(dataloaders['Train']):
                # res_rec=[]
                image, labels = sample['image'], sample['label']
                # image = image.cuda()
                # labels = labels.cuda()
                # forward
                outputs = Model(image)
                preds = outputs.data.cpu().numpy()
                result = np.argmax(preds, axis=1)
                labels = labels.data.cpu().numpy()
                total_scores.extend(preds.tolist())  # 增加当前batch的分类概率
                total_labels.extend(labels.tolist())  # 增加当前样本的真实标签
                for i, label in enumerate(labels):
                    if label == 0:
                        if result[i] == 0:
                            TN += 1
                        else:
                            FP += 1
                    else:
                        if result[i] == 0:
                            FN += 1
                        else:
                            TP += 1
            acc = (TP + TN) / (TP + TN + FP + FN + 0.01)
            Sensitive = (TP) / (TP + FP + 0.1)
            Specificity = (TN) / (TN + FN + 0.1)
            Precision = (TP) / (TP + FP + 0.1)
            Recall = TP / (TP + FN + 0.1)
            F1 = 2 * Precision * Recall / (Precision + Recall + 0.00001)
            str1 = '  TP: ' + str(TP)
            str2 = '  FN: ' + str(FN)
            str3 = ' TN ' + str(TN)
            str4 = '  FP: ' + str(FP)
            str44 = '  True' + str(TP + TN)
            str5 = '  acc: ' + str(acc)
            str6 = '  Sensitive: ' + str(Sensitive)
            str7 = '  Specificity: ' + str(Specificity)
            str8 = '  Precision: ' + str(Precision)
            str9 = '  Recall: ' + str(Recall)
            str10 = '  F1: ' + str(F1)
            print(str1 + str2 + str3 + str4 + str44 + str5 + str6 + str7 + str8 + str9 + str10)
            # 指标数据组装
            metric_dict = {'TP': TP, 'FN': FN, 'TN': TN, 'FP': FP, 'True': TP + FN, 'acc': f'{acc:.6f}',
                           'Sensitive': f'{Sensitive:.6f}', 'Specificity': f'{Specificity:.6f}',
                           'Precision': f'{Precision:.6f}', 'Recall': f'{Recall:.6f}',
                           'F1': f'{F1:.6f}'}
            # 保存指标数据
            save_metric.save_metric(model_filename=name, mode='train', metric_dict=metric_dict)
            # 获取和保存roc的绘图数据
            fpr, tpr, auc_val = metrics.get_fpr_tpr(label=total_labels, score=total_scores)
            save_metric.save_roc_about(fpr=fpr, tpr=tpr, auc_val=auc_val, model_filename=name, mode='train')

        print('====获取测试集上的指标====')
        with torch.no_grad():

            Model.eval()  # Set model to evaluate mode
            # Model.cuda()

            TP = 0
            FP = 0
            FN = 0
            TN = 0
            total_scores = []  # 记录所有样本的分类概率
            total_labels = []  # 记录所有样本的真实标签
            for sample in tqdm(dataloaders['val']):
                # res_rec=[]
                image, labels = sample['image'], sample['label']
                # image = image.cuda()
                # labels = labels.cuda()
                # forward
                outputs = Model(image)
                preds = outputs.data.cpu().numpy()
                result = np.argmax(preds, axis=1)
                labels = labels.data.cpu().numpy()
                total_scores.extend(preds.tolist())  # 增加当前batch的分类概率
                total_labels.extend(labels.tolist())  # 增加当前样本的真实标签
                for i, label in enumerate(labels):
                    if label == 0:
                        if result[i] == 0:
                            TN += 1
                        else:
                            FP += 1
                    else:
                        if result[i] == 0:
                            FN += 1
                        else:
                            TP += 1
            acc = (TP + TN) / (TP + TN + FP + FN + 0.01)
            Sensitive = (TP) / (TP + FP + 0.1)
            Specificity = (TN) / (TN + FN + 0.1)
            Precision = (TP) / (TP + FP + 0.1)
            Recall = TP / (TP + FN + 0.1)
            F1 = 2 * Precision * Recall / (Precision + Recall + 0.00001)
            str1 = '  TP: ' + str(TP)
            str2 = '  FN: ' + str(FN)
            str3 = ' TN ' + str(TN)
            str4 = '  FP: ' + str(FP)
            str44 = '  True' + str(TP + TN)
            str5 = '  acc: ' + str(acc)
            str6 = '  Sensitive: ' + str(Sensitive)
            str7 = '  Specificity: ' + str(Specificity)
            str8 = '  Precision: ' + str(Precision)
            str9 = '  Recall: ' + str(Recall)
            str10 = '  F1: ' + str(F1)
            print(str1 + str2 + str3 + str4 + str44 + str5 + str6 + str7 + str8 + str9 + str10)
            metric_dict = {'TP': TP, 'FN': FN, 'TN': TN, 'FP': FP, 'True': TP + FN, 'acc': f'{acc:.6f}',
                           'Sensitive': f'{Sensitive:.6f}', 'Specificity': f'{Specificity:.6f}',
                           'Precision': f'{Precision:.6f}', 'Recall': f'{Recall:.6f}',
                           'F1': f'{F1:.6f}'}
            # 保存模型
            save_metric.save_metric(model_filename=name, mode='test', metric_dict=metric_dict)
            # 获取和保存roc的绘图数据
            fpr, tpr, auc_val = metrics.get_fpr_tpr(label=total_labels, score=total_scores)
            save_metric.save_roc_about(fpr=fpr, tpr=tpr, auc_val=auc_val, model_filename=name, mode='test')


if __name__ == '__main__':
    main()
