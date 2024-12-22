<script setup>
import { onMounted } from 'vue';
onMounted(() => {
  let logIn = document.querySelector(".log-in-form");
  let signUp = document.querySelector(".sign-up-form");
  let switcher = document.querySelector(".form-check-input")
  let inputNameSignUp = document.querySelector(".sign-up-input-name")
  let inputEmailSignUp = document.querySelector(".sign-up-input-email")
  let inputPasswordSignUp = document.querySelector(".sign-up-input-password")
  let inputEmailLogIn = document.querySelector(".log-in-input-email")
  let inputPasswordLogIn = document.querySelector(".log-in-input-password")
  let submitButtonLogIn = document.querySelector(".button-submit-login")
  let submitButtonSignUp = document.querySelector(".button-submit-signup")

  
  submitButtonLogIn.onclick = function(){
    // console.log(inputEmailLogIn.value.length);  
    // if (inputEmailLogIn.value != "") {
    //   console.log("noPysta");
    // }
    if (inputPasswordLogIn.value.length >= 8) {
      console.log("noPysta23");
      inputPasswordLogIn.classList.add("green")
    }
    else{
      console.log("dd");
      inputPasswordLogIn.classList.add("red")
    }
  }

  submitButtonSignUp.onclick = function(){
    
  }

  switcher.onclick = function(){
    logIn.classList.toggle("opacity-0")
    signUp.classList.toggle("opacity-0")
  }
  



})
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
          <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
        </div>
      </div>
    </section>

    <!-- Sign Up -->
    <section class="center-position sign-up-form opacity-0">
      <div class="container block-form text-center">
        <div class="row content">
          <h4 class="pb-4 log-in-font-size"><strong>Sign Up</strong></h4>
          <!-- Your Full Name -->
          <div class="pb-2 position-relative">
            <input type="submit" name="logemail" class="form-style inputs sign-up-input-name" placeholder="Your Name" id="logemail"
              autocomplete="off">
            <i class="input-icon uil uil-user"></i>
          </div>
          <!-- Your Email -->
          <div class="pb-2 position-relative">
            <input type="email" name="logemail" class="form-style inputs sign-up-input-email" placeholder="Your Email" id="logemail2"
              autocomplete="off">
            <i class="input-icon uil uil-at"></i>
          </div>
          <!-- Your Password -->
          <div class="pb-4 position-relative">
            <input type="password" name="logpass" class="form-style inputs sign-up-input-password" placeholder="Your Password" id="logpass2"
              autocomplete="off">
            <i class="input-icon uil uil-lock-alt"></i>
          </div>
          <!-- Submit -->
          <div class="pb-4">
            <button class="button-submit-shiny button-submit button-submit-signup"><strong>Submit</strong></button>
          </div>
        </div>
      </div>
    </section>

    <!-- Log In Block -->
    <section class="center-position log-in-form">
      <div class="container block-form text-center">
        <div class="row content">
          <h4 class="pb-4 log-in-font-size"><strong>Log In</strong></h4>
          <!-- Your Email -->
          <div class="pb-2 position-relative">
            <input type="email" name="logemail" class="form-style inputs log-in-input-email" placeholder="Your Email" id="logemail1"
              autocomplete="off">
            <i class="input-icon uil uil-at"></i>
          </div>
          <!-- Your Password -->
          <div class="pb-4 position-relative">
            <input type="password" name="logpass" class="form-style inputs log-in-input-password" placeholder="Your Password" id="logpass1"
              autocomplete="off">
            <i class="input-icon uil uil-lock-alt"></i>
          </div>
          <!-- Submit -->
          <div class="pb-4">
            <button class="button-submit-shiny button-submit button-submit-login"><strong>Submit</strong></button>
          </div>
          <!-- Forgot your password? -->
          <div class="forgot-password">Forgot your password?</div>
        </div>
      </div>
    </section>

  </div>
</template>

<style scoped>
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
  height: 320px;
  background: #2a2b38;
  background-image: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/1462889/pat.svg');
  border-radius: 5px;
  background-position: bottom center;
  background-repeat: no-repeat;
  background-size: 300%;
}

.forgot-password {
  font-size: 12px;
  transition: 1s;
}

.forgot-password:hover {
  color: #ffeba7;
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

.uil-lock-alt::before {
  color: #ffeba7;
  position: absolute;
  left: 7%;
  bottom: 57%;
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
.red{
  color: red;
  border: 2px solid red;
}
.green{
  color: green;
  border: 2px solid green;
}
</style>
