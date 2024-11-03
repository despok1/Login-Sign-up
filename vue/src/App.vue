<script setup lang="ts">

</script>

<template>
  <div class="section a-lot-height modal-dialog-centered">
    <div class="container text-center">
      <div class="row">
        <div class="form-check form-switch">
          <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
          <label class="form-check-label" for="flexSwitchCheckDefault">Default switch checkbox input</label>
        </div>
      </div>
      <div class="row">
        <div class="row mb-3">
          <label for="colFormLabelSm" class="col-sm-2 col-form-label col-form-label-sm">Email</label>
          <div class="col-sm-10">
            <input type="email" class="form-control form-control-sm" id="colFormLabelSm"
              placeholder="col-form-label-sm">
          </div>
        </div>
        <div class="row mb-3">
          <label for="colFormLabel" class="col-sm-2 col-form-label">Email</label>
          <div class="col-sm-10">
            <input type="email" class="form-control" id="colFormLabel" placeholder="col-form-label">
          </div>
        </div>
        <div class="row">
          <label for="colFormLabelLg" class="col-sm-2 col-form-label col-form-label-lg">Email</label>
          <div class="col-sm-10">
            <input type="email" class="form-control form-control-lg" id="colFormLabelLg"
              placeholder="col-form-label-lg">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.a-lot-height {
  height: 1000px;
}
</style>
