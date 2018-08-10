from django.shortcuts import render , redirect, HttpResponse

def index(request):
# clean scrub submission info
    arr = ['name', 'location', 'language', 'comments']
    for x in arr:
        if x in request.session:
            del request.session[x]
    return render(request, "surveyform/index.html" )

def process(request):
    if request.method !="POST" or request.POST['name'] =='':
        return redirect ("/")

# log submission count
    if 'submits' not in request.session:
        request.session['submits'] = 0
    request.session['submits'] += 1

# log session keys 
    for x in request.POST:
        if x not in request.session:
            request.session[x] = request.POST[x]
            print("-"*50)
    return redirect("/result" )

#LOOPING request.session AFTER REDIRECT IS AN ERROR-----WHY?!?
def result(request):
    if 'submits' not in request.session:
        return redirect ('/')
    # print("-"*50)
    # print(request.session.keys())
    # print(request.method)
    content ={}
    for x in request.session.keys():
        content[x] = request.session[x]
    #     print( str(x) +" : "+ str(content[x]))
    #     print("-"*50)
    # print(content)
    # print("-"*50)
    return render(request, "surveyform/result.html", content )


def forceredirect(request):
    # print(request)
    # print("--------------------------------flushing------------------------------")
    # request.session.flush()
    return redirect('/')


