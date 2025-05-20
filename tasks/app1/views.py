from django.shortcuts import render

DAILY_TASKS = {
    "sunday": "Plan the week ahead.",
    "monday": "Prepare for meetings.",
    "tuesday": "Grocery shopping.",
    "wednesday": "Workout session.",
    "thursday": "Clean the house.",
    "friday": "Family movie night.",
    "saturday": "Gardening and relaxation.",
}

def home(request):
    week_days = [day.title() for day in DAILY_TASKS]
    context = {"week_days": week_days}
    return render(request, "index.html", context)

def show_task(request, day):
    selected_task = DAILY_TASKS.get(day.lower(), "No task found.")
    context = {"day_name": day.title(), "task_detail": selected_task}
    return render(request, "day.html", context)