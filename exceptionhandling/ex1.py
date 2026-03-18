try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("❌ Invalid input! Please enter a number.")

except ZeroDivisionError:
    print("❌ Cannot divide by zero!")

else:
    print("✅ Result is:", result)

finally:
    print("🔚 This block always executes.")

