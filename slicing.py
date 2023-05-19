planet1 = "Closest of Sun"
print("planet1")

# Slicing the words from +ve.
print(planet1[0])
print(planet1[1])
print(planet1[2])

# Slicing the words from -ve.
print(planet1[-1])
print(planet1[-2])
print(planet1[-3])

# Slicing a string, get a substring from a string
print(planet1[0:5])
print(planet1[:])
print(planet1[:7])
print(planet1[11:])

# Slicing tuple
devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")
print(devops[0])
print(devops[1])
print(devops[2])

print(devops[-1])

print(devops[2:5])
print(devops[2:5] [0])
print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-1])

# Slicing List
devops = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]
print(devops[0])
print(devops[1])
print(devops[2])

print(devops[-1])

print(devops[2:5])
print(devops[2:5] [0])
print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-1])


# Dictionary Example
skills = {"devops": ("AWS", "Jenkins", "Python", "Ansible"), "development": ["java", "NodeJS", ".Net"]}

print(skills)
print(skills["devops"])
print(skills["development"])

print(skills["devops"][-1])
print(skills["devops"][-1][:3])
