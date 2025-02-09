<script setup>
import { onMounted, ref } from 'vue';

const loginServerURL = 'http://localhost:8000/login';
const registerServerURL = 'http://localhost:8000/register';

let status = false;

import { postData, checkInput, swapClasses, styleRemover, clearInputs } from './ts/helpers';

let logInCard = ref();
let signUpCard = ref();
let inputNameSignUp = ref()
let inputEmailSignUp = ref()
let inputPasswordSignUp = ref()
let inputEmailLogIn = ref()
let inputPasswordLogIn = ref()
let submitButtonLogIn = ref()
let submitButtonSignUp = ref()
let hiddenText = ref()
let hiddenText2 = ref()

function rotateForm() {
  logInCard.value.classList.toggle("opacity-0")
  signUpCard.value.classList.toggle("opacity-0")
}


onMounted(() => {
  
  let script = document.createElement("script");
  script.src = "https://accounts.google.com/gsi/client";
  script.async = true;
  script.defer = true;
  document.head.appendChild(script);




  submitButtonLogIn.onclick = function () {

    // ? Проверка Email в Лог-Ин
    checkInput(inputEmailLogIn)

    // Проверка Пароля в Лог-Ин
    checkInput(inputPasswordLogIn)

    // Добавляем надпись Correct/Uncorrect
    if (inputPasswordLogIn.value.length >= 8 && inputPasswordLogIn.value != "" && inputEmailLogIn.value.length >= 8 && inputEmailLogIn.value != "") {
      hiddenText.classList.add("green")
      hiddenText.innerText = 'Loging you in, please wait...';
      status = true
    }
    else {
      hiddenText.classList.remove("green")
      hiddenText.classList.add("red");
      hiddenText.innerText = 'Uncorrect!';
    }


    let logInData = {
      "user_email": inputEmailLogIn.value,
      "password": inputPasswordLogIn.value
    };


    if (status) {
      let promiseForResult = postData(loginServerURL, logInData);
      // console.log("Data has been send");
      submitButtonLogIn.disabled = true

      promiseForResult.then((data) => {
        if (data.isLoginSuccess == false) {
          hiddenText.innerText = 'You aren`t registered';

          swapClasses(hiddenText, "green", "red")
          styleRemover(inputEmailLogIn)
          styleRemover(inputPasswordLogIn)

          clearInputs([inputEmailLogIn, inputPasswordLogIn])

          submitButtonLogIn.disabled = false
          status = false
        }
      })
    }
    else {
      console.log("Error sending data");
    }
  };




  submitButtonSignUp.onclick = function () {

    // Проверка Имя в Sign-Up
    checkInput(inputNameSignUp)

    // ? Проверка Email в Sign-Up
    checkInput(inputEmailSignUp)


    // Проверка Пароля в Sign-Up
    checkInput(inputPasswordSignUp)

    // Добавляем надпись Correct/Uncorrect
    if (inputPasswordSignUp.value.length >= 8 && inputPasswordSignUp.value != "" && inputEmailSignUp.value.length >= 8 && inputEmailSignUp.value != "" && inputNameSignUp.value.length >= 8 && inputNameSignUp.value != "") {
      hiddenText2.classList.add("green")
      hiddenText2.innerText = 'Correct!';
    }
    else {
      hiddenText2.classList.remove("green")
      hiddenText2.classList.add("red");
      hiddenText2.innerText = 'Uncorrect!';
    }

    let signUpData = {
      "user_email": "string",
      "password": "string",
      "full_name": "string"
    };

    signUpData.user_email = inputEmailSignUp.value;
    signUpData.password = inputPasswordSignUp.value;
    signUpData.full_name = inputNameSignUp.value;
    // console.log(signUpValue);


    postData(registerServerURL, signUpData);



  }



});




</script>

<template>
  <div class="container content2">


    <!-- Switcher -->
    <section class="center-position pb-5">
      <div class="row">
        <div class="center-position pb-3">
          <span><strong>LOG IN</strong></span> <span class="micro-padding"><strong>SIGN UP</strong></span>
        </div>
        <div class="form-check form-switch center-position">
          <input @click="rotateForm" class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
        </div>
      </div>
    </section>

    <!-- Sign Up -->
    <section ref="signUpCard" class="center-position sign-up-form opacity-0">
      <div class="container block-form text-center">
        <div class="row content">
          <h4 class="pb-4 log-in-font-size"><strong>Sign Up</strong></h4>
          <!-- Your Full Name -->
          <div class="pb-2 position-relative">
            <input ref="inputNameSignUp" type="text" name="logemail" class="form-style inputs" placeholder="Your Name"
              id="logemail" autocomplete="off">
            <i class="input-icon uil uil-user"></i>
          </div>
          <!-- Your Email -->
          <div class="pb-2 position-relative">
            <input ref="inputEmailSignUp" type="email" name="logemail" class="form-style inputs"
              placeholder="Your Email" id="logemail2" autocomplete="off">
            <i class="input-icon uil uil-at"></i>
          </div>
          <!-- Your Password -->
          <div class="pb-2 position-relative">
            <input ref="inputPasswordSignUp" type="password" name="logpass" class="form-style inputs"
              placeholder="Your Password" id="logpass2" autocomplete="off">
            <i class="input-icon uil uil-lock-alt top-55"></i>
          </div>
          <div ref="hiddenText2" class="mb-3"></div>
          <!-- Submit -->
          <div class="pb-2">
            <button ref="submitButtonSignUp" class="button-submit-shiny button-submit"><strong>Submit</strong></button>
          </div>
          <div class="g_id_signin button_google" data-type="standard" data-size="large" data-theme="filled_black"
            data-text="sign_in_with" data-shape="circle" data-logo_alignment="right">
          </div>
        </div>
      </div>
    </section>

    <!-- Log In Block -->
    <section ref="logInCard" class="center-position log-in-form">
      <div class="container block-form text-center">
        <div class="row content">
          <h4 class="pb-4 log-in-font-size"><strong>Log In</strong></h4>
          <!-- Your Email -->
          <div class="pb-2 position-relative">
            <input ref="inputEmailLogIn" type="email" name="logemail" class="form-style inputs" placeholder="Your Email"
              id="logemail1" autocomplete="off">
            <i class="input-icon uil uil-at"></i>
          </div>
          <!-- Your Password -->
          <div class="pb-2 position-relative">
            <input ref="inputPasswordLogIn" type="password" name="logpass" class="form-style inputs"
              placeholder="Your Password" id="logpass1" autocomplete="off">
            <i class="input-icon uil uil-lock-alt"></i>
          </div>
          <div ref="hiddenText" class="mb-3"></div>
          <!-- Submit -->
          <div class="pb-2">
            <button ref="submitButtonLogIn" class="button-submit-shiny button-submit"><strong>Submit</strong></button>
          </div>
          <!-- Forgot your password? -->
          <div class="forgot-password">Forgot your password?</div>


          <div class="g_id_signin button_google" data-type="standard" data-size="large" data-theme="filled_black"
            data-text="sign_in_with" data-shape="circle" data-logo_alignment="right">
          </div>
        </div>
      </div>
    </section>
  </div>

</template>

<style scoped>
.button_google {
  height: 40px;
  position: relative;
  z-index: 1001;
}

.center-position {
  display: flex;
  justify-content: center;
  align-items: center;
}

.log-in-font-size {
  font-size: 21px;
}

.content {
  padding: 40px 25px 40px 25px;
}

.content2 {
  padding: 200px 20px 60px 20px;
}

.micro-padding {
  padding-left: 30px;
}

.inputs {
  font-size: 14px;
  background-color: #1f2029;
  width: 100%;
  height: 40px;
  border-radius: 5px;
  border: none;
  text-indent: 14%;
  color: #c4c3ca;
}

.block-form {
  max-width: 30%;
  /* height: 320px; */
  background: #2a2b38;
  background-image: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/1462889/pat.svg');
  border-radius: 5px;
  background-position: bottom center;
  background-repeat: no-repeat;
  background-size: 300%;
}

.forgot-password {
  margin: 0 0 1rem 0;
  font-size: 12px;
  transition: 1s;
}

.forgot-password:hover {
  color: #ffeba7;
  cursor: pointer;
}

.button-submit {
  box-shadow: 0px 0px 21px 0px #ffeba7;
  background-color: #ffeba7;
  border: none;
  border-radius: 3px;
  padding: 5px 25px 5px 25px;
  text-transform: uppercase;
  font-size: 13px;
  color: rgb(33, 60, 133);
  transition: 0.6s;
}

.button-submit:hover {
  background-color: rgb(33, 60, 133);
  box-shadow: 0px 0px 21px 0px rgb(33, 60, 133);
  color: #ffeba7;
}

.uil-at:before {
  color: #ffeba7;
  position: absolute;
  left: 7%;
  bottom: 40%;
}

.uil-user:before {
  color: #ffeba7;
  position: absolute;
  left: 7%;
  bottom: 39%;
}

.uil-lock-alt:before {
  color: #ffeba7;
  position: absolute;
  left: 7%;
  bottom: 40%;
}

.top-55:before {
  bottom: 40%;
}

.opacity-0 {
  opacity: 0;
  height: 0;
  position: relative;
  z-index: -1;
}

.form-check-input:checked {
  background-color: #ffeba7;
  border-color: #1f2029;
}

.form-check-input {
  background-color: #ffeba7;
  border-color: #1f2029;
}

.form-check-input {
  width: 3.5rem;
  height: 1.5rem;
}

.form-switch .form-check-input {
  --bs-form-switch-bg: url(./assets/ArrowUpLeft.svg);
}

.form-switch .form-check-input:checked {
  --bs-form-switch-bg: url(./assets/ArrowUpRight.svg);
}

.red-border {
  color: rgba(255, 0, 0, 0.7);
  border: 2px solid rgba(255, 0, 0, 0.7);
}

.red {
  color: rgba(255, 0, 0, 0.7);
}

.green-border {
  color: rgba(0, 128, 0, 0.7);
  border: 2px solid rgba(0, 128, 0, 0.7);
}

.green {
  color: rgba(0, 128, 0, 0.7);
}
</style>
