import pytest
import utils 

def test_similarity_scores():
    test_cases = [["OK, and what's your order?", "I'm ready for your order.",  0.25],
                  ["I'd like a medium supreme pizza.", "Can I get a pepperoni pizza, medium?",   0.3],
                  ["Hi there, how can I help you?", "Hi there, how can I help you?",   1.0],
                  ["Is your order for one large pizza?", "Thanks, please come again.",   0.0],
                ]
    for test in test_cases:
        similarity = utils.jaccardSimilarity(test[0], test[1])
        assert similarity == test[2]



def test_correct_intent():
    test_cases = {
        "OK, your order is a large pizza and garlic bread." : "ConfirmItem", 
        "Ready in 30" : "DurationBeforePickupAnswer"
    }
    for sentence in test_cases:
        intent = utils.getIntentFromSentence(sentence)
        assert intent == test_cases[sentence]
