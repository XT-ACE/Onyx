<template>
  <div class="form-container">
    <!-- New Fields Above the Form -->
    <div class="privacy-section">
      <label>
        <input v-model="formData.agreeToPrivacy" type="checkbox" required /> 
        I agree to the <span class="highlight">Data Protection and Privacy Statement</span>
      </label>
      <span v-if="!formData.agreeToPrivacy" class="error-message">This is a required field</span>
    </div>

    <div class="responsible-gaming-section">
      <label>
        <input v-model="formData.isOver21" type="checkbox" required /> 
        I am over 21 years old
      </label>
      <span v-if="!formData.isOver21" class="error-message">This is a required field</span>
    </div>

    <h2>Welcome to Onyx Casino</h2>
    <form @submit.prevent="submitForm" class="form">
      <div class="form-row">
        <select v-model="formData.title" required>
          <option value="" disabled>Title</option>
          <option value="Mr">Mr</option>
          <option value="Mrs">Mrs</option>
          <option value="Ms">Ms</option>
        </select>
        <input v-model="formData.last_name" placeholder="Surname" required />
      </div>
      <div class="form-row">
        <input v-model="formData.first_name" placeholder="Given Name" required />
        <input v-model="formData.age" type="number" placeholder="Age" required />
        <span v-if="formData.age && formData.age < 21" class="error-message">You must be 21 or older</span>
      </div>
      <div class="form-row">
        <input v-model="formData.citizenship" placeholder="Citizenship" required />
        <input v-model="formData.mobile_number" placeholder="Mobile Number" required />
      </div>
      <div class="form-row">
        <input v-model="formData.email_address" type="email" placeholder="Email Address" required />
      </div>
      
      <!-- Updated Present and Permanent Address Fields -->
      <div class="form-row">
        <label>
          <input type="checkbox" v-model="formData.present_address" /> Present Address
        </label>
        <label>
          <input type="checkbox" v-model="formData.permanent_address" /> Permanent Address
        </label>
      </div>

      <div class="form-row">
        <input v-model="formData.country_residence" placeholder="Country of Residence" required />
      </div>
      <div class="form-row">
        <input v-model="formData.street_address" placeholder="Street Address" required/>
        <input v-model="formData.valid_id" placeholder="Valid ID" required />
      </div>
      <div class="form-row">
        <input v-model="formData.id_no" placeholder="ID No" />
        <input v-model="formData.photo_id" placeholder="Photo ID" />
      </div>
      <div class="form-row">
        <input v-model="formData.work_industry" placeholder="Work Industry" required />
        <input v-model="formData.role" placeholder="Role" required />
      </div>
      <div class="form-row">
        <input v-model="formData.income" type="number" placeholder="Income" required />
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      users: [],
      formData: {
        title: '',
        last_name: '',
        first_name: '',
        age: '',
        citizenship: '',
        mobile_number: '',
        email_address: '',
        present_address: false,  // Changed to boolean for checkbox
        permanent_address: false,  // Changed to boolean for checkbox
        country_residence: '',
        street_address: '',
        valid_id: '',
        id_no: '',
        photo_id: '',
        work_industry: '',
        role: '',
        income: '',
        agreeToPrivacy: false,
        isOver21: false
      }
    };
  },
  methods: {
    async fetchUsers() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/form-records/');
        this.users = response.data;
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },
    async submitForm() {
      if (this.formData.age && this.formData.age < 21) {
        alert('You must be 21 or older to submit this form.');
        return;
      }
      if (!this.formData.agreeToPrivacy || !this.formData.isOver21) {
        alert('Please agree to the privacy statement and confirm you are over 21.');
        return;
      }

      // Convert checkboxes to strings before sending data
      const submissionData = {
        ...this.formData,
        present_address: this.formData.present_address ? "Yes" : "No",
        permanent_address: this.formData.permanent_address ? "Yes" : "No",
      };

      try {
        await axios.post('http://127.0.0.1:8000/api/form-records/', submissionData);
        this.fetchUsers(); // Refresh user list
      } catch (error) {
        console.error('Error submitting form:', error);
      }
    }
  },
  mounted() {
    this.fetchUsers();
  }
};
</script>

<style scoped>
.form-container {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  font-size: 24px;
  color: #333;
  margin-bottom: 20px;
}

.privacy-section, .responsible-gaming-section {
  margin-bottom: 15px;
}

label {
  font-size: 16px;
  color: #333;
}

input[type="checkbox"] {
  margin-right: 10px;
}

.error-message {
  color: red;
  font-size: 12px;
  display: block;
  margin-top: 5px;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-row {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}

.form-row input, .form-row select {
  width: 48%;
  padding: 12px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-sizing: border-box;
}

.form-row input:focus, .form-row select:focus {
  border-color: #007BFF;
  outline: none;
}

button {
  padding: 12px 20px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #0056b3;
}

@media (max-width: 768px) {
  .form-row input, .form-row select {
    width: 100%;
  }

  .form-container {
    padding: 15px;
  }

  button {
    width: 100%;
  }
}

@media (max-width: 480px) {
  h2 {
    font-size: 20px;
  }

  button {
    padding: 10px 15px;
  }
}
</style>
