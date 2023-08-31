from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer()

text = ["Hi, how are you", "I hope you are doing good", "My name is Nguyen Anh Tu"]

vect.fit(text)

train = vect.transform(text)
train.toarray()

import pandas as pd
data = pd.DataFrame(train.toarray(), columns=vect.get_feature_names_out())
print(data)