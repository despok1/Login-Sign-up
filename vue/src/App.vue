<script setup lang="ts">

</script>

<template>
  <div class="container">
    <!-- Switcher -->
    <section class="center-position">
      <div class="row">
        <div>
          <span>LOG IN</span> <span class="micro-padding">SIGN UP</span>
        </div>
        <div class="form-check form-switch">
          <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
        </div>
      </div>
    </section>
    <section class="center-position">
      <div class="block-form text-center">
        <h4>Log In</h4>
        <div>
          <input type="email" name="logemail" class="form-style" placeholder="Your Email" id="logemail"
            autocomplete="off">
        </div>
        <div>
          <input type="password" name="logpass" class="form-style" placeholder="Your Password" id="logpass"
            autocomplete="off">
        </div>
        <!-- Submit -->
        <div>
          <button class="button-submit-shiny button-submit">Submit</button>
        </div>
        <div class="forgot-password-shiny">Forgot your password?</div>
      </div>
      <!-- INPUTS -->
    </section>
  </div>
</template>

<style scoped>
.center-position {
  display: flex;
  justify-content: center;
  align-items: center;
}

.micro-padding {
  padding-left: 30px;
}

.block-form {
  width: 400px;
  /* height: 350px; */
  background: #343541;
}

.forgot-password-shiny:hover {
  color: yellow;
}

.button-submit-shiny:hover {
  background-color: rgb(33, 60, 133);
}

.button-submit {
  border-radius: 10px 10px 10px 10px;
  -webkit-border-radius: 10px 10px 10px 10px;
  -moz-border-radius: 10px 10px 10px 10px;
}
</style>
