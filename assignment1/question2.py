def two():
    # Question 2
    # The cover price of a book is $25, but bookstores get a 10% discount. Shipping costs $2 for the first five copies
    # and 2.75 cents for all rest of copies. Write a Python program to show what is the total wholesale cost for
    # 40 copies display the result.

    # given in question
    number_of_copies = 40
    actual_price = 25
    discount = 0.10

    # calculating discounted price for each book
    discounted_price = (1 - discount) * actual_price

    # calculating total book price after discounting
    total_book_price = discounted_price * 40

    # calculating shipping price
    shipping_cost_first5 = 2
    shipping_cost_rest = 2.75

    # to calculate total shipping cost
    total_shipping_cost = (shipping_cost_first5 * 5) + ((number_of_copies - 5) * shipping_cost_rest)

    # to calculate total wholesale cost
    wholesale_cost = total_book_price + total_shipping_cost

    # printing the total wholesale cost
    print("Total whole sale cost: $", wholesale_cost)