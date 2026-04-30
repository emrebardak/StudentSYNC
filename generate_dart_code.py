import pandas as pd

df = pd.read_excel('docs/Computer_Engineering_Course_Schedule.xlsx')
lines = []
for idx, row in df.iterrows():
    code = str(row['Course Code']).strip()
    name = str(row['Course Name']).strip()
    if code != '-' and code.upper() != 'NAN' and code:
        code_clean = code.replace(' ', '')
        id_clean = code_clean.lower()
        lines.append(f"    RegistrationCourse(id: '{id_clean}', code: '{code_clean}', name: '{name}'),")

print('\n'.join(lines))
