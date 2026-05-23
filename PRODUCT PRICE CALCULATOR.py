# Product Price Calculator with Discount and GST

print("========== Product Price Calculator ==========\n")

# Taking inputs
product_price = float(input("Enter product price: ₹"))
discount_percent = float(input("Enter discount percentage: "))
gst_percent = float(input("Enter GST percentage: "))

# Calculating discount amount
discount_amount = (product_price * discount_percent) / 100

# Price after discount
price_after_discount = product_price - discount_amount

# Calculating GST amount
gst_amount = (price_after_discount * gst_percent) / 100

# Final price after adding GST
final_price = price_after_discount + gst_amount

# Displaying formatted output
print("\n======================================")
print("           BILL SUMMARY")
print("======================================")
print(f"Original Price      : ₹{product_price:.2f}")
print(f"Discount Percentage : {discount_percent}%")
print(f"Discount Amount     : ₹{discount_amount:.2f}")
print("--------------------------------------")
print(f"Price After Discount: ₹{price_after_discount:.2f}")
print(f"GST Percentage      : {gst_percent}%")
print(f"GST Amount          : ₹{gst_amount:.2f}")
print("--------------------------------------")
print(f"Final Price         : ₹{final_price:.2f}")
print("======================================")

print("\nThank you for using the calculator!")