# test_python.py
import sys
print(f"✅ Python version: {sys.version}")

# Test basic data analysis
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(f"✅ Average of {numbers} is: {average}")

# Test if pip packages work
try:
    import pip
    print(f"✅ pip is working!")
except:
    print("❌ pip issue")

print("\n🎉 PYTHON IS WORKING PERFECTLY!")