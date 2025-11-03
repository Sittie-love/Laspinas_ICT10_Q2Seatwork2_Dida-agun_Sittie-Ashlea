from pyscript import display, document

def calculate_gwa(e):
    first_name = document.getElementById("firstName").value
    last_name = document.getElementById("lastName").value
    name = f"{first_name} {last_name}"

    science = float(document.getElementById("science").value or 0)
    math = float(document.getElementById("math").value or 0)
    english = float(document.getElementById("english").value or 0)
    filipino = float(document.getElementById("filipino").value or 0)
    ict = float(document.getElementById("ict").value or 0)
    pe = float(document.getElementById("pe").value or 0)

    grades = {
        "Science": science,
        "Math": math,
        "English": english,
        "Filipino": filipino,
        "ICT": ict,
        "PE": pe
    }

    gwa = round(sum(grades.values()) / len(grades), 2)

    document.getElementById("result_name").innerHTML = f"<b>Name:</b> {name}"
    document.getElementById("result_grades").innerHTML = (
        "<b>Grades:</b><br>" + "<br>".join(f"{s}: {g}" for s, g in grades.items())
    )
    document.getElementById("result_gwa").innerHTML = f"<b>GWA:</b> <b>{gwa}</b>"
