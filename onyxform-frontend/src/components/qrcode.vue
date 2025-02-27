<template>
  <div class="container">
    <div class="card">
      <div ref="qrCodeContainer" class="qr-code-box">
        <img src="/images/onyxlogo.jpg" />
        <h1 class="title">Your Onyx Member QR Code</h1>
        <qrcode-vue :value="qrCodeData" :size="200" level="H" render-as="canvas"></qrcode-vue>
      </div>
      <button ref="downloadButton" @click="captureQRCode" class="download-btn">
        Download QR Code
      </button>
      <p><strong>Note:</strong> Please save your QR code for scanning at the Frontdesk.</p>
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

      // Capture QR Code area with title
      html2canvas(qrContainer).then((canvas) => {
        const link = document.createElement("a");
        link.href = canvas.toDataURL("image/png");
        link.download = "Onyx_Member_QR.png";
        link.click();

        downloadBtn.style.display = "block";
        downloadBtn.style.margin = "13px auto";

      });
    },
  },
};
</script>

<style scoped>
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
  padding: 30px;
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
  color: rgb(24, 24, 24);
  margin-bottom: 15px;
}

/* QR Code Box */
.qr-code-box {
  background: white;
  padding: 25px;
  border-radius: 10px;
  display: inline-block;
  text-align: center;
}
.qr-code-box img{
  width: 100px;
  border-radius: 100px;
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
p{
  font-size: 0.7rem !important;
}
</style>
