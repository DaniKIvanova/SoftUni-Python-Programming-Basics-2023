number_package_pen = int(input())
number_package_marker = int(input())
number_package_preparation = int(input())
percentage_reduction = int(input())

package_pen = 5.80
package_marker = 7.20
preparation = 1.20

price_pen = number_package_pen * 5.80
price_marker = number_package_marker * 7.20
price_preparation = preparation * 1.20
price_for_all_materials = price_pen + price_marker + price_preparation
discounted_price = price_for_all_materials - (price_for_all_materials * percentage_reduction)

print(discounted_price)