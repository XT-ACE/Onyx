<template>
    <div class="profile-container" v-if="formData">
      <div class="profile-card">
        <div class="profile-header">
    <img src="/images/pagcor.png" />
    <div class="header-text">
    <h1>ONYX CASINO</h1>
    <h2>MEMBERSHIP CARD</h2>
    <h2>APPLICATION FORM</h2>
    <p>FORM NO. MD-1040</p>
    <p>REV.6 | OCT 17, 2024</p>
  </div>
    <img src="/images/onyxlogo.jpg" class="onyx"/>
  </div>
  <div class="not-allowed-list">
    <ul>
    <li>♠️ <strong>Government Official</strong> or employee connected directly with the operation of the <strong>Government</strong> or any of its agencies.</li>
    <li>♠️ Member of the <strong>Armed Forces of the Philippines</strong>, including the Army, Navy, Air Force, or the Philippine National Police.</li>
    <li>♠️ Persons <strong>under 21</strong> years of age.</li>
    <li>♠️ Persons included in the PAGCOR's National Database of Restricted Persons (<strong>NDRP</strong>).</li>
    <li>♠️ Gaming Employment License (<strong>GEL</strong>) holder.</li>
    <li>Funds or credits in the account of player who is found ineligible to play shall mean forfeiture of said funds/credits in favor of the Government.</li>
  </ul>
  </div>
        <h1 class="profile-title">Onyx Member Profile</h1>
  
        <div class="profile-info">
        <div class="personal-info">
          <h2>Personal Information</h2>
          <p><strong>Full Name:</strong> {{ formData.title }} {{ formData.first_name }} {{ formData.last_name }}</p>
          <p><strong>Age:</strong> {{ formData.age }}</p>
          <p><strong>Date of Birth:</strong> {{ formData.date_of_birth }}</p>
          <p><strong>Place of Birth:</strong> {{ formData.place_of_birth }}</p>
          <p><strong>Gender:</strong> {{ formData.gender }}</p>
          <p><strong>Nationality:</strong> {{ formData.nationality }}</p>
        </div>
  
        <div class="personal-info">
          <h2>Contact Information</h2>
          <p><strong>Email:</strong> {{ formData.email_address }}</p>
          <p><strong>Phone:</strong> {{ formData.mobile_number }}</p>
        </div>
  </div>
        <div class="profile-section">
          <h2>Address</h2>
          <p><strong>Present Address:</strong> {{ formData.street_address }}, {{ formData.city_residence }}, {{ formData.state_residence }}</p>
          <p v-if="!formData.same_address">
            <strong>Permanent Address:</strong> {{ formData.permanent_street_address }}, {{ formData.permanent_city }}, {{ formData.permanent_state }}
          </p>
        </div>
  
        <div class="profile-section">
         <div class="verification">
          <div class="income-indentification">
          <h2>Work & Income</h2>
          <p><strong>Industry:</strong> {{ formData.work_industry }}</p>
          <p><strong>Role:</strong> {{ formData.role }}</p>
          <p><strong>Income:</strong> {{ formData.income }}</p>
        </div>
        <div class="income-indentification">
          <h2>Identification</h2>
          <p><strong>Valid ID:</strong> {{ formData.valid_id }}</p>
          <p><strong>ID Number:</strong> {{ formData.id_no }}</p>
          <p><strong>Valid Until:</strong> {{ formData.valid_until }}</p>
        </div>
      </div>
          <div class="id-images">
        <div>
          <h3>Front ID</h3>
          <img v-if="frontIDPreview" :src="frontIDPreview" alt="Front ID Preview" class="id-image" />
        </div>
        <div>
          <h3>Back ID</h3>
          <img v-if="backIDPreview" :src="backIDPreview" alt="Back ID Preview" class="id-image" />
        </div>
      </div>
        </div>
  
        <div class="profile-section">
          <div class="member-agreement">
          <h2>Member Agreement</h2>
          <div class="consents">
          <p><strong>Marketing Consent:</strong> {{ formData.marketing_consent ? '✔' : ' ✘' }}</p>
          <p><strong>Privacy Consent:</strong> {{ formData.privacy_consent ? '✔' : ' ✘' }}</p>
        </div>
        <div class="conditions">
          <p><strong>Terms & Conditions:</strong> {{ formData.agreeToPrivacy  ? '✔' : ' ✘' }}</p>
          <p><strong>21 Years Old Above:</strong> {{ formData.agreeToPrivacy  ? '✔' : ' ✘' }}</p>
        </div>
        </div>
      </div>

        <div class="verified-section">
          <div class="member-signature">
            <p>Signature Over Printed Name</p>
            <img v-if="signature" :src="signature" alt="User Signature" class="signature-image"/>
            <div class="signature-line">________________</div>
            <p>{{ formData.title }} {{ formData.first_name }} {{ formData.last_name }}</p>
          </div>
          <div class="pagcor-signature">
  <p>VERIFIED BY:</p>
  <div class="signature-line">________________</div>
  <p>PAGCOR I.S.</p>
