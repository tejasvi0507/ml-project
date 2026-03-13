# Tuple storing subject marks
marks = (78, 85, 90, 88, 76)

print("Marks in each subject:", marks)

# Calculate total marks
total = sum(marks)
print("Total Marks:", total)

# Calculate average
average = total / len(marks)
print("Average Marks:", average)

# Find highest and lowest marks
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

# Check if a mark exists
if 90 in marks:
    print("Student scored 90 in one subject")
else:
    print("90 not found")

# Loop through tuple
print("Marks subject-wise:")
for i in range(len(marks)):
    print("Subject", i+1, ":", marks[i])