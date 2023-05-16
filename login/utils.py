
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import string
import tweepy as tw
import re
import arabic_reshaper
from bidi.algorithm import get_display
from transformers import *


def get_graph():
    buffer = BytesIO()
    plt. savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64. b64encode(image_png)
    graph = graph. decode( 'utf-8')
    buffer.close()
    return graph

# show_pie_chart([10,7,5])


# function to add value labels

def chart(data_dist):
    
    plt.switch_backend('AGG')
    # creating data on which bar chart will be plot
    x = ["Positive", "Neutral", "Negative"]
        
    y = data_dist
        
    # setting figure size by using figure() function
    plt.figure(figsize = (10,5))
        
    # making the bar chart on the data

    plt.bar(x, y,color=['green', 'orange', 'red'])
        
    # calling the function to add value labels
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')
        
    # giving title to the plot
    plt.title("Sentiment analysis")
        
    # giving X and Y labels
    plt.xlabel("Sentiment")
    plt.ylabel("Number of tweets")
    plt.tight_layout()
    graph = get_graph()
    return graph


def show_pie_chart(data_dist):
    plt.switch_backend('AGG')
    #define Seaborn color palette to use
    red = [(0.8901960784313725, 0.10196078431372549, 0.10980392156862745)]
    orange = [(1.0, 0.4980392156862745, 0.0)]
    green = [(0.2, 0.6274509803921569, 0.17254901960784313)]
    labels = ['Positive', 'Neutral', 'Negative']
    #create pie chart
    plt.pie(data_dist, labels = labels, colors=green+orange+red, autopct='%.0f%%')
    plt.tight_layout()
    graph = get_graph()
    return graph


# result_type
#     Specifies what type of search results you would prefer to receive.
#     The current default is "mixed." Valid values include:

#     * mixed : include both popular and real time results in the \
#               response
#     * recent : return only the most recent results in the response
#     * popular : return only the most popular results in the response
# count
#     |count|
# until
#     Returns tweets created before the given date. Date should be
#     formatted as YYYY-MM-DD. Keep in mind that the search index has a
#     7-day limit. In other words, no tweets will be found for a date
#     older than one week.
# since_id
#     |since_id| There are limits to the number of Tweets which can be
#     accessed through the API. If the limit of Tweets has occurred since
#     the since_id, the since_id will be forced to the oldest ID
#     available.
def get_tweets(tw_text,number):
    
    consumer_key = "BQbUgYjppzaJBkAnNfGGPti9H"
    consumer_secret = "oVF6RDbgsnb51k6BoaTV0yjjqOXNNFZFYWTlou31Rg5V701xRR"
    access_token = "116391616-FehRfAhL4mEWgvwkafYOEkV9ShRZUPVtccjzeHqZ"
    access_token_secret = "XVPvuormHZHanWoOKlIaQrkPx5UH7GmhRWmpc4VJIpPxo"
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    tweets = tw.Cursor(api.search_tweets,
              q=str(tw_text),
              lang="ar",
              result_type = "recent").items(int(number))

    return [[tweet.text] for tweet in tweets]



def preprocessing(a):
    ##REMOVE phone_numbers
    a = re.sub(r'\d{10}', '', str(a))

    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags=re.UNICODE) 
    a = emoji_pattern.sub(r'', a)
    ##remove urls
    a = re.sub(r"http\S+|www.\S+", "", a)
    ##REMOVE EMAILS
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', a)
    for email in emails:
        a = a.replace(email,'')
    ##REMOVE HASHTAG
    a= re.compile('\#').sub('', re.compile('rt @[a-zA-Z0-9_]+:|@[a-zA-Z0-9_]+').sub('', a).strip())
    ##REMOVE underscore
    a = ' '.join(a.split('_'))
    ## normalize_hamza
    HAMZAT_PAT = re.compile(u"["+u"".join([u'\u0624', u'\u0626'])+u"]")
    ALEFAT_PAT = re.compile(u"["+u"".join([u'\ufef5', u'\u0623',
                                            u'\u0625', u'\u0654',
                                            u'\u0655'])+u"]")
    a = ALEFAT_PAT.sub(u'\u0627', a)
    a = HAMZAT_PAT.sub(u'\u0621', a)
    ## REMOVE COMMA + SEMICOLON + QUESTION + PERCENT + DECIMAL + THOUSANDS + STAR + FULL_STOP + MULITIPLICATION_SIGN + DIVISION_SIGN
    arabic_punctuations = u'\u060C' + u'\u061B' + u'\u061F' + u'\u066a' + u'\u066b' + u'\u066c' + u'\u066d' + u'\u06d4' + u'\u00D7' + u'\u00F7'
    all_punctuations = string.punctuation + arabic_punctuations + '()[]{}'
    all_punctuations = ''.join(list(set(all_punctuations)))
    for punctuation in all_punctuations:
        a = a.replace(punctuation, ' ')
    ##convert eastern to western numerals
    WESTERN_ARABIC_NUMERALS = ['0','1','2','3','4','5','6','7','8','9']
    EASTERN_ARABIC_NUMERALS = [u'۰', u'۱', u'۲', u'۳', u'٤', u'۵', u'٦', u'۷', u'۸', u'۹']
    eastern_to_western_numerals = {}
    for i in range(len(EASTERN_ARABIC_NUMERALS)):
        eastern_to_western_numerals[EASTERN_ARABIC_NUMERALS[i]] = WESTERN_ARABIC_NUMERALS[i]
    for num in EASTERN_ARABIC_NUMERALS:
        a = a.replace(num, eastern_to_western_numerals[num])
    ## remove extra spaces
    a = ' '.join(a.split())
    ## remove non arabic
    a = ' '.join(re.sub(u"[^\u0621-\u063A\u0640-\u0652 ]", " ", a,  flags=re.UNICODE).split())
    ## strip tatweel
    a = re.sub(u'[%s]' % u'\u0640', '', a)
    ## normalize spellerrors
    a = re.sub(u'[%s]' % u'\u0629', u'\u0647', a)
    a = re.sub(u'[%s]' % u'\u0649', u'\u064a', a)
    ## REMOVE REPEATED CHAR
    a = re.sub(r'(.)\1+', r'\1', a)
    a = "".join(a)
    
    return a

def sentimental(Utext,Unumber=20):

    text = get_tweets(str(Utext),int(Unumber))


    balance_text = []
    for i in range (0,len(text)): 
        text_pre  = preprocessing(text[i][0])
        balance_text.append(text_pre)
    print(balance_text)
    nat = 0
    pos = 0
    neg = 0

    tokenizer = AutoTokenizer.from_pretrained("ALANZI/imamu_arabic_sentimentAnalysis")
    model = AutoModelForSequenceClassification.from_pretrained("ALANZI/imamu_arabic_sentimentAnalysis")
    my_pipeline  = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    pip = my_pipeline(balance_text)
   
    for i in range (0,len(pip)):
        if pip[i]['label'] == "neutral":
            nat += 1
        elif pip[i]['label'] == "positive":
            pos += 1
        elif pip[i]['label'] == "negative":
            neg +=1
    return pos,nat,neg

pos,nat,neg = sentimental("يوم التاسيس",5)

print(pos,nat,neg)
