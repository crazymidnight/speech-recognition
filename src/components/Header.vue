<template>
  <div class="hello">
    <header>
      <a href="/">
        <img src="../assets/logo.png" alt="Logo" class="logo">
      </a>
      <a href="/" class="header-text">Speech Recognition</a>
    </header>
  </div>
</template>

<script>
export default {
  name: "Header",
  props: {}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
header {
  background: #17005a;
  height: 88px;
  display: flex;
  flex-direction: row;
}
.logo {
  width: 128px;
  line-height: 88px;
  margin-left: 20px;
  margin-top: 15px;
}
.header-text {
  font-size: 30px;
  text-align: left;
  text-decoration: none;
  color: white;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  line-height: 88px;
  margin-left: 10px;
}
</style>
