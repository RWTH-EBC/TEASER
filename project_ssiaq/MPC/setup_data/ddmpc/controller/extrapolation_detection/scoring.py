import numpy as np
import sklearn.metrics as metrics


def score_samples(data_groundtruth, data_nscores, nscores_threshold, beta=None, print_opt=True, advanced=True):
    classification = np.zeros((len(data_nscores), 1))
    classification[data_nscores > nscores_threshold] = 1

    truePositiveMat = np.zeros((len(data_groundtruth), 1))
    truePositiveMat[((data_groundtruth == 1) & (classification == 1))] = 1
    truePositive = np.sum(truePositiveMat)

    trueNegativeMat = np.zeros((len(data_groundtruth), 1))
    trueNegativeMat[((data_groundtruth == 0) & (classification == 0))] = 1
    trueNegative = np.sum(trueNegativeMat)

    falsePositiveMat = np.zeros((len(data_groundtruth), 1))
    falsePositiveMat[((data_groundtruth == 0) & (classification == 1))] = 1
    falsePositive = np.sum(falsePositiveMat)

    falseNegativeMat = np.zeros((len(data_groundtruth), 1))
    falseNegativeMat[((data_groundtruth == 1) & (classification == 0))] = 1
    falseNegative = np.sum(falseNegativeMat)

    if (truePositive+falsePositive) != 0:
        precision = truePositive / (truePositive+falsePositive)
    else:
        precision = 1
    recall = truePositive / (truePositive+falseNegative)
    if (precision+recall) == 0:
        F = 0
    else:
        F = 2*(precision*recall)/(precision+recall)
    result_dict = {'truePositive': truePositive, 'trueNegative': trueNegative, 'falsePositive': falsePositive,
                   'falseNegative': falseNegative, 'precision': precision, 'recall': recall, 'F': F}
    if print_opt:
        print('truePositive: ' + str(truePositive))
        print('trueNegative: ' + str(trueNegative))
        print('falsePositive: ' + str(falsePositive))
        print('falseNegative: ' + str(falseNegative))
        print('precision: ' + str(precision))
        print('recall: ' + str(recall))
        print('F: ' + str(F))

    if beta is not None:
        if truePositive == 0:
            Fbeta = 0
        else:
            Fbeta = (1 + beta ** 2) * (precision * recall) / (beta ** 2 * precision + recall)
        result_dict['Fbeta'] = Fbeta
        if print_opt:
            print('Fbeta: ' + str(Fbeta))
    else:
        result_dict['Fbeta'] = F

    if advanced:
        roc = round(metrics.roc_auc_score(data_groundtruth, data_nscores), ndigits=4)
        result_dict['roc'] = roc
        if print_opt:
            print('roc: ' + str(roc))

        roc_x, roc_y, _ = metrics.roc_curve(data_groundtruth, data_nscores)
        result_dict['roc_x'] = roc_x
        result_dict['roc_y'] = roc_y

        prc_y, prc_x, thresholds = metrics.precision_recall_curve(data_groundtruth, data_nscores)
        thresholds = np.append(thresholds, thresholds[-1])
        thresholds = (thresholds - min(thresholds))/(max(thresholds)-min(thresholds))
        result_dict['prc_x'] = prc_x
        result_dict['prc_y'] = prc_y
        result_dict['prc_thresholds'] = thresholds

        outliers = np.sum(data_groundtruth)
        outlier_share = outliers / len(data_groundtruth)
        if beta is None:
            beta = 1
        rel_F = (F-(1+beta**2)*outlier_share/(1+beta**2 * outlier_share))/(1.0-(1+beta**2)*outlier_share/(1+beta**2 * outlier_share))
        result_dict['rel_F'] = rel_F

    return dict
