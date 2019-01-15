<template>
  <div id="app">

    <h1>Transform your speech into text easily!</h1>
    <vue-dropzone ref="myVueDropzone" id="dropzone" :options="dropzoneOptions"></vue-dropzone>
  </div>
</template>

<script>
  import vue2Dropzone from 'vue2-dropzone'
  import 'vue2-dropzone/dist/vue2Dropzone.min.css'

  export default {
    name: 'app',
    components: {
      vueDropzone: vue2Dropzone,
    },
    data: function () {
      return {
        dropzoneOptions: {
          url: 'http://localhost:8000/post',
          thumbnailWidth: 150,
          maxFilesize: 500,
          headers: { "My-Awesome-Header": "header value" },
          acceptedFiles: ".wav",

        }
      }

    }
  }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
