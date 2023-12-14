import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('C:/Users/asus/fcb_posts')

data = data.rename(columns={'0': 'posts'})

# Delete lines containing strings in Arabic
arabic_mask = data['posts'].str.contains('[\u0600-\u06FF]+')
data = data.drop(data[arabic_mask].index)

# Finding contractions
contractions_dict = {"ain't": "are not","'s":" is","aren't": "are not"}
contractions_re=re.compile('(%s)' % '|'.join(contractions_dict.keys()))
def expand_contractions(text,contractions_dict=contractions_dict):
    def replace(match):
        return contractions_dict[match.group(0)]
    return contractions_re.sub(replace, text)
data['posts']=data['posts'].apply(lambda x:expand_contractions(x))

# Make posts in lower case
data['posts'] = data['posts'].str.lower()

# Remove punctuation
string.punctuation = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
data['posts'] = data['posts'].apply(lambda x: re.sub('[%s]' % re.escape(string.punctuation), '' , x))

#### Remove stopwords
stop_words = set(stopwords.words('english'))
stop_words.add('language')
stop_words.add('models')
stop_words.add('chatgbt')
stop_words.add('for')
stop_words.add('dialogue')
stop_words.add('see')
stop_words.add('more')
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in stop_words])
#here we have implemented a custom function that will split each word from the text and check whether it is a stopword or not.
#If not then pass as it is in string and if stopword then removes it.
data['posts'] = data['posts'].apply(lambda x: remove_stopwords(x))

# Remove empty rows 
data.drop(data[data['posts'] == ''].index, inplace=True)

# Noise removal: This is to eliminate unwanted elements such as URLs, email addresses, HTML tags
def eliminate_noise(text):
    # Suppression des URL
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)    
    # Suppression des adresses e-mail
    text = re.sub(r"\S+@\S+", "", text)
    # Suppression des caractères spéciaux et des chiffres
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    # Suppression des espaces supplémentaires
    text = re.sub(r"\s+", " ", text)
    return text
data['posts'] = data['posts'].apply(eliminate_noise)

# Stemming
stemmer = PorterStemmer()
def stem_words(text):
    return " ".join([stemmer.stem(word) for word in text.split()])
data['posts'] = data['posts'].apply(lambda x: stem_words(x))

# lemmatization
lemmatizer = WordNetLemmatizer()
def lemmatize_words(text):
    return " ".join([lemmatizer.lemmatize(word) for word in text.split()])
data['posts'] = data['posts'].apply(lambda text: lemmatize_words(text))

#### Remove Extra Spaces
data["posts"] = data["posts"].apply(lambda x: re.sub(' +', ' ', x))
