# Prompt-Engineering
 generate prompts for LLMs to extract relevant entities from job descriptions and also to classify web pages given only a few examples of human scores.
# Entity Extraction with Generative Models
This notebook demonstrates how to use Cohere's generative models to extract the name of a film from the title of an article. This demonstrates Named Entity Recognition (NER) of entities which are harder to isolate using other NLP methods (and where pre-training provides the model with some context on these entities). This also demonstrates the broader usecase of sturctured generation based on providing multiple examples in the prompt.
![image](https://user-images.githubusercontent.com/110843414/190238987-ca154048-cf44-4be1-af9b-6b96124f3efe.png)
# Preparing examples for the prompt
In our prompt, we'll present the model with examples for the type of output we're after. We basically get a set of subreddit article titles, and label them ourselves. The label here is the name of the movie mentioned in the title (and "none" if no movie is mentioned).
![image](https://user-images.githubusercontent.com/110843414/190240175-984de18c-815b-46a5-b0fa-c7ce6b5c114a.png)
# Creating the extraction prompt
We'll create a prompt that demonstrates the task to the model. The prompt contains the examples above, and then presents the input text and asks the model to extract the movie name.
![image](https://user-images.githubusercontent.com/110843414/190240288-50642493-8ad7-4554-b03b-acd978a1e601.png)

