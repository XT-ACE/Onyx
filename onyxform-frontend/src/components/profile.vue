<template>
    <div class="profile-container" v-if="formData">
      <div class="profile-card">
        <h1 class="profile-title">Onyx User Profile</h1>
  
        <div class="profile-section">
          <h2>Personal Information</h2>
          <p><strong>Full Name:</strong> {{ formData.title }} {{ formData.first_name }} {{ formData.last_name }}</p>
          <p><strong>Age:</strong> {{ formData.age }}</p>
          <p><strong>Date of Birth:</strong> {{ formData.date_of_birth }}</p>
          <p><strong>Place of Birth:</strong> {{ formData.place_of_birth }}</p>
          <p><strong>Gender:</strong> {{ formData.gender }}</p>
          <p><strong>Nationality:</strong> {{ formData.nationality }}</p>
        </div>
  
        <div class="profile-section">
          <h2>Contact Information</h2>
          <p><strong>Email:</strong> {{ formData.email_address }}</p>
          <p><strong>Phone:</strong> {{ formData.mobile_number }}</p>
        </div>
  
        <div class="profile-section">
          <h2>Address</h2>
          <p><strong>Present Address:</strong> {{ formData.street_address }}, {{ formData.city_residence }}, {{ formData.state_residence }}</p>
          <p v-if="!formData.same_address">
            <strong>Permanent Address:</strong> {{ formData.permanent_street_address }}, {{ formData.permanent_city }}, {{ formData.permanent_state }}
          </p>
        </div>
  
        <div class="profile-section">
          <h2>Work & Income</h2>
          <p><strong>Industry:</strong> {{ formData.work_industry }}</p>
          <p><strong>Role:</strong> {{ formData.role }}</p>
          <p><strong>Income:</strong> {{ formData.income }}</p>
        </div>
  
        <div class="profile-section">
          <h2>Identification</h2>
          <p><strong>Valid ID:</strong> {{ formData.valid_id }}</p>
          <p><strong>ID Number:</strong> {{ formData.id_no }}</p>
          <p><strong>Valid Until:</strong> {{ formData.valid_until }}</p>
  
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
          <h2>Privacy & Consent</h2>
          <p><strong>Marketing Consent:</strong> {{ formData.marketing_consent ? 'Yes' : 'No' }}</p>
          <p><strong>Privacy Consent:</strong> {{ formData.privacy_consent ? 'Yes' : 'No' }}</p>
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
          console.warn("User is not logged into Django Admin.");
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

      } catch (error) {
        console.error("Error fetching user data:", error);
        alert("An error occurred while fetching user details.");
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
  /* General styling */
  .profile-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    padding: 20px;
  }
  
  .profile-card {
    background: white;
    max-width: 600px;
    width: 100%;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  .profile-title {
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
  }
  
  .profile-section {
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 1px solid #eee;
  }
  
  .profile-section h2 {
    font-size: 18px;
    color: #555;
    margin-bottom: 10px;
  }
  
  .profile-section p {
    font-size: 16px;
    margin: 5px 0;
  }
  
  /* Image styling */
  .id-images {
    display: flex;
    gap: 15px;
    margin-top: 10px;
  }
  
  .id-images img {
    width: 100px;
    height: 60px;
    border-radius: 5px;
    border: 1px solid #ddd;
    object-fit: cover;
  }
  
  /* Loading State */
  .loading-container {
    text-align: center;
    font-size: 18px;
    color: #555;
    padding: 50px;
  }
  
  /* Responsive Design */
  @media (max-width: 768px) {
    .profile-card {
      max-width: 100%;
      padding: 15px;
    }
  
    .id-images {
      flex-direction: column;
    }
  
    .id-img {
      width: 100%;
      height: auto;
    }
  }
  </style>
  