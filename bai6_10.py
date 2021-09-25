favorite_numbers={
    'Lực':{
        1:3,
        2:7,
        3:8
    },
    'Long':{
        1:2,
        2:3,
        3:4
    },
    'Kiên':{
        1:5,
        2:8,
        3:9
    },
    'Hùng':{
        1:1,
        2:2,
        3:5
    },
    'Dũng':{
        1:4,
        2:8,
        3:9
    }
}

for name,number in favorite_numbers.items():
    print(f"Những số yêu thích của {name} là: {number[1]}, {number[2]}, {number[3]}")