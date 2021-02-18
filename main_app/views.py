from django.shortcuts import render, redirect
from .models import BlogCategory, BlogPost
from .forms import BlogCategoryForm, BlogPostForm



def startpage(request):
    context= {'hello':'This is startpage from main_app'}
    return render(request, 'main_app/startpage.html', context)

def blogcats(request):
    cats = BlogCategory.objects.all()

    context={'cats':cats}
    return render(request,'main_app/allcats.html',context=context)

def addcat(request):
    if request.method=='POST':
        form = BlogCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:blogcats')
        else:
            form = BlogCategoryForm(request.POST)
            return render(request,'main_app/addcat.html',{'form':form})
    else:
        form = BlogCategoryForm()
        return render(request, 'main_app/addcat.html', {'form':form})

def editcat(request, pk):
    if request.method == 'POST':
        form = BlogCategoryForm(request.POST)
        if form.is_valid():
            cat = BlogCategory.objects.get(pk=pk)
            cat.name = form.cleaned_data['name']
            cat.description = form.cleaned_data['description']
            cat.save()
            return redirect('main_app:blogcats')
        else:
            return redirect('main_app:editcat')
    else:
        cat = BlogCategory.objects.get(pk=pk)
        form = BlogCategoryForm(instance=cat)
        context = {'form':form, 'cat':cat}
        return render(request, 'main_app/editcat.html', context=context)

def deletecat(request, pk):
    cat = BlogCategory.objects.get(pk=pk)
    cat.delete()
    return redirect('main_app:blogcats')


def blogposts(request):
    posts = BlogPost.objects.all()

    context={'posts':posts}
    return render(request, 'main_app/allposts.html', context=context)

def addpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:allposts')
        else:
            form = BlogPostForm(request.POST)
            return render(request, 'main_app:addpost.html', {'form':form})
    else:
        form = BlogPostForm()
        context = {'form':form}
        return render(request, 'main_app/addpost.html', context=context)


def editpost(request,pk):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = BlogPost.objects.get(pk=pk)
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('main_app:allposts')
        else:
            return redirect('main_app:editpost')
    else:
        post = BlogPost.objects.get(pk=pk)
        form = BlogPostForm(instance=post)
        context = {'form':form, 'post':post}
        return render(request, 'main_app/editpost.html', context=context)


def delpost(request,pk):
    post = BlogPost.objects.get(pk=pk)
    post.delete()
    return redirect('main_app:allposts')




