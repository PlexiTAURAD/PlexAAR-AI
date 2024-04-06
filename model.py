import cohere
from cohere.classify import Example

co = cohere.Client('SvMpSTWkpUfpZkzWB4OAx7kWdsDARN4gVO24Qq6I') # This is your trial API key
response = co.classify(
  model='e7cd0c96-a994-46ab-be86-cd3fe11d5809-ft',
  inputs=["I want a tree that looks beautiful","I want a tree that looks beautiful","I want a tree that looks beautiful","I want a tree that looks beautiful","I want a tree that looks beautiful","I want a tree that looks beautiful"])

print('The confidence levels of the labels are: {}'.format(response.classifications))