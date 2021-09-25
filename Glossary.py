python={"Strings":"La chuoi","Booleans":"La dai dien cho true/false","Lists":"la danh sach","Comments":"La chu thich","DataTypes":"La kieu du lieu"}

print(f"Strings:{python['Strings']}\n")
print(f"Booleans:{python['Booleans']}\n")
print(f"Lists:{python['Lists']}\n")
print(f"Comments:{python['Comments']}\n")
print(f"DataTypes:{python['DataTypes']}\n")

for i in python:
    print(f"{i}:{python[i]}\n")

python["int"]="La kieu so nguyen"
python["double"]="La kieu so thuc"
python["while"]="La lap lai neu..."
python["if"]="La thuc thi neu dung..."
python["break"]="La nhay ra khoi vong lap"

for i in python:
    print(f"{i}:{python[i]}\n")









