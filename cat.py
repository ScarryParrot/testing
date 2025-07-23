import subprocess

# Step 1: Run the Python command (or read the /etc/passwd file in this case)
output = open('/etc/passwd').read()

# Step 2: Wrap the output in HTML
html_content = f"""
<html>
  <head><meta charset="UTF-8"></head>
  <body>
    <h1>Contents of /etc/passwd</h1>
    <pre><code>{output}</code></pre>
  </body>
</html>
"""

# Step 3: Save the HTML content to a file
with open("cat.html", "w") as file:
    file.write(html_content)

# Step 4: Convert the HTML to PDF using wkhtmltopdf
subprocess.run(["wkhtmltopdf", "cat.html", "output.pdf"])
