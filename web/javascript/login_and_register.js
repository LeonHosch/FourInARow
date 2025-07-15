function pre_login() {
    webpage.innerHTML = `
        <button class="start_button" id="login">Log in</button>
        <button class="start_button" id="register">Register</button>
    `;
    login_and_register_buttons();
}

function login() {
    webpage.innerHTML = `
        <button class="home_button"></button>
        <input class="input_field" id=username type="text" placeholder="Username">
        <input class="input_field" id=password type="password" placeholder="Password">
        <button class="start_button" id="submit_login">Submit</button>
    `;
    home_button();
    submit_login_button();
}

function register() {
    webpage.innerHTML = `
        <button class="home_button"></button>
        <input class="input_field" type="text" placeholder="Username">
        <input class="input_field" type="password" placeholder="Password">
        <input class="input_field" type="password" placeholder="Repeat Password">
        <button class="start_button" id="submit_register">Submit</button>
    `;
    home_button();
    submit_register_button();
}

function login_and_register_buttons() {
    const loginButton = document.getElementById('login');
    const registerButton = document.getElementById('register');
    loginButton.addEventListener('click', () => {
        login();
    });
    registerButton.addEventListener('click', () => {
        register();
    });
}

function home_button() {
    const homeButton = document.querySelector('.home_button');
    homeButton.addEventListener('click', pre_login);
}

function submit_login_button() {
    const submitButton = document.getElementById("submit_login");
    submitButton.addEventListener('click', check_login);
}

function submit_register_button() {
    const register_button = document.getElementById("submit_register");
    register_button.addEventListener("click", check_register);
}

function check_login() {
    const real_password = "meinpasswort"
    const real_name = "meinname"
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    if (!usernameInput || !passwordInput) {
        alert("Register clicked, no login check.");
        return;
    }
    const username = usernameInput.value;
    const password = passwordInput.value;
    if (username === real_name && password === real_password) {
        main_menu();
    }   else {
        alert("Login failed");
        main_menu();
    }
}

function check_register() {
    alert("Registered your account");
    pre_login();
}

const webpage = document.getElementById("webpage")
pre_login();
