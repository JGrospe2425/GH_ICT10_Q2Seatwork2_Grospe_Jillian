from pyscript import document, display

def calculate_grades(e):
    # Get student name
    firstname = document.getElementById('firstname').value
    lastname = document.getElementById('lastname').value
    completename = firstname + " " + lastname

    # list and tuple
    subjects = ["English", "Filipino", "Social Studies", "Science", "Math", "PE"]
    units = (5, 3, 3, 5, 5, 1)

    # Get grades
    englishgrade = float(document.getElementById('English').value)
    filipinograde = float(document.getElementById('Filipino').value)
    socialstudiesgrade = float(document.getElementById('SocialStudies').value)
    sciencegrade = float(document.getElementById('Science').value)
    mathgrade = float(document.getElementById('Math').value)
    PEgrade = float(document.getElementById('PE').value)

    # Weighted calculations
    englishaverage = englishgrade * 5
    filipinoaverage = filipinograde * 3
    socialstudiesaverage = socialstudiesgrade * 3
    scienceaverage = sciencegrade * 5
    mathaverage = mathgrade * 5
    PEaverage = PEgrade * 1 
 
    # Final average
    Finalaverage = (englishaverage + filipinoaverage + socialstudiesaverage + scienceaverage + mathaverage + PEaverage) / sum(units)

    # Display results
    display(f"Name: {completename}", target="information")

    display(f"English: {englishgrade}", target="information")
    display(f"Filipino: {filipinograde}", target="information")
    display(f"Social Studies: {socialstudiesgrade}", target="information")
    display(f"Science: {sciencegrade}", target="information")
    display(f"Math: {mathgrade}", target="information")
    display(f"PE: {PEgrade}", target="information")

    display(f"General Weighted Average: {Finalaverage:.2f}", target="Average")
