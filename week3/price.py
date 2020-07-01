# 가격 계산하기

price = float(input("음식값 (정수로 입력) : "))

# 각 항목 계산
tax = price * 0.15
service = (price + tax) * 0.13
total = price + tax + service

# 각 항목을 format에 맞춤
format_price = "{:>10}".format("price")
format_tax = "{:>10}".format("tax")
format_service = "{:>10}".format("service")
format_total = "{:>10}".format("total")

# 각 항목의 출력값을 format에 맞춤
output_price = "{:7.0f}".format(price)
output_tax = "{:10.2f}".format(tax)
output_service = "{:10.2f}".format(service)
output_total = "{:10.2f}".format(total)

print("===========================")

print(format_price, " : ", output_price)
print(format_tax, " : ", output_tax)
print(format_service, " : ", output_service)
print(format_total, " : ", output_total)

print("===========================")

