from pyscript import document, display

def nameChecker (e):

# Variables for the names that are considered true
    pangalan = ["Ysabel Valerio", "Joy Manawari", "Hector Samala", "Emman Azarcon", "Anthony Cruz"]

    fname = (document.getElementById("fname").value)
    lname = (document.getElementById("lname").value)

# Variable using concatenation for the name the user will input to appear
    name = fname + " " + lname

# Variable to determine whether the user's name is listed or not (true or false)
    full_name = (name in pangalan)

# First statement = 0 = False | Second Statement = 1 = True
    remark = (f'Sorry, {name}, your name is not on the list.', f'Congrats! {name}, YOU ARE a member of the Rainbow Catering Club!')

    document.getElementById("output1").innerHTML = remark[full_name]

    