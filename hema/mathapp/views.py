from django.shortcuts import render

def lamp_power(request):
    result = None
    if request.method == 'POST':
        try:
            intensity = float(request.POST.get('intensity'))
            resistance = float(request.POST.get('resistance'))
            result = intensity ** 2 * resistance
        except:
            result = "Invalid input!"
    return render(request, 'lamp_power.html', {'result': result})