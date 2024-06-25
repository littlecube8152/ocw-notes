import pdb
import numpy as np
import code_for_hw3_part2 as hw3

#-------------------------------------------------------------------------------
# Auto Data
#-------------------------------------------------------------------------------

# Returns a list of dictionaries.  Keys are the column names, including mpg.
auto_data_all = hw3.load_auto_data('auto-mpg.tsv')

# The choice of feature processing for each feature, mpg is always raw and
# does not need to be specified.  Other choices are hw3.standard and hw3.one_hot.
# 'name' is not numeric and would need a different encoding.
# features = [('cylinders', hw3.raw),
#             ('displacement', hw3.raw),
#             ('horsepower', hw3.raw),
#             ('weight', hw3.raw),
#             ('acceleration', hw3.raw),
#             ## Drop model_year by default
#             ## ('model_year', hw3.raw),
#             ('origin', hw3.one_hot)]

# Construct the standard data and label arrays
# auto_data, auto_labels = hw3.auto_data_and_labels(auto_data_all, features)
# print('auto data and labels shape', auto_data.shape, auto_labels.shape)

#-------------------------------------------------------------------------------
# Evaluation
#-------------------------------------------------------------------------------

if False:
    feature_sets = [('feature set 1',
                    [('cylinders',       hw3.raw),
                     ('displacement',    hw3.raw),
                     ('horsepower',      hw3.raw),
                     ('weight',          hw3.raw),
                     ('acceleration',    hw3.raw),
                     ('origin',          hw3.one_hot)]),
                    ('feature set 2',
                    [('cylinders',       hw3.one_hot), 
                     ('displacement',    hw3.standard),
                     ('horsepower',      hw3.standard),
                     ('weight',          hw3.standard),
                     ('acceleration',    hw3.standard),
                     ('origin',          hw3.one_hot)])]

    learners = [('perceptron', hw3.perceptron), ('averaged', hw3.averaged_perceptron)]
    iterations = [1, 10, 50]

    for T in iterations:
        for fname, features in feature_sets:
            result = []
            for lname, learner in learners:
                auto_data, auto_labels = hw3.auto_data_and_labels(auto_data_all, features)
                print("evaluating {0}, learner {1} with {2} iteration".format(fname, lname, T))
                result.append(hw3.xval_learning_alg(learner, auto_data, auto_labels, 10, {'T': T}))
            print("accuracy", result)


if False:                               # set to True to see histograms
    import matplotlib.pyplot as plt
    for feat in range(auto_data.shape[0]):
        print('Feature', feat, features[feat][0])
        # Plot histograms in one window, different colors
        plt.hist(auto_data[feat,auto_labels[0,:] > 0])
        plt.hist(auto_data[feat,auto_labels[0,:] < 0])
        plt.show()
        # Plot histograms in two windows, different colors
        fig,(a1,a2) = plt.subplots(nrows=2)
        a1.hist(auto_data[feat,auto_labels[0,:] > 0])
        a2.hist(auto_data[feat,auto_labels[0,:] < 0])
        plt.show()

#-------------------------------------------------------------------------------
# Analyze auto data
#-------------------------------------------------------------------------------

if False:
    feature = [('cylinders',       hw3.one_hot), 
               ('displacement',    hw3.standard),
               ('horsepower',      hw3.standard),
               ('weight',          hw3.standard),
               ('acceleration',    hw3.standard),
               ('origin',          hw3.one_hot)]
    auto_data, auto_labels = hw3.auto_data_and_labels(auto_data_all, feature, False)
    th, th0 = hw3.averaged_perceptron(auto_data, auto_labels, {'T': 10})
    print("Separator for automobile data:", th, th0)

#-------------------------------------------------------------------------------
# Review Data
#-------------------------------------------------------------------------------

if False:
    # Returns lists of dictionaries.  Keys are the column names, 'sentiment' and 'text'.
    # The train data has 10,000 examples
    review_data = hw3.load_review_data('reviews.tsv')

    # Lists texts of reviews and list of labels (1 or -1)
    review_texts, review_label_list = zip(*((sample['text'], sample['sentiment']) for sample in review_data))

    # The dictionary of all the words for "bag of words"
    dictionary = hw3.bag_of_words(review_texts)

    # The standard data arrays for the bag of words
    review_bow_data = hw3.extract_bow_feature_vectors(review_texts, dictionary)
    review_labels = hw3.rv(review_label_list)
    print('review_bow_data and labels shape', review_bow_data.shape, review_labels.shape)

#-------------------------------------------------------------------------------
# Analyze review data
#-------------------------------------------------------------------------------

if False:
    learners = [('perceptron', hw3.perceptron), ('averaged', hw3.averaged_perceptron)]
    iterations = [1, 10, 50]

    for T in iterations:
        result = []
        for lname, learner in learners:
            data = review_bow_data
            labels = review_labels
            print("evaluating learner {0} with {1} iteration".format(lname, T))
            result.append(hw3.xval_learning_alg(learner, data, labels, 10, {'T': T}))
        print("accuracy", result)

if False:
    th, th0 = hw3.averaged_perceptron(review_bow_data, review_labels, {'T': 10})
    rdict = hw3.reverse_dict(dictionary)
    words_result = []

    for i in range(len(th)):
        words_result.append([th[i][0], rdict[i]])
    words_result.sort()
    print([words_result[i][1] for i in range(10)])
    words_result = words_result[::-1]
    print([words_result[i][1] for i in range(10)])

