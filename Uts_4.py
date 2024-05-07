berat_badan = float(input("Masukkan berat badan (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (m): "))
bmi = berat_badan / (tinggi_badan ** 2)

print("Berat Badan:", berat_badan, "kg")
print("Tinggi Badan:", tinggi_badan, "m")
print("BMI Anda:", round(bmi, 2))

if bmi < 18.5:
    print("Kategori BMI: Kurang berat badan")
elif bmi < 25:
    print("Kategori BMI: Normal (sehat)")
elif bmi < 30:
    print("Kategori BMI: Kelebihan berat badan")
else:
    print("Kategori BMI: Obesitas")