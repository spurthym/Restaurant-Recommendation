class Settings:
    def __init__(self):
        pass

    DATASET_FILE = '/Users/spurthy/Desktop/Restaurant-Recommendation/dataset/tempe_review_1600.json'
    MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
    # REVIEWS_DATABASE = "Dataset_Challenge_Reviews" # original, trained

    TAGS_DATABASE = "Tags"
    REVIEWS_COLLECTION = "inv"
    CORPUS_COLLECTION = "Corpus"
    USER_DATABASE = "user"
    USER_COLLECTION = "u"
    BUSINESS_COLLECTION = "b"
    USER_STOP="su"
    BUSINESS_STOP="sb"
    USER_PROFILE="up"
    BUSINESS_PROFILE="ub"



