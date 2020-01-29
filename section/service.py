from .models import Student


class StudentCurdOp():

    def get_list_students():
        return Student.objects.all()

    def get_single_student(id):
        return Student.objects.get(id=id)

    def get_dummy_student():
        return Student(id=0, name='', age=0, fees=0, address='')

    def save_update_student(stud):
        if stud.id == '0':
            Student.objects.create(name=stud.name, age=stud.age, fees=stud.fees, address=stud.address)
            return "Record added successfully..!"
        else:
            stud.save()
            return "Record updated successfully..!"
            
    def delete_student(id):
        dbstud = StudentCurdOp.get_single_student(id)
        if dbstud:
            dbstud.delete()
            return "Record deleted successfully..!"
        return "Record cannot delete as no record for given id..."