</div>
</div>
      </div>
    </div>
  
    <div v-else class="loading-container">
      <p>Loading user data...</p>
    </div>
  </template>
  
  <script>
export default {
  data() {
    return {
      formData: null,  // API response data
      frontIDPreview: null, // Image preview for front ID
      backIDPreview: null,  // Image preview for back ID
      signature: null,
    };
  },
  async created() {
    await this.checkAdminSession(); // Check if already logged into Django Admin
    await this.fetchUserData();
  },
  methods: {
    async checkAdminSession() {
      try {
        const response = await fetch("http://192.168.1.11:8000/api/authenticated-user/", {
          method: "GET",
          credentials: "include",  // Allows cookies to be sent for session auth
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (!response.ok) {
          console.warn("Staff is not logged into Admin.");
          return;
        }

        const data = await response.json();
        console.log("Admin User:", data); // Log admin user data

      } catch (error) {
        console.error("Error checking admin session:", error);
      }
    },

    async fetchUserData() {
      const id = this.$route.params.id;

      if (!id) {
        console.error("User ID is missing in route params.");
        alert("Invalid request. No user ID found.");
        this.$router.push("/");
        return;
      }

      try {
        const response = await fetch(`http://192.168.1.11:8000/api/form-records/${id}/`, {
          method: "GET",
          credentials: "include",  // Ensures session cookies are sent
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (!response.ok) {
          throw new Error(`Failed to fetch user: ${response.statusText}`);
        }

        const userData = await response.json();
        this.formData = userData;

        // Generate preview URLs
        this.frontIDPreview = this.getFullImageUrl(userData.id_front);
        this.backIDPreview = this.getFullImageUrl(userData.id_back);
        this.signature = this.getFullImageUrl(userData.signature);


      } catch (error) {
        console.error("Error fetching user data:", error);
        alert("An error occurred while fetching user details. This Scanning is For Onyx Facility Only!");
      }
    },

    getFullImageUrl(imagePath) {
      if (!imagePath) return null;
      return imagePath.startsWith("http") ? imagePath : `http://192.168.1.11:8000${imagePath}`;
    }
  }
};

</script>
  
  <style>
/* PDF-like Styling */
.profile-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #f0f0f0; /* Light gray to resemble a document background */
  padding: 40px 10px;
}

.profile-card {
  background: white;
  max-width: 750px; /* A4-like width */
  width: 100%;
  padding: 40px;
  border-radius: 0;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15); /* Subtle shadow for paper effect */
  font-family: 'Arial', Times, serif; /* Traditional document font */
  color: #222;
  border: 1px solid #ccc; /* Paper-like border */
}
.profile-header{
  display: flex;
  justify-content: space-between;
  align-items: center;
  line-height: 1rem;
}
.header-text{
  text-align: center;
}
.profile-header img{
  width: 100px;
}

.header-text h1{
  font-size: clamp(2rem, 2vw, 2.5rem);
  font-weight: 800;
}

.header-text h2{
  font-size: clamp(1rem, 1vw, 1.5rem);
  line-height: 0.5rem;
  font-weight: 800;
}
.header-text p{
  line-height: 0.2rem;
  font-size: 0.7rem;
}
.onyx{
  border-radius: 100px;
}
.profile-title {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  text-transform: uppercase;
  color: #000;
  border-bottom: 2px solid #000;
  margin-top: -1rem;
}

.profile-section {
  border-bottom: 1px dashed #888; /* Dashed divider to look like document sections */
  margin-top: -0.3rem;
}
.profile-section p{
  font-size: 10px;
}
.profile-info{
  display: flex;
  justify-content: space-between;
  border-bottom: 1px dashed #888; /* Dashed divider to look like document sections */
  margin-top: -1rem;
}
.profile-section h2 {
  font-size: 15px;
  color: #000;
  text-decoration: underline;
}

.personal-info  h2 {
  font-size: 15px;
  color: #000;
  text-decoration: underline;
}
.personal-info  p {
  font-size: 10px;
  margin-top: -0.5rem;
}
.verification{
  display: flex;
  justify-content: space-between;
  margin-top: -0.5rem;
}
.verification p{
  margin-top: -0.5rem;
  font-size: 10px;
}
.not-allowed-list li{
  list-style: none;
  line-height: 1rem;
  font-size: 12px;
  margin-left: -2rem;
  
}
.not-allowed-list strong{
  color: red;
}
strong {
  font-weight: bold;
  text-transform: uppercase;
  font-size: 10px;
}

/* Image Styling */
.id-images {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.id-images div {
  text-align: center;
  flex: 1;
}

.id-images h3 {
  font-size: 15px;
  text-transform: uppercase;
  margin-bottom: 0px;
}

.id-images img {
  width: 200px;
  height: 100px;
  border: 1px solid #000;
  object-fit: cover;
}

/* Loading State */
.loading-container {
  text-align: center;
  font-size: 20px;
  font-style: italic;
  color: #666;
  padding: 50px;
}
.verified-section {
  position: relative;
  margin-top: 0px;
  padding-right: 20px;
  display: flex;
  justify-content: space-between;
}

.verified-section p {
  font-size: 12px;
  font-weight: bold;
  text-transform: uppercase;

}
.member-signature{
  height: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.pagcor-signature{
  display: flex;
  flex-direction: column;
  align-items: center;
}
.pagcor-signature p{
  margin-bottom: 3rem;
}
.signature-image{
  height: 40px;
  width: 100px;
}
.member-agreement{
  list-style: 1px;
}
.consents{
  display: flex;
  justify-content: space-between;
  margin-top: -1rem;
}
.conditions{
  display: flex;
  justify-content: space-between;
  margin-top: -1rem;
}
/* Print Styles */
@media print {
  body {
    background: white !important;
  }

  .profile-container {
    box-shadow: none !important;
    padding: 40px 10px !important; /* Keep desktop padding */
  }

  .profile-card {
    box-shadow: none !important;
    border: none !important; /* Keep desktop border */
    padding: 40px !important; /* Keep desktop padding */
  }

  .profile-header {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    line-height: 1rem !important; /* Keep desktop line height */
  }

  .profile-header img {
    width: 100px !important; /* Ensure desktop size */
  }

  .id-images {
    flex-direction: row !important; /* Keep row layout */
  }

  .header-text h1 {
    font-size: clamp(2rem, 2vw, 2.5rem) !important;
    font-weight: 800 !important;
  }

  .header-text h2 {
    font-size: clamp(1rem, 1vw, 1.5rem) !important;
    line-height: 0.5rem !important;
    font-weight: 800 !important;
  }

  .header-text p {
    line-height: 0.2rem !important;
    font-size: 0.7rem !important;
  }

  .not-allowed-list li {
    list-style: none !important;
    line-height: 1rem !important;
    font-size: 8px !important;
    margin-left: -2rem !important;
  }
  .verified-section{
  flex-direction: row !important;
}
.profile-info{
  flex-direction: row !important;
}
.verification{
  flex-direction: row !important;
}
}


@media (max-width: 768px) {
.profile-header{
  line-height: 2rem;
}
  .profile-header img{
    width: 80px;
  }
  .id-images{
    flex-direction: column;
  }
  .header-text h1{
  font-size: 1.2rem;
  }
  .header-text h2{
  font-size: 0.6rem;
  line-height: 0.5rem;
  font-weight: 800;
}
.profile-info{
  flex-direction: column;
}
.verification{
  flex-direction: column;
}
.header-text p{
  line-height: 0.3rem;
  font-size: 0.5rem;
}
.verified-section{
  flex-direction: column;
}
}
  </style>
  