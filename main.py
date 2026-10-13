from pyscript import document, display
# Use document if there is a form

def nameChecker (e):

    fname = ["Ysabel", "Joy", "Hector", "Emman", "Anthony"]

    lname = ["Valerio", "Manawari", "Samala", "Azarcon", "Cruz"]

    name1 = str(document.getElementById("fname").value)
    name2 = str(document.getElementById("lname").value)

    full_name = name1 + name2

    remark = display(f'Sorry, {full_name}, your name is not on the list.', f'Congrats! {full_name}, your a member of the Rainbow Catering Club!', target="nameChecker")
    # First statement = 0 = False | Second Statement = 1 = True

    document.getElementById("output1").innerHTML = message[full_name]