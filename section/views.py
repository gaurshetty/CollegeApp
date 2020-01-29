from django.shortcuts import render
from .models import Student
from .service import StudentCurdOp as service
from django.views.generic import View


class Studentops(View):
    
    def get(self, req):
        print(req.GET)
        print(req.POST)
        print(req.path)
        msg = ''
        if "edit" in req.path:
            context = {
                'student': service.get_single_student(int(req.path.split("/")[-1])),
                'students': service.get_list_students()
            }
            return render(req, 'student.html', context)
        elif "delete" in req.path:
            msg = service.delete_student(int(req.path.split("/")[-1]))
        context = {
            'student': service.get_dummy_student(),
            'students': service.get_list_students(),
            'actionmsg': msg
        }
        return render(req, 'student.html', context)

    def post(self, req):
        msg = ''
        if req.method == 'POST':
            rd = req.POST
            stud = Student(id=rd['id'], name=rd['name'], age=rd['age'], fees=rd['fees'], address=rd['address'])
            msg = service.save_update_student(stud)
        context = {
            'student': service.get_dummy_student(),
            'students': service.get_list_students(),
            'actionmsg': msg
        }
        return render(req, 'student.html', context)



# def home(req):
#     context = {
#         'student': service.get_dummy_student(),
#         'students': service.get_list_students()
#     }
#     return render(req, 'student.html', context)

# def save_update(req):
#     if req.method == 'POST':
#         rd = req.POST
#         stud = Student(id=rd['id'], name=rd['name'], age=rd['age'], fees=rd['fees'], address=rd['address'])
#         msg = service.save_update_student(stud)
#     context = {
#         'student': service.get_dummy_student(),
#         'students': service.get_list_students(),
#         'actionmsg': msg
#     }
#     return render(req, 'student.html', context)

# def edit(req, id):
#     context = {
#         'student': service.get_single_student(id),
#         'students': service.get_list_students()
#     }
#     return render(req, 'student.html', context)


# def delete(req, id):
#     msg = service.delete_student(id)
#     context = {
#         'student': service.get_dummy_student(),
#         'students': service.get_list_students(),
#         'actionmsg': msg
#     }
#     return render(req, 'student.html', context)