#-------------------------------------------------------------------------------
# MNIST Data
#-------------------------------------------------------------------------------

"""
Returns a dictionary formatted as follows:
{
    0: {
        "images": [(m by n image), (m by n image), ...],
        "labels": [0, 0, ..., 0]
    },
    1: {...},
    ...
    9
}
Where labels range from 0 to 9 and (m, n) images are represented
by arrays of floats from 0 to 1
"""
mnist_data_all = hw3.load_mnist_data(range(10))

print('mnist_data_all loaded. shape of single images is', mnist_data_all[0]["images"][0].shape)

# HINT: change the [0] and [1] if you want to access different images
# d0 = mnist_data_all[0]["images"]
# d1 = mnist_data_all[1]["images"]
# y0 = np.repeat(-1, len(d0)).reshape(1,-1)
# y1 = np.repeat(1, len(d1)).reshape(1,-1)

# data goes into the feature computation functions
# data = np.vstack((d0, d1))
# labels can directly go into the perceptron algorithm
# labels = np.vstack((y0.T, y1.T)).T

def raw_mnist_features(x):
    """
    @param x (n_samples,m,n) array with values in (0,1)
    @return (m*n,n_samples) reshaped array where each entry is preserved
    """
    (t, m, n) = np.shape(x)
    return x.reshape(t, -1).T


def row_average_features(x):
    """
    This should either use or modify your code from the tutor questions.

    @param x (n_samples,m,n) array with values in (0,1)
    @return (m,n_samples) array where each entry is the average of a row
    """
    return np.average(x, axis=2).T


def col_average_features(x):
    """
    This should either use or modify your code from the tutor questions.

    @param x (n_samples,m,n) array with values in (0,1)
    @return (n,n_samples) array where each entry is the average of a column
    """
    return np.average(x, axis=1).T


def top_bottom_features(x):
    """
    This should either use or modify your code from the tutor questions.

    @param x (n_samples,m,n) array with values in (0,1)
    @return (2,n_samples) array where the first entry of each column is the average of the
    top half of the image = rows 0 to floor(m/2) [exclusive]
    and the second entry is the average of the bottom half of the image
    = rows floor(m/2) [inclusive] to m
    """
    (t, m, n) = np.shape(x)
    [up, down] = np.split(x, [m//2], axis=1)
    up = np.average(up, axis=(1,2)).reshape(1,-1)
    down = np.average(down, axis=(1,2)).reshape(1,-1)
    return np.vstack((up, down))

def row_differential(x):
    """
    @param x (n_samples,m,n) array with values in (0,1)
    @return (m(n-1),n_samples) array
    """
    (t, m, n) = np.shape(x)
    d = np.zeros((t, m, n - 1))
    for i in range(t):
        for j in range(m):
            for k in range(n - 1):
                d[i][j][k] = x[i][j][k + 1] - x[i][j][k]
    return raw_mnist_features(d)

# data = np.array([[[0, 1, 0],
#                   [0, 1, 0],
#                   [0, 1, 0]],
#                  [[1, 0, 0],
#                   [0, 1, 0],
#                   [0, 0, 1]],
#                  [[0, 1, 1],
#                   [1, 1, 1],
#                   [1, 1, 0]]])
# print(top_bottom_features(data))

# use this function to evaluate accuracy
# acc = hw3.get_classification_accuracy(raw_mnist_features(data), labels)

#-------------------------------------------------------------------------------
# Analyze MNIST data
#-------------------------------------------------------------------------------

# Your code here to process the MNIST data
compare_list = [(0, 1), (2, 4), (6, 8), (9, 0)]

# 6.2 A: raw feature
result = []
for a, b in compare_list:
    d0 = mnist_data_all[a]["images"]
    d1 = mnist_data_all[b]["images"]
    y0 = np.repeat(-1, len(d0)).reshape(1,-1)
    y1 = np.repeat(1, len(d1)).reshape(1,-1)

    data = raw_mnist_features(np.vstack((d0, d1)))
    labels = np.vstack((y0.T, y1.T)).T
    
    acc = hw3.xval_learning_alg(hw3.perceptron, data, labels, 10, {'T':50})
    print("classification between {0} and {1} according to raw feature: accuracy {2}".format(a, b, acc))
    result.append(acc)
print(result)

# 6.2 B-E: using different features
feature_list = [("row", row_average_features), ("column", col_average_features), ("top-bottom", top_bottom_features), ("row differential", row_differential)]

for a, b in compare_list:
    d0 = mnist_data_all[a]["images"]
    d1 = mnist_data_all[b]["images"]
    y0 = np.repeat(-1, len(d0)).reshape(1,-1)
    y1 = np.repeat(1, len(d1)).reshape(1,-1)

    result = []
    labels = np.vstack((y0.T, y1.T)).T
    for fname, feature_fun in feature_list:
        data = feature_fun(np.vstack((d0, d1)))
        acc = hw3.xval_learning_alg(hw3.perceptron, data, labels, 10, {'T':50})
        print("classification between {0} and {1} according to {2} feature: accuracy {3}".format(a, b, fname, acc))
        result.append(acc)
    print(result)

# 