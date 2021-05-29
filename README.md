# PaperWhisperer
PaperWhisperer is a Python application that keeps you up-to-date 
with research papers. How? It retrieves the latest articles from 
arXiv on a topic, by performing a keyword-based search. Then, it creates vocal 
summaries of the articles using Text-To-Speech and stores them to disk. 

## Installation
To install the package, move to the root of the repo and type in the console:

`$ pip install .`

If you plan to develop the package further, install the package in editable 
mode also installing the packages necessary to run unittests: 

`$ pip install -e .[test]`


## Testing
To run unittests, issue the following command from the root of the repo:

`$ pytest`


## Package structure 
The package is divided into 2 sub-packages:
- retrieval
- tts

*retrieval* contains data structures and facilities necessary to retrieve 
articles from [arXiv](https://arxiv.org/). Under the hood, the app uses *arxiv*, a 
Python package that is a wrapper around the arXiv free API. 

*tts* has facilities to generate speech renditions of text-based article 
summaries. The summary of an article consists of its title, authors, and abstract. 
Speech synthesis is performed using Google Cloud Text-To-Speech.


## Setting up Google Cloud Text-To-Speech
PaperWhisperer uses Google Cloud Text-To-Speech to synthesise speech. 

In order to be able to use this service, you should: 
1. create an account on Google Cloud,
2. create a Cloud Platform project,
3. enable the Text-To-Speech API in the project
4. setup authentication
5. download a Json private key

More info on how to set up [Google Cloud Text-To-Speech](https://github.com/googleapis/python-texttospeech)

## Environment variables
The app uses an environment variable called GOOGLE_APPLICATION_CREDENTIALS 
to connect to Google Cloud Text-To-Speech safely.

In `config.yml`, set GOOGLE_APPLICATION_CREDENTIALS to the path of the Json 
private key you previously downloaded while setting up the Google service. 

Without this step, you won't be able to connect to Google Cloud 
Text-To-Speech, and the app will throw an error.


## How to create summaries
To create summaries for a keyword search, use the *create_summaries* entry 
point. This is the only console script of the package and the main entry 
point of the application.

Below is an example of how you can run the script:

`$ create_summaries "generate chord progressions" 100 /save/dir 40`

The script takes 4 positional arguments:
- keywords used for searching articles (more than one keyword is possible)
- maximum number of articles to retrieve
- directory where to store vocal summaries
- retrieve articles no older than this integer value in days


## Dependencies
PaperWhisperer depends on the following packages:

- arxiv==1.2.0
- google-cloud-texttospeech
- python-dotenv


## YouTube video
Learn more about PaperWhisperer in this project presentation video on The 
Sound of AI YouTube channel.






