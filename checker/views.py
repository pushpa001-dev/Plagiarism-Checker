from django.shortcuts import render

def home(request):
    if request.method == "POST":
        text1 = request.POST.get("text1")
        text2 = request.POST.get("text2")
        request.session['text1'] = text1
        request.session['text2'] = text2
        return render(request, "checker/results.html", {
            "text1": text1,
            "text2": text2,
            "similarity": calculate_similarity(text1, text2)
        })
    return render(request, "checker/home.html")


def results(request):
    text1 = request.session.get("text1", "")
    text2 = request.session.get("text2", "")
    similarity = calculate_similarity(text1, text2)
    return render(request, "checker/results.html", {
        "text1": text1,
        "text2": text2,
        "similarity": similarity
    })


# Simple similarity function (for demo)
def calculate_similarity(text1, text2):
    if not text1 or not text2:
        return 0
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    common = words1.intersection(words2)
    total = words1.union(words2)
    return round(len(common)/len(total)*100, 2)
