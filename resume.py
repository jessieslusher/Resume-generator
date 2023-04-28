from docxtpl import DocxTemplate
import os
import sys

# Prompt user to choose template type
while True:
    try:
        template_type = int(input("Enter '1' to use a pre-built template, or '2' to use a custom template: "))
        if template_type not in [1, 2]:
            print('Invalid option. Please enter either 1 or 2.')
            continue
        break
    except ValueError:
        print('Invalid input. Please enter a number.')

if template_type == 1:
    # Use pre-built template
    doc = DocxTemplate('pre-built-template.docx')

else:
    # Use custom template
    while True:
        try:
            custom_template = input('Enter the file path to your custom template: ')
            if not os.path.exists(custom_template):
                print('The file path does not exist. Please try again.')
                continue
            doc = DocxTemplate(custom_template)
            break
        except Exception as e:
            print(f'Error: {e}. Please try again or enter "q" to quit.')
            if input().lower() == 'q':
                sys.exit()

# Add header with name and contact information
name = input('Enter your name: ')
phone_number = input('Enter your phone number: ')
email = input('Enter your email: ')
context = {'name': name, 'phone_number': phone_number, 'email': email}
doc.render(context)

# Add profile picture
while True:
    try:
        profile_picture = input('Enter the file path to your profile picture: ')
        if not os.path.exists(profile_picture):
            print("The file path does not exist. Please try again.")
            continue
        context = {'profile_picture': profile_picture}
        doc.render(context)
        break
    except Exception as e:
        print(f'Error: {e}. Please try again or enter "q" to quit.')
        if input().lower() == 'q':
            sys.exit()

# Add summary section
summary = input('Enter a summary of your skills and experience: ')
context = {'summary': summary}
doc.render(context)

# Add education section
education = input('Enter your education details: ')
context = {'education': education}
doc.render(context)

# Add experience section
experience = input('Enter your work experience details: ')
context = {'experience': experience}
doc.render(context)

# Add skills section
skills = input('Enter your skills: ')
skill_list = skills.split(',')
context = {'skills': skill_list}
doc.render(context)

# Add awards section
awards = input('Enter your awards: ')
context = {'awards': awards}
doc.render(context)

# Add certifications section
certifications = input('Enter your certifications: ')
context = {'certifications': certifications}
doc.render(context)

# Add publications section
publications = input('Enter your publications: ')
context = {'publications': publications}
doc.render(context)

# Save the resume as a Word document
while True:
    try:
        save_path = input('Enter the file path to save your resume: ')
        doc.save(save_path)
        print('Your resume has been saved.')
        break
    except Exception as e:
        print(f'Error: {e}. Please try again or enter "q" to quit.')
        if input().lower() == 'q':
            sys.exit()
