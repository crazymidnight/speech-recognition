<template>
  <div id="app">
    <Header/>
    <div id="upload">
      <h1>Transform your speech into text easily!</h1>
      <br>
      <vue-dropzone ref="myVueDropzone" id="dropzone" :options="dropzoneOptions"></vue-dropzone>
    </div>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import vue2Dropzone from "vue2-dropzone";
import "vue2-dropzone/dist/vue2Dropzone.min.css";

export default {
  name: "app",
  components: {
    Header,
    vueDropzone: vue2Dropzone
  },
  data: function() {
    return {
      dropzoneOptions: {
        url: "http://localhost:8000/post",
        thumbnailWidth: 150,
        maxFilesize: 500,
        headers: { "My-Awesome-Header": "header value" },
        acceptedFiles: ".wav"
      }
    };
  }
};
</script>

<style>
#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #111111;
}
#upload {
  display: flex;
  flex-direction: column;
  align-items: center;
}
h1 {
  font-size: 40px;
  font-weight: 200;
  margin-top: 200px;
}
#dropzone {
  width: 20%;
}
html {
  font-family: Helvetica;
}
body {
  margin: 0;
}
</style>
