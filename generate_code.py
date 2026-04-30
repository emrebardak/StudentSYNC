import pandas as pd

df = pd.read_excel('docs/Computer_Engineering_Course_Schedule.xlsx')
lines = []
c_idx = 1
course_vars = []
for idx, row in df.iterrows():
    code = str(row['Course Code']).strip()
    name = str(row['Course Name']).strip()
    if code != '-' and code.upper() != 'NAN' and code:
        code = code.replace(' ', '')
        var_name = f'c{c_idx}'
        lines.append(f'                CourseCatalogEntity {var_name} = new CourseCatalogEntity();')
        lines.append(f'                {var_name}.setCode("{code}");')
        lines.append(f'                {var_name}.setName("{name}");')
        lines.append(f'                {var_name}.setDifficultyRating(4.0);')
        lines.append(f'                {var_name}.setRatingCount(100);\n')
        course_vars.append(var_name)
        c_idx += 1

print('\n'.join(lines))
print(f'                courseRepository.saveAll(List.of({", ".join(course_vars)}));')
