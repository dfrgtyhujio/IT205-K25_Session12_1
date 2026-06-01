# 1. PHÂN TÍCH INPUT/OUTPUT
# Input:
# - Lựa chọn menu: Chuỗi ký tự (str)
# - Mã sản phẩm: Chuỗi ký tự (str)
# - Tên sản phẩm: Chuỗi ký tự (str)
# - Số lượng: Chuỗi ký tự (str), kiểm tra bằng isdigit() rồi ép sang int
# - Đơn giá: Chuỗi ký tự (str), kiểm tra bằng isdigit() rồi ép sang int

# Output:
# - Danh sách sản phẩm trong giỏ hàng
# - Tổng số lượng sản phẩm
# - Tổng tiền cần thanh toán
# - Thông báo thêm, sửa, xóa thành công
# - Thông báo lỗi khi dữ liệu không hợp lệ


# 2. ĐỀ XUẤT GIẢI PHÁP
# - Dùng vòng lặp while True để hiển thị menu
# - Lưu dữ liệu bằng List chứa Dictionary
# - Chuẩn hóa mã sản phẩm bằng .strip().upper()
# - Kiểm tra dữ liệu bằng isdigit()
# - Kiểm tra số lượng > 0 và đơn giá >= 0
# - Dùng vòng lặp for để tìm sản phẩm
# - Nếu mã đã tồn tại thì cộng dồn số lượng
# - Nếu chưa tồn tại thì thêm mới
# - Dùng remove() để xóa sản phẩm
# - Tính tổng tiền = số lượng * đơn giá
# - Kiểm tra menu hợp lệ trước khi xử lý


# 3. THIẾT KẾ THUẬT TOÁN
# Bước 1: Khởi tạo danh sách cart_items
# Bước 2: Hiển thị menu và nhận lựa chọn
# Bước 3:
# - Chức năng 1:
#   + Hiển thị danh sách sản phẩm
#   + Tính tổng số lượng và tổng tiền

# - Chức năng 2:
#   + Nhập thông tin sản phẩm
#   + Kiểm tra dữ liệu hợp lệ
#   + Nếu mã tồn tại thì cộng số lượng
#   + Nếu chưa tồn tại thì thêm mới

# - Chức năng 3:
#   + Nhập mã sản phẩm và số lượng mới
#   + Tìm sản phẩm theo mã
#   + Cập nhật số lượng hoặc báo lỗi

# - Chức năng 4:
#   + Nhập mã sản phẩm cần xóa
#   + Tìm và xóa sản phẩm
#   + Nếu không có thì báo lỗi

# - Chức năng 5:
#   + Thoát chương trình bằng break

# - Nhập sai menu:
#   + Thông báo "Lựa chọn không hợp lệ"
#   + Quay lại menu


cart_items = [
    {
        "id": "P001", 
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon", 
        "number": 2, 
        "price": 150000
    }
]

while True:
    print('\n==========================================')
    print('      SHOPEE CART MANAGEMENT SYSTEM      ')
    print('==========================================')
    print('1. Xem chi tiêt giỏ hàng & Tính tổng tiên')
    print('2. Thêm sản phẩm mới / Cộng dôn sô lượng')
    print('3. Cập nhật sô lượng của một sản phẩm')
    print('4. Xóa sản phẩm khỏi giỏ hàng')
    print('5. Thoát chương trình')
    print('==========================================')

    choice = input('Mời bạn chọn chức năng (1-5) :').strip()
    
    if choice == '1':
        total = 0
        count = 0
        for i, item in enumerate(cart_items):
            print(f"{i+1}. {item['name']} - Số lượng: {item['number']} - Đơn giá: {item['price']:,} VNĐ")
            total += item['number'] * item['price']
            count += 1

        print(f"\nTổng tiền: {total:,} VNĐ")
        print(f"Tổng số lượng sản phẩm: {count}")
    
    elif choice == '2':
        status = False
        id = input("Nhập mã sản phẩm: ").strip().upper()
        
        for item in cart_items:
            if item["id"] == id:
                number = input("Nhập số lượng sản phẩm: ").strip()
                
                if not number.isdigit() or int(number) <= 0:
                    print("Số lượng mua phải là số nguyên dương lớn hơn 0")
                    break
                    
                else:
                    item["number"] += int(number)
                    print("Đã cộng dồn số lượng sản phẩm")
                    status = True
                    break
        
        if status == False:
            name = input("Nhập tên sản phẩm: ").strip()
                
            number = input("Nhập số lượng sản phẩm: ").strip()
            if not number.isdigit() or int(number) <= 0:
                print("Số lượng mua phải là số nguyên dương lớn hơn 0")
                continue
                    
            price = input("Nhập giá sản phẩm: ").strip()
            if not price.isdigit() or int(price) <= 0:
                print("Giá sản phẩm phải là số nguyên dương lớn hơn 0")
                continue
                    
            cart_items.append({
                "id": id,
                "name": name,
                "number": int(number),
                "price": int(price)
            })
            
            print('Thêm sản phẩm thành công')

    elif choice == '3':
        id = input("Nhập mã sản phẩm: ").strip().upper()
        
        for item in cart_items:
            if item["id"] == id:
                new_number = input("Nhập số lượng mới: ").strip()
                if not new_number.isdigit() or int(new_number) <= 0:
                    print("Số lượng mới không hợp lệ")
                else:
                    item["number"] = int(new_number)
                    print("Đã cập nhật số lượng sản phẩm")
                break
        else:
            print("Không tìm thấy sản phẩm cần cập nhật")
            
    elif choice == '4':
        id = input("Nhập mã sản phẩm: ").strip().upper()

        for i, item in enumerate(cart_items):
            if item["id"] == id:
                cart_items.pop(i)
                print("Đã xóa sản phẩm khỏi giỏ hàng")
                break
        else:
            print("Không tìm thấy sản phẩm cần xóa")
            
    elif choice == '5':
        print('Cảm ơn bạn đã sử dụng dịch vụ!')
        break
    else:
        print('Lựa chọn không hợp lệ. Vui lòng chọn lại.')
        
