from pyscript import document, display
# Use document if there is a form

def nameChecker (e):

# Variables for the names that are considered true
    pangalan = ["Ysabel Valerio", "Joy Manawari", "Hector Samala", "Emman Azarcon", "Anthony Cruz"]

    fname = (document.getElementById("fname").value)
    lname = (document.getElementById("lname").value)

    name = fname + lname

# Variable to determine whether the user's name is listed or not (true or false) with the use of concatination
    full_name = (fname + lname) in pangalan

# First statement = 0 = False | Second Statement = 1 = True
    remark = (f'Sorry, {name}, your name is not on the list.', f'Congrats! {name}, you are a member of the Rainbow Catering Club!')

    document.getElementById("output1").innerHTML = remark[full_name]

    