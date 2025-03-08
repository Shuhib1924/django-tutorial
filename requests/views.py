from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018",
    },
    {
        "id": 3,
        "author": "John Doe",
        "title": "Blog Post 3",
        "content": "Third post content",
        "date_posted": "April 22, 2018",
    },
    {
        "id": 4,
        "author": "Jane Doe",
        "title": "Blog Post 4",
        "content": "Fourth post content",
        "date_posted": "April 23, 2018",
    },
]


def index(request):
    # content = ""
    # for post in posts:
    #     content += f"""
    # <div>{post['author']}</div>
    # <div>{post['title']}</div>
    # <div>{post['content']}</div>
    # <div>{post['date_posted']}</div>
    # <hr>
    #     """
    # return HttpResponse(content)
    return render(request, "index.html", {"posts": posts})


def post(request, post_id):
    for post in posts:
        if post["id"] == int(post_id):
            return render(request, "post.html", {"post": post})

    return HttpResponse("Post not found")
