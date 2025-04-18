# Art Institute of Chicago API

Prompt engineering to have a LLM make a Python script to query exhibitions.

***Student**, Complete below.*

## Stats

### How many different prompts did you have to try before it worked?
We tried a ton of prompts, it was not a set amount since we just edited them quicky, but somewhere around 10 is our best guess. 

### How well did the final produced script work?
Seemingly it functions as expected. It hits the outlined requirements in the lab, so we feel it accomplishes its tasks. 

### What are some of the artwork titles from the exhibition "Ink on Paper: Japanese Monochromatic Prints (2009)"
"Summer Bush Clover"
"The Tanabata Festival"
"Landscape with Waterfall"

## Prompt

### Share the conversation URL
https://claude.ai/share/2a5ea8fa-f389-4eeb-8884-c7c0d1fe7de4



## Paste your prompt here



I want you to complete some Python code for me. I will first give you background information; then I will give you background information on the API, and lastly, I will give you a Python template.
 
## Background Information
The python script should do the following:
~~~
1. Accepts a search term from the user.
2. Searches the ArtIC API for exhibitions matching that term and that have artwork titles.
3. Prompts the user for a number of exhibitions they would like to view.
4. Displays the titles of the artwork for those exhibition to the user.
5. Loops until user exit.
~~~
 
## Search API Background
 
~~~
#Quick Start
An API (opens new window)is a structured way that one software application can talk to another. APIs power much of the software we use today, from the apps on our phones and watches to technology we see in sports and TV shows. We have built an API to let people like you easily get our data in an ongoing way.
TIP
Do you want all of our data? Are you running into problems with throttling or deep pagination? Consider using our data dumps instead of our API.
For example, you can access the /artworks listing endpoint in our API by visiting the following URL to see all the published artworks in our collection:
https://api.artic.edu/api/v1/artworks
If you want to see data for just one artwork, you can use the /artworks/{id} detail endpoint. For example, here's Starry Night and the Astronauts (opens new window)by Alma Thomas:
https://api.artic.edu/api/v1/artworks/129884
When you view these URLs in your browser, you might see a jumbled bunch of text. That's OK! If you're using Chrome, install the JSON Formatter extension (opens new window), hit reload, and the results will be formatted in a way humans can read, too.
There is a lot of data you'll get for each artwork. If you want to only retrieve a certain set of fields, change the fields parameter in the query to list which ones you want, like this:
https://api.artic.edu/api/v1/artworks?fields=id,title,artist_display,date_display,main_reference_number
TIP
The fields parameter expects either an array of field names, or a comma-separated list of field names in a single string (e.g. example above). We encourage you to use it because it makes your queries run faster and lets us track which fields need continued support.
You can paginate through results using page and limit params:
https://api.artic.edu/api/v1/artworks?page=2&limit=100
If you want to search and filter the results, you can do so via our search endpoints. For example, here is a full-text search (opens new window)for all artworks whose metadata contains some mention of cats:
https://api.artic.edu/api/v1/artworks/search?q=cats
Here is the same search, but filtered to only show artworks that are in the public domain:
https://api.artic.edu/api/v1/artworks/search?q=cats&query[term][is_public_domain]=true
Behind the scenes, our search is powered by Elasticsearch (opens new window). You can use its Query DSL (opens new window)to interact with our API. The example above uses a term (opens new window)query. Other queries we use often include exists (opens new window)and bool (opens new window). Aggregations (opens new window)are also a powerful tool.
Our API accepts queries through both GET and POST. It might be easier to visualize how the GET query above is structured by comparing it to its POST equivallent:
curl --location --request POST 'https://api.artic.edu/api/v1/artworks/search' \
--header 'Content-Type: application/json' \
--data-raw '{
    "q": "cats",
    "query": {
        "term": {
            "is_public_domain": true
        }
    }
}'
For production use, we recommend using GET and passing the entire query as minified URL-encoded JSON via the params parameter. For example:
https://api.artic.edu/api/v1/artworks/search?params=%7B%22q%22%3A%22cats%22%2C%22query%22%3A%7B%22term%22%3A%7B%22is_public_domain%22%3Atrue%7D%7D%7D
WARNING
Our API is flexible in how it accepts queries, but each method of querying is meant for a specific purpose. Use GET for simple queries, and use POST when you have complex payloads to submit with your query.
There's a lot of information you can get about our collection, and there's a lot more than artworks in our API. Explore our documentation to learn more!
~~~
 
## Python Template
import requests
def search_exhibitions(term: str) -> list[int]:
    '''Make a request to exhibitions/search for the search term,
    using Elasticsearch 'exists' option to only return results where the 'artwork titles' field is not empty
    Process the result and return a list of exhibitions IDs.
    '''
# TODO: main function that repeatedly prompts the user...
 
Based on issues that I have had in the past:
1. Ensure that requests, json, and sys are all imported.
2. Ensure that it does not always respond with "No artwork titles found for this exhibition" when asked for a number.
3. Ensure that it does not say "No artwork titles found for this exhibition" if there were artwork titles found for the exhibition.
