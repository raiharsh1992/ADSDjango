from task.task import activate_task
from django.http import JsonResponse


def trigger_task(request):
    if request.method =="GET":
        activate_task.delay(3)
        return JsonResponse({
            "message":"Created a task"
        })
    else:
        return JsonResponse({
            "message":"Invalid request type"
        })
    
    
    