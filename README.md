# Infinitus coding assessment

###  System Requirements: 

- Python3 
- Running Docker daemon 

###  Running the service: 

```
pip3 install pre-commit pytest
pre-commit install
docker-compose up
```

### Evaluating the code 

The docker container will publish the flask server on the local port 5000.

The local tests are written using the Pytest framework in `test_sentences.py`. They can also be run simply with the `pytest` command. 

To test the pre-commit hook, modify any of the python files in the directory, then stage and commit them.  