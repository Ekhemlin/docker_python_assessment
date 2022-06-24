import flask
from flask import jsonify, make_response
import datetime
import json
import string

"""
formatReturnPayload formats a message body into a flask response object. 

@param body: response object (that is convertable to json)
@param status: status code for the response 
@return: flask response object  
"""
def formatReturnPayload(body, status):
    json_body = jsonify(body)
    resp = flask.make_response(json_body, status)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


"""
jaccardSimilarity returns the similarity score of two sentences. 

@param sen1: original sentence 
@param sen2: phrase to compare to the original setence 
@return: float from in [0,1.0] representing the similarity score between the sentences  
"""
def jaccardSimilarity(sen1, sen2):
    # Remove all punctuation from strings
    sen1 = sen1.translate(str.maketrans('', '', string.punctuation))
    sen2 = sen2.translate(str.maketrans('', '', string.punctuation))
    # Process strings into sets.
    sen1_set = set(sen1.lower().split()) 
    sen2_set = set(sen2.lower().split())
    # Calculate similarity.
    intersection = sen1_set.intersection(sen2_set)
    union = sen1_set.union(sen2_set)
    return float(len(intersection)) / len(union)


"""
getIntentFromSentence returns the intent from the given sentence. 

@param sentence: sentence to compare to chatlogs 
@return: intent string   
"""
def getIntentFromSentence(sentence):
    # Load json chat logs 
    chatlogs_file = open('chatlogs.json')
    json_chatlogs = json.load(chatlogs_file)
    # Find sentence with highest similarity score 
    max_similarity_score = 0.0 
    max_similarity_intent = None 
    for log in json_chatlogs["chatLog"]:
        similarity = jaccardSimilarity(sentence, log["utterance"])
        if(similarity > max_similarity_score):
            max_similarity_intent = log["intent"]
            max_similarity_score = similarity
    return(max_similarity_intent)


    