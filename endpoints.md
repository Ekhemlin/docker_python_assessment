# API Endpoints doc 

##  /health 
Method: GET
Return codes: 200 (Success)
 

##  /detect_intent 
Method: POST
Mandatory body args: message
message: message to get intent for
Return codes: 200 (Success), 422 (missing argument), 500 (Internal error) 

