favorite_places={
    'Ánh':{
        1:'Vũng Tàu',
        2:'Cà Mau',
        3:'Thanh Hóa',
    },
    'Ba':{
        1:'Ninh Bình',
        2:'Tây Bắc',
        3:'Móng Cái',
    },
    'Cường':{
        1:'Hạ Long',
        2:'Tây Nguyên',
        3:'Hà Nội',
    }
}

for name,favorite in favorite_places.items():
    print(f"Bạn {name} có 3 địa điểm yêu thích đó là: {favorite[1]},{favorite[2]},{favorite[3]}")