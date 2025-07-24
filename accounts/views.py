from django.http import HttpResponse, JsonResponse
from .recaptcha import verify_recaptcha

def home(request):
    return HttpResponse("✅ WUD starter project is running!")

def signup(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)
    token = request.POST.get("g-recaptcha-response", "")
    if not verify_recaptcha(token):
        return JsonResponse({"error": "recaptcha‑failed"}, status=400)
    return JsonResponse({"ok": True})