from re import A


class ThiSinh:
    def __init__(self,hoTen,ngaySinh,diem1,diem2,diem3):
        self.hoTen=hoTen
        self.ngaySinh=ngaySinh
        self.diem1=diem1
        self.diem2=diem2
        self.diem3=diem3
    
    def show(self):
        print(self.hoTen,self.ngaySinh,self.diem1+self.diem2+self.diem3)

if __name__=='__main__':
    hoten=input()
    ngaySinh=input()
    diem1=float(input())
    diem2=float(input())
    diem3=float(input())
    ts=ThiSinh(hoten,ngaySinh,diem1,diem2,diem3)
    ts.show()