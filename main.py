###### ------------------ MAIN FILE, PRODUCES HTML AND PDFS ------------------ ######
import debt_tracker as dt

print("Beginning Main...")

basic_debt_html = f"""
<div class="container">
<div class="content">
    <h2>Current Debt</h2>
    <p>The gross national debt is currently <strong>${dt.current_debt_rounded:,} trillion</strong>. This equates to:</p>
    <ul>
        <li><strong>${dt.debt_per_person:,}</strong> per person</li>
        <li><strong>${dt.debt_per_household:,}</strong> per household</li>
        <li><strong>${dt.debt_per_child:,}</strong> per child</li>
    </ul>

    <h2>Debt Accumulation under President Biden</h2>
    <p>When President Biden took office total gross debt was <strong>${dt.biden_start_debt_rounded:,} trillion</strong>, meaning he has increased the national debt by <strong>${dt.biden_debt_rounded:,} trillion</strong>. This equates to:</p>
    <ul>
        <li><strong>${dt.biden_debt_per_person:,}</strong> more debt per person</li>
        <li><strong>${dt.biden_debt_per_household:,}</strong> more debt per household</li>
        <li><strong>${dt.biden_debt_per_child:,}</strong> more debt per child</li>
    </ul>
    <p>The rate of debt accumulation during the Biden Administration has equaled:</p>
    <ul>
        <li><strong>${dt.biden_debt_per_day_rounded:,} billion</strong> in new debt per day</li>
        <li><strong>${dt.biden_debt_per_hour:,} million</strong> in new debt per hour</li>
        <li><strong>${dt.biden_debt_per_min:,} million</strong> in new debt per minute</li>
        <li><strong>${dt.biden_debt_per_sec:,}</strong> in new debt per second</li>
    </ul>

    <h2>Debt Accumulation in Past Year</h2>
    <p>The debt one year ago was <strong>${dt.debt_year_ago_rounded:,} trillion</strong>, meaning that the debt has increased by <strong>${dt.debt_increase_from_year_ago_rounded:,} trillion</strong> over the past 12 months. This rate of increase equates to:</p>
    <ul>
        <li><strong>${dt.last_year_debt_per_day_rounded:,} billion</strong> in new debt per day</li>
        <li><strong>${dt.last_year_debt_per_hour:,} million</strong> in new debt per hour</li>
        <li><strong>${dt.last_year_debt_per_min:,} million</strong> in new debt per minute</li>
        <li><strong>${dt.last_year_debt_per_sec:,}</strong> in new debt per second</li>
    </ul>
</div>
</div>
"""


#### ---- FINAL HTML ---- ####
html = f"""
<!DOCTYPE html>
<html>
<head>
    <center>
        <img src="../inputs/HBR_Logo_Primary.png" width="500" align = "middle">
    </center> 
    <title>Debt Tracker</title>
    <style>
        body {{
            font-family: 'Montserrat', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f7f7f7;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        .header {{
            background-color: #004647;
            color: white;
            padding: 20px;
            text-align: center;
        }}
        .content {{
            background-color: white;
            padding: 20px;
            margin-top: 20px;
        }}
        .content h2 {{
            color: #004647;
        }}
        .content p {{
            color: #333;
        }}
        .content img {{
            width: 100%;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
<br> </br>
<div class="header">
    <h1>Debt Tracker</h1>
</div>
{basic_debt_html}
    
</body>
</html>
"""

html_file_name = f"output/Debt Tracker {dt.today}.html"
with open(html_file_name, "w", encoding="utf-8") as file:
    file.write(html)

print("Main Complete!")