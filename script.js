const countryStateCity = {
    IN: {
        Telangana: ["Hyderabad", "Warangal"],
        Karnataka: ["Bangalore", "Mysore"]
    },
    US: {
        Texas: ["Dallas", "Austin"],
        California: ["Los Angeles", "San Jose"]
    }
};

const form = document.getElementById("regForm");
const submitBtn = document.getElementById("submitBtn");

const fname = document.getElementById("fname");
const lname = document.getElementById("lname");
const email = document.getElementById("email");
const phone = document.getElementById("phone");
const password = document.getElementById("password");
const cpassword = document.getElementById("cpassword");
const terms = document.getElementById("terms");
const country = document.getElementById("country");
const state = document.getElementById("state");
const city = document.getElementById("city");

const fnameErr = document.getElementById("fnameErr");
const lnameErr = document.getElementById("lnameErr");
const emailErr = document.getElementById("emailErr");
const phoneErr = document.getElementById("phoneErr");
const genderErr = document.getElementById("genderErr");
const passErr = document.getElementById("passErr");
const termsErr = document.getElementById("termsErr");
const topError = document.getElementById("topError");
const successMsg = document.getElementById("successMsg");
const strength = document.getElementById("strength");


function loadStates() {
    state.innerHTML = "<option value=''>Select State</option>";
    city.innerHTML = "<option value=''>Select City</option>";
    if (country.value) {
        Object.keys(countryStateCity[country.value]).forEach(s => {
            state.innerHTML += `<option value="${s}">${s}</option>`;
        });
    }
}

function loadCities() {
    city.innerHTML = "<option value=''>Select City</option>";
    if (state.value) {
        countryStateCity[country.value][state.value].forEach(c => {
            city.innerHTML += `<option value="${c}">${c}</option>`;
        });
    }
}

function validateForm() {
    let valid = true;
    topError.innerText = "";

    if (fname.value === "") { setErr(fname, fnameErr, "First name required"); valid = false; }
    else clearErr(fname, fnameErr);

    if (lname.value === "") { setErr(lname, lnameErr, "Last name required"); valid = false; }
    else clearErr(lname, lnameErr);

    if (!email.value.includes("@") || email.value.includes("tempmail")) {
        setErr(email, emailErr, "Invalid email"); valid = false;
    } else clearErr(email, emailErr);

    if (country.value && !phone.value.startsWith("+")) {
        setErr(phone, phoneErr, "Phone must start with country code"); valid = false;
    } else clearErr(phone, phoneErr);

    let genderChecked = document.querySelectorAll('input[name="gender"]:checked');
    if (genderChecked.length === 0) {
        genderErr.innerText = "Select gender"; valid = false;
    } else genderErr.innerText = "";

    if (password.value.length < 6) {
        strength.innerText = "Weak";
        valid = false;
    } else if (password.value.length < 10) {
        strength.innerText = "Medium";
    } else strength.innerText = "Strong";

    if (password.value !== cpassword.value) {
        passErr.innerText = "Passwords do not match"; valid = false;
    } else passErr.innerText = "";

    if (!terms.checked) {
        termsErr.innerText = "Accept terms"; valid = false;
    } else termsErr.innerText = "";

    submitBtn.disabled = !valid;
}

function setErr(field, errField, msg) {
    field.classList.add("invalid");
    errField.innerText = msg;
    topError.innerText = "Please fix errors before submitting";
}

function clearErr(field, errField) {
    field.classList.remove("invalid");
    errField.innerText = "";
}

function submitForm(e) {
    e.preventDefault();

    let users = JSON.parse(localStorage.getItem("users")) || [];
    let existingUser = users.find(u => u.email === email.value);

    if (existingUser) {
        successMsg.style.color = "red";
        successMsg.innerText = "User already registered with this email.";
        return;
    }

    users.push({ email: email.value });
    localStorage.setItem("users", JSON.stringify(users));

    successMsg.style.color = "green";
    successMsg.innerText = "Registration Successful! Your profile has been submitted successfully.";
    form.reset();
    submitBtn.disabled = true;
}
