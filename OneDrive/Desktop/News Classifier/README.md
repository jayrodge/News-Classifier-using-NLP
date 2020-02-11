## Business News Classifier

This is a text classifier which classify any new text into business news category among any other test. For training data, I crawled various news websites, and collected business news and labelled them as 1. With the same process, I collected other news such as Polictics, Entertainment etc. for 0/negative examples. 
Finally after the putting the collected text data with lables into a pandas dataframe, a Naive Bayes Model is training after converting the text into tfidf feature vectors.


## Steps
1. Collecting Data
2. Label
3. Classifier

----
### Collecting Data
News was collected from the news websites from various domains (Business, Cricket, Politics etc.) using a web crawler.

    crawler.py 

To use this, simply put link in BASE_URL
    
    BASE_URL='https://www.moneycontrol.com/news/business-3.html/page-'

Then, copy the XPath of the item that needs to be crawled for, and add it in the path variable.

    path=str('//*[@id="newslist-'+str(j)+'"]/p/text()')



### Labeling
After collecting the Business news and we labeled it as '1' for business news and concatenated it with other news (Sports, Entertainment etc.) and labeled them with '0' using pandas and saved them in a csv file.


### Classifier

The Classifier was trained on the data that was processed after Labelling.
In this, naive bayes model using scikit learn library was used to create the classifier in which the split for training and testing was 66 and 33.
The accuracy of this model is 88%.
This classifier can be used to classify business news from non business news in large corpus.


