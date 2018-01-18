from textblob import TextBlob
import json

def get_label(polarity, threshold = 0.):
    if polarity > threshold:
        return 'Positive'
    elif polarity < threshold:
        return 'Negative'
    else:
        return 'Neutral'

aadhar_data = open('aadhar_data.csv', 'w')
aadhar_data.write('User Name, Tweet, Polarity, Sentiment_Label\n')



with open('adhar_data.json','r',newline='\r\n') as file:
    for line in file:
        tweet = json.loads(line)
        sentiment = TextBlob(tweet['text']).sentiment

        if sentiment.subjectivity*100 >= 60:
            username = tweet['user']['screen_name']
            polarity = sentiment.polarity
            sentiment_label = get_label(polarity)
            text = str(tweet['text'].encode('utf8'))
            text = text.replace("\'", "")
            text = text.replace("\"", "")
            text = text.replace(",", "")
            quoted_tweets= "\"" + text + "\""
            print(quoted_tweets,'\t Polarity:',polarity,'\n')
            
            aadhar_data.write('%s,%s,%f,%s\n' % (username, quoted_tweets, polarity, sentiment_label ))


aadhar_data.close()
        
            
