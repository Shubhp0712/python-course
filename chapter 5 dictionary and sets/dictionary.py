name = {}  # empty dictionary
contact = {
    "Shubh" : 6352765272,
    "Rahul" : 6352765273,
    "Rohan" : 6352765274,
    "Raj" : 6352765275,
    "Ravi" : 6352765276,
    6352765272 :"Shubh" # key can be any immutable data type.here 1st and last entry are not same.because 1st is string and last is integer key value.
}

print(contact)

print(contact["Shubh"])

print(contact[6352765272])

contact["Shubh"] = 6352765277 # updating the value of key Shubh. Because dictionary is mutable.

print(contact)