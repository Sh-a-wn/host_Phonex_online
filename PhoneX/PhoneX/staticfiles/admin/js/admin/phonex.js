<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Glassmorphism Login Form</title>
    <style>
    form {
        color: #fff;
        font-size: 2.3em;
        justify-content: center;
        display: flex;
        margin: 60px;
        font-weight: bold;
        cursor: pointer;
        transition: .5s ease-in-out;
        background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
            text-align: center;
    }
    </style>
</head>
<body>
    <section class="container">
        <div class="register-forget">
            <div class="circle circle-one"></div>
            <div class="form-container">
                <img src="https://raw.githubusercontent.com/hicodersofficial/glassmorphism-login-form/master/assets/illustration.png" alt="illustration" class="illustration" />
                <h1 class="opacity">REGISTER</h1>
                <form>
                    <input type="text" placeholder="FIRST NAME" />
                    <input type="text" placeholder ="LASTNAME"/>
                     <input type = "date" placeholder="ENTER YOUR DATE OF BIRTH"/>
                     <input type = "email" placeholder="ENTER YOUR EMAIL ADDRESS"/>

                      <input type="password" placeholder="PASSWORD" />
                      <input type="confirm password" placeholder="RE-ENTER YOUR PASSWORD"/>
                    <button class="opacity">SUBMIT</button>
                </form>
                <div class="register-forget opacity">
                    <a href="register.html" id="register-link">REGISTER</a>
                    <a href="#" id="forgot-password-link">FORGOT PASSWORD</a>
                </div>
            </div>
            <div class="circle circle-two"></div>
        </div>
        <div class="theme-btn-container"></div>
    </section>

    <script>
        const themes = [
            /* Array of theme objects */
        ];

        const setTheme = (theme) => {
            /* Function to set theme */
        };

        const displayThemeButtons = () => {
            /* Function to display theme buttons */
        };

        displayThemeButtons();

        // Automatically redirect to register page after 5 seconds
        setTimeout(() => {
            window.location.href = 'register.html';
        }, 5000);

        // Automatically redirect to forgot password page after 10 seconds
        setTimeout(() => {
            window.location.href = 'forgot_password.html';
        }, 10000);

        // Register link click event
        document.getElementById('register-link').addEventListener('click', (event) => {
            // Redirect to register page
            window.location.href = event.target.href;
            event.preventDefault(); // Prevent default link behavior
        });

        // Forgot password link click event
        document.getElementById('forgot-password-link').addEventListener('click', (event) => {
            // Redirect to forgot password page
            window.location.href = event.target.href;
            event.preventDefault(); // Prevent default link behavior
        });
    </script>
</body>
</html>

