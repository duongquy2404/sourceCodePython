cities={
    'Hà Nội':{
        'country':'Việt Nam',
        'population':'8,3 triệu người',
        'fact':'là thủ đô của Việt Nam.'
    },
    'New York':{
        'country':'Hoa Ky',
        'population':'8,8 triệu người',
        'fact':'là thành phố có mật độ dân số cao nhất ở Hoa Kỳ.'
    },
    'Paris':{
        'country':'Phap',
        'population':'2,2 triệu người',
        'fact':'là thủ đô của nước Pháp.'
    }
}

for city,information in cities.items():
    print(f"{city} là thành phố của {information['country']},dân số khoảng {information['population']} và {information['fact']}")