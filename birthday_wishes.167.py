#Birthday wishes
#Demonstrates keyword arguments and default parameter values
#pg 167

#positional parameters
def birthday1(name, age):
    print("Happy birthday", name, "!", " I hear you're", age, "today.\n")

#parameters with default values
def birthday2(name = "Gandolf", age = 1):
    print("Happy birthday", name, "!", " I hear you're", age, "today.\n")

birthday1("Gandolf", 1)
birthday1(1, "Gandolf")
birthday1(name="Gandolf", age=1)
birthday1(age=1, name="Gandolf")

birthday2()
birthday2(age=2)
birthday2(name="Trondor")
birthday2(name="Throndor", age=2)
birthday2(age=2, name="Throndor")

