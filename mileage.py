print("How many kilometers did you travel today?")
kms = float(input())
conversion = 1.60934
print(f"Ok, you said {kms}!")
miles = round(float(kms)/conversion, 2)
print(f"That is {miles} miles! Nice work!")
print(f"You {kms}km ride is {miles}mi")