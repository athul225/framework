from django.shortcuts import render, redirect
import datetime


subject = []

def index(request):
    
    current_date = datetime.datetime.now()

    
    if request.method == 'POST': 
        
        slno = len(subject) + 1
        sub = request.POST['subject']  
        subject.append({'slno': slno, 'sub': sub})
    
    return render(request, 'index.html', {'subjects': subject, 'date': current_date})

def todo_update(request, slno):
    
    sub = next((item for item in subject 
    if item['slno'] == slno), None)
    
    if sub is None:
        return redirect(index)

    if request.method == 'POST':
       
        todo_sub = request.POST['todo']
        sub['sub'] = todo_sub
        return redirect(index)

    return render(request, 'update.html', {'sub': sub['sub'], 'slno': slno})

def todo_delete(request, slno):
    
    sub = next((item for item in subject if item['slno'] == slno), None)
    
    if sub is None:
        return redirect(index)

    if request.method == 'POST':
        
        subject.remove(sub)
        return redirect(index)

    return render(request, 'delete.html', {'sub': sub['sub'], 'slno': slno})