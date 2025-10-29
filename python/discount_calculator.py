def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying discount if discount_percent >= 20.
    
    Args:
        price (float): Original price of the item
        discount_percent (float): Discount percentage
    
    Returns:
        float: Final price after discount, or original price if discount < 20%
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Print result
    if discount_percentage >= 20:
        print(f"Discount of {discount_percentage}% applied!")
        print(f"Original price: ${original_price:.2f}")
        print(f"Final price: ${final_price:.2f}")
    else:
        print(f"Discount of {discount_percentage}% is below 20%, no discount applied.")
        print(f"Price remains: ${final_price:.2f}")
        
except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
    