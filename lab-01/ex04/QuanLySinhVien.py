from SinhVien import SinhVien
class QLSinhVien:
    listSinhvien = []
    def generate(self):
        maxId = 1
        if self.soluong_sinhvien() > 0:
            maxId = self.listSinhvien[0]._id
            for sv in self.listSinhvien:
                if maxId < sv._id:
                    maxId = sv._id
            maxId += 1
        return maxId

    def soluong_sinhvien(self):
        return self.listSinhvien.__len__()

    def nhap_sinhvien(self):
        id = self.generate()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành học: ")
        diemTB = float(input("Nhập điểm trung bình: "))
        sv = SinhVien(id, name, sex, major, diemTB)
        self.XepLoaiHocLuc(sv)
        self.listSinhvien.append(sv)

    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if (sv != None):
            name = input("Nhập tên mới: ")
            sex = input("Nhập giới tính mới: ")
            major = input("Nhập chuyên ngành mới: ")
            diemTB = float(input("Nhập điểm trung bình mới: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xep_loai_hoc_luc(sv)
        else:
            print("Sinh viên có ID = {} không tồn tại.", format(ID))
        def sortByID(self):
            self.listSinhvien.soft(key= lambda x: x._id, reverse =False)
        def sortByName(self):
            self.listSinhvien.soft(key= lambda x: x._name, reverse =False)
        def sortByDiemTB(self):
            self.listSinhvien.soft(key= lambda x: x._diemTB, reverse =False)

        def finByID(self, ID):
            searchResult = None
            if (self.soLuongSinhVien()>0):
                for sv in self.listSinhvien:
                    if(sv._id == ID):
                        searchResult = sv
            return listSV
                