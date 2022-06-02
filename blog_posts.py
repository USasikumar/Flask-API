from flask import Flask
from flask import request
import requests
import requests_cache #for caching redudant requests
import concurrent
from concurrent.futures import ThreadPoolExecutor #for running requests concurrently or parallely

app = Flask(__name__)
requests_cache.install_cache(cache_name='posts_cache', backend='sqlite', expire_after=180) #for caching redudant server requests


@app.route('/api/ping', methods=['GET'])  #for pinging the server to check response code as per requierment
def ping_server():
  test_url="https://api.hatchways.io/assessment/blog/posts?tag=tech" #dummy url
  response=get_server_response(test_url)
  if response.status_code==200:
    return {"success": True}, 200
  else:
    return {"success": False}, response.status_code


@app.route('/api/posts', methods=['GET']) #for getting blog posts from api
def get_posts():
  
    tags=request.args.get('tags')
    sortBy=request.args.get('sortBy')
    direction=request.args.get('direction')
    valid_sort_options=['likes','reads','id','popularity']
    valid_sort_direction=['asc','desc']

    if tags is None:
      return {"error": "Tags parameter is required"}, 400  #validation to check is required tags field is present

    if sortBy is not None and sortBy not in valid_sort_options:
      return {"error": "sortBy parameter is invalid"}, 400   #validation to check is sortby parameter is valid as per requierment

    if direction is not None and direction not in valid_sort_direction:
      return {"error": "direction parameter is invalid"}, 400    #validation to check is direction parameter is valid as per requierment

    temp_json={}
    unsorted_posts={}
    final_json=[]
    unique_posts=[]
    list_of_urls=[]

    for each_tag in tags.split(','):
      list_of_urls.append("https://api.hatchways.io/assessment/blog/posts?tag="+each_tag)  #gathering all urls to get response from

    with ThreadPoolExecutor(max_workers=10) as executor:  #running requests concurrently or parallel
        future_to_url = {executor.submit(get_server_response, each_url)for each_url in list_of_urls}

        for future in concurrent.futures.as_completed(future_to_url):
            posts = future.result().json()
            for each_post in posts['posts']:
              if sortBy is not None:
                unsorted_posts[each_post['id']]=each_post[sortBy]
              else:
                unsorted_posts[each_post['id']]=each_post['id']

              if each_post not in unique_posts:
                unique_posts.append(each_post)

        for each_post in unique_posts:
          temp_json[each_post['id']]=each_post

        if direction is not None and direction=='asc':
          sorted_posts = sorted(unsorted_posts.items(), key=lambda x: x[1]) #sorting as per sortby condition and direction
        else:
          sorted_posts = sorted(unsorted_posts.items(), key=lambda x: x[1], reverse=True) #sorting as per sortby condition and direction, default direction is desc

        for each_post in sorted_posts:
          final_json.append(temp_json[each_post[0]])
        
        return {"posts":final_json}
        

def get_server_response(each_url):  #making https requessts to the api to get blog posts
    response=requests.get(each_url)
    #caching is tested using "response.from_cache" which returns boolean value either True or False, asserting that the caching is working as expected
    return response