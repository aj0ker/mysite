from django.shortcuts import render,get_object_or_404
from .models import BlogArticles

# Create your views here.
# render()的作用是将数据渲染到指定的模板，第一个参数必须是request，第二个参数是模板的位置，第三个参数是要传递到模板的数据，这些数据是字典形式的。

def blog_list(request):
    blogs = BlogArticles.objects.all()
    return render(request,'blog/blog_list.html',{'blogs':blogs})

def blog_detail(request,article_id):
    article = get_object_or_404(BlogArticles,id=article_id)
    pub = article.publish
    return render(request,'blog/blog_detail.html',{'article':article,'publish':pub})