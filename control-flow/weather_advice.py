Weather_Input = input(" What's the weather like today? (sunny/rainy/cold): ")

if Weather_Input == str("sunny"):
    print(" Wear a t-shirt and sunglasses.")
    
elif Weather_Input == str("rainy"):
    print("Don't forget your umbrella and a raincoat.")

elif Weather_Input == str("cold"):
    print("Make sure to wear a warm coat and a scarf.")
else:
    print(" Sorry, I don't have recommendations for this weather.")