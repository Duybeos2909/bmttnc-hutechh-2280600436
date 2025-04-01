#tạo danh sách rỗng
j =[]
# duyệt qua tất cả các số trong khoản từ 2000 đến 3200, kiểm tra xem số i chia hết cho 7 và không phải là bội số của 5
for i in range (2000, 3200):
    if(i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))