class Person():
    def __init__(self,ten,gioiTinh,ngaySinh):
        self.ten=ten
        self.gioiTinh=gioiTinh
        self.ngaySinh=ngaySinh
    
    def description_person(self):
        print(f"Ten: {self.ten}")
        print(f"Gioi tinh: {self.gioiTinh}")
        print(f"Ngay sinh: {self.ngaySinh}")

class Student(Person):
    def __init__(self,ten,gioiTinh,ngaySinh,maSV,diemTB,email):
        super().__init__(ten,gioiTinh,ngaySinh)
        self.maSV=maSV
        self.diemTB=diemTB
        self.email=email

    def description_student(self):
        super().description_person()
        print(f"Ma sinh vien: {self.maSV}")
        print(f"Diem TB: {self.diemTB}")
        print(f"Ngay sinh: {self.ngaySinh}")

    def checkColaship(self):
        pass

my_student=Student(input(),input(),input(),input(),input(),input())
my_student.description_student()