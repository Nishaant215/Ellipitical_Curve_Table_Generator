import EC_Points_Generator as ECPtsGen
import EC_Points_Multiply as ECPtsMult

# importing the csv module
import csv

print("Elliptic Curve: y^2 = x^3 + a*x + b (mod p)")
a = int(input("Enter the coefficient a: ").strip())
b = int(input("Enter the coefficient b: ").strip())
p = int(input("Enter the p mod value: ").strip())

# a =4
# b = 6
# p = 197
ec_equation = "Elliptic Curve: y^2 = x^3 + "+str(a)+"*x + "+str(b)+" (mod"+str(p)+")"
print(ec_equation)
print("Points on Curve")

ec_curve_points = ECPtsGen.ec_gen_points_set(a, b, p)
print(ec_curve_points)

print("Order of Elliptical Curve points: ",len(ec_curve_points),"\n")

max_order= 0
csv_list = []
fields = []
for generator in ec_curve_points:
    scale_points_set = ECPtsMult.scale_point_set(a, b, p, generator)

    order = len(scale_points_set)
    scale_points_set["Order"] = order

    print("Order:",order, generator, end="   ")
    print(scale_points_set)

    if order > max_order:
        max_order = order

    csv_list.append(scale_points_set)


for i in range(1,(max_order+1)):
    fields.append(str(i)+"P")

fields.append("Order")

filename = "EC_Points_Table.csv"
# writing to csv file
with open(filename, 'w', newline='') as csvfile:
    # creating a csv dict writer object
    csvfile.write("EC Points Table")
    csvfile.write('\n')
    csvfile.write(ec_equation)
    csvfile.write('\n')

    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(csv_list)