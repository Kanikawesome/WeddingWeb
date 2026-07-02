import os

files = [f for f in os.listdir('.') if f.endswith('.html') or f.endswith('.js')]

for file in files:
    if file == 'index.html':
        continue # we will handle this separately
    with open(file, 'r') as f:
        content = f.read()
    
    if 'index.html' in content:
        new_content = content.replace('index.html', 'home.html')
        with open(file, 'w') as f:
            f.write(new_content)

print("Updated links.")
