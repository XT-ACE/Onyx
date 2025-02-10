<template>
    <div class="container">
      <div class="card">
        <h1 class="title">Your Onyx Member QR Code</h1>
        <div ref="qrCodeContainer" class="qr-code-box">
          <qrcode-vue :value="qrCodeData" :size="200" level="H" render-as="canvas"></qrcode-vue>
        </div>
        <button ref="downloadButton" @click="captureQRCode" class="download-btn">
          Download QR Code
        </button>
      </div>
    </div>
  </template>
  
  <script>
  import { nextTick } from "vue";
  import QrcodeVue from "qrcode.vue";
  import html2canvas from "html2canvas";
  
  export default {
    components: {
      QrcodeVue,
    },
    data() {
      return {
        qrCodeData: null,
      };
    },
    created() {
      const id = this.$route.params.id;
      this.qrCodeData = `http://192.168.1.11:5173/profile/${id}`;
    },
    methods: {
      async captureQRCode() {
        const qrContainer = this.$refs.qrCodeContainer;
        const downloadBtn = this.$refs.downloadButton;
  
        // Hide the button before capturing
        downloadBtn.style.display = "none";
  
        await nextTick(); // Wait for Vue to apply changes
  
        // Capture QR Code area
        html2canvas(qrContainer).then((canvas) => {
          const link = document.createElement("a");
          link.href = canvas.toDataURL("image/png");
          link.download = "Onyx_Member_QR.png";
          link.click();
  
          // Show the button again after screenshot
          downloadBtn.style.display = "block";
        });
      },
    },
  };
  </script>
  
  <style>
  /* General Styling */
  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    color: white;
    padding: 20px;
  }
  
  /* Card Styling */
  .card {
    background: #1e1e1e;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(255, 215, 0, 0.3);
    text-align: center;
    max-width: 350px;
    width: 100%;
  }
  
  /* Title */
  .title {
    font-size: 20px;
    font-weight: bold;
    color: gold;
    margin-bottom: 15px;
  }
  
  /* QR Code Box */
  .qr-code-box {
    background: white;
    padding: 10px;
    border-radius: 10px;
    display: inline-block;
  }
  
  /* Download Button */
  .download-btn {
    margin-top: 15px;
    padding: 10px 20px;
    background: gold;
    color: black;
    font-weight: bold;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s ease-in-out;
  }
  
  .download-btn:hover {
    background: #ffcc00;
  }
  </style>
  