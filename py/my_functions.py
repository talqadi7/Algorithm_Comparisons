import numpy as np
import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score, classification_report, confusion_matrix, accuracy_score, f1_score, precision_score
import matplotlib.pyplot as plt


def plot_roc(y, preds, model):
    fpr, tpr, thresholds = roc_curve(y, preds)
    optimal_idx = np.argmax(tpr - fpr)
    optimal_threshold = thresholds[optimal_idx]
    ths = int(len(thresholds)/5)
    print("max(tpr - fpr) w/ th = ", optimal_threshold)
    l1, = plt.plot([0, 1], [0, 1], '--')
    l2, = plt.plot(fpr, tpr, label = 'Random Forest')
    auc = roc_auc_score(y, preds)
    l = plt.legend([l2], [model+str(' AUC: %.2f' % auc)])
    for x, y, txt in zip(fpr[::ths], tpr[::ths], thresholds[::ths]):
        plt.annotate(np.round(txt,5), (x, y-0.04))
        plt.annotate(np.round(optimal_threshold,5), (fpr[optimal_idx], tpr[optimal_idx]-0.04))
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.show()
def matrix_info(th, y, probs):
    fpr, tpr, thresholds = roc_curve(y, probs)
    optimal_idx = np.argmax(tpr - fpr)
    optimal_threshold = thresholds[optimal_idx]
    preds = (probs >= optimal_threshold).astype(np.int)
    f1 = f1_score(y, preds, average = 'macro' )
    apr = precision_score(y, preds, average = 'macro' )
    acc = accuracy_score(y, preds)
    auc = roc_auc_score(y, probs)
    print('f1_score:')
    print(f1)

    print('precision_score:')
    print(apr)

    print('accuracy_score:')
    print(acc)

    print('Confusion Matrix:')	
    print(confusion_matrix(y,preds))
    print(classification_report(y,preds))
    
    return f1, apr, acc, auc

