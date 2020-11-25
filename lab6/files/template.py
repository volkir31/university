
def make_data_set(file_name):
    pass

def train_classifier(training_set_list):
    pass

def classify_test_set_list(test_set_list, classifier_list):
    pass

def report_results(result_list):
    pass


#пример работы

training_list = make_data_set("SomeTrainingData.txt")

classifier_list = train_classifier(training_list)

test_set_list = make_data_set("SomeMoreTrainingData.txt")

result_list = classify_test_set_list(test_set_list, classifier_list)

report_results(result_list)