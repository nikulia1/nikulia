for row in select_rezult:
    print(row)
cursor.execute('UPDATE students SET Device =''Nika'' WHERE age >19)
print(cursor.rowcount)
conecc.commit()
ID = 18
Age = 14
onlineclasstime = 4
Device = "lenovo"
SelfstudyHour = 4
FitnesTime = "4"
sleep = "9"
SocialMedia = "6"
SocialMediaPlatform = "instagram"
conecc.execute(f"INSERT INTO students ( age, onlineclaasstime, Device, SelfstudyHour, FitnessTime, Sleep, Socialmedia, SocalMediaPlatform) VALUES (?,?,?,?,?,?,?,?)",(age, onlineclaasstime, Device, SelfstudyHour, FitnessTime, Sleep, Socialmedia, SocalMediaPlatform))


