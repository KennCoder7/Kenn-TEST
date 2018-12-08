import numpy as np
import os
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

y_true = np.array(['cat', 'dog', 'pig', 'cat', 'dog', 'pig'])
y_pred = np.array(['cat', 'pig', 'dog', 'cat', 'cat', 'dog'])
# print(precision_recall_fscore_support(y_true, y_pred, average='macro'))
# # Macro-P,Macro-R,Macro-F1
# print(precision_recall_fscore_support(y_true, y_pred, average='micro'))
# # Micro-P,Micro-R,Micro-F1
# print(classification_report(y_true, y_pred))

# (0.2222222222222222, 0.3333333333333333, 0.26666666666666666, None)
# (0.3333333333333333, 0.3333333333333333, 0.3333333333333333, None)
#              precision    recall  f1-score   support
#
#         cat       0.67      1.00      0.80         2
#         dog       0.00      0.00      0.00         2
#         pig       0.00      0.00      0.00         2
#
# avg / total       0.22      0.33      0.27         6

report = classification_report(y_true, y_pred)
cm = confusion_matrix(y_true, y_pred)
print(str(cm))
with open("./data/test.txt", 'a') as f:
    f.write("# Report:\n")
    f.write(report)
    f.write("# Confusion matrix:\n")
    f.write(str(cm))
    f.write('\n')
os.rename("./data/test.txt", "./data/new_test.txt